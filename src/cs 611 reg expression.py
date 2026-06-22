r"""
Regex -> epsilon-NFA (Thompson) + NFA simulation for pattern matching.

Supports:
  - Literals (any char except metacharacters unless escaped)
  - Parentheses: ( ... )
  - Union: |
  - Concatenation (implicit)
  - Star: *
  - Plus: +
  - Optional: ?
  - Wildcard: .  (matches any single character)
  - Escape: \\x (treat x as literal)

Pattern matching modes:
  - full_match(text): does the regex match the entire text?
  - search(text): does the regex match some substring of text? (like DFA pattern match)

Author: (you)
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Set, List, Tuple, Optional


# ----------------------------
# NFA data structures
# ----------------------------

EPS = None  # We will use None to represent epsilon transitions
WILDCARD = "__DOT__"  # Special token for '.' wildcard transitions


@dataclass
class NFA:
    """A simple epsilon-NFA representation."""
    start: int
    accept: int
    transitions: Dict[int, Dict[object, Set[int]]]  # state -> (symbol/None) -> next states

    def add_state(self) -> int:
        """Create a new state ID and ensure it exists in the transitions dict."""
        new_id = len(self.transitions)
        self.transitions[new_id] = {}
        return new_id

    def add_edge(self, src: int, sym: object, dst: int) -> None:
        """Add a transition edge (src --sym--> dst), sym can be EPS(None) or a token."""
        if src not in self.transitions:
            self.transitions[src] = {}
        if sym not in self.transitions[src]:
            self.transitions[src][sym] = set()
        self.transitions[src][sym].add(dst)


@dataclass
class Fragment:
    """Thompson fragment: start and accept states of a partial NFA."""
    start: int
    accept: int


# ----------------------------
# Regex parsing: infix -> postfix
# ----------------------------

def is_literal_token(ch: str) -> bool:
    """Return True if character is treated as a literal (not an operator) in infix scanning."""
    return ch not in {'|', '*', '+', '?', '(', ')'}  # concatenation is implicit


def tokenize_regex(regex: str) -> List[str]:
    """
    Tokenize the regex into a list of tokens.
    Handles escapes and wildcard '.'.
    """
    tokens: List[str] = []  # This will store the parsed tokens in order.
    i = 0  # This index moves through the regex string one character at a time.

    while i < len(regex):  # Loop until we have read all characters in the regex.
        ch = regex[i]  # Read the current character.

        if ch == '\\':  # If we see a backslash, the next character is escaped.
            if i + 1 >= len(regex):  # If backslash is at the end, that's invalid.
                raise ValueError("Regex ends with a single backslash '\\'.")
            tokens.append(regex[i + 1])  # Add the escaped character as a literal token.
            i += 2  # Move past the backslash and the escaped character.
            continue  # Continue the main loop.

        if ch == '.':  # If we see '.', we treat it as wildcard token.
            tokens.append('.')  # Store '.' as a distinct token (we handle it in NFA build).
            i += 1  # Move to next character.
            continue  # Continue the main loop.

        # Otherwise, just add the character as its own token (operator or literal).
        tokens.append(ch)  # Append this token to the list.
        i += 1  # Move to next character.

    return tokens  # Return the final list of tokens.


def insert_concat(tokens: List[str]) -> List[str]:
    """
    Insert explicit concatenation operator '·' where concatenation is implicit.
    Example: a(b|c)*d  ->  a · ( b | c ) * · d
    """
    result: List[str] = []  # This will store tokens with explicit concat operators.

    def can_end(tok: str) -> bool:
        """True if tok can appear at the end of a concatenated piece."""
        return (tok not in {'|', '(', '·'}) and tok not in {')'} and tok not in set() or True

    # We'll explicitly compute "left-can-concat" and "right-can-concat" with simple rules:
    def left_can_concat(tok: str) -> bool:
        # A token can be on the left of a concat if it is:
        # - a literal or '.'
        # - ')' (a closed group)
        # - a postfix unary operator (* + ?)
        return tok not in {'|', '('} and tok != '·'

    def right_can_concat(tok: str) -> bool:
        # A token can be on the right of a concat if it is:
        # - a literal or '.'
        # - '(' (an open group)
        return tok not in {'|', ')', '*', '+', '?', '·'}

    for i, tok in enumerate(tokens):  # Walk through tokens with index.
        result.append(tok)  # Always append the current token.

        if i == len(tokens) - 1:  # If this is the last token, no concat after it.
            break  # Exit loop.

        nxt = tokens[i + 1]  # Look at the next token.

        # Insert concat if "tok" can end an atom and "nxt" can start an atom.
        if left_can_concat(tok) and right_can_concat(nxt):
            # Examples: literal followed by literal, ')' followed by '(', '*' followed by literal, etc.
            result.append('·')  # Insert explicit concatenation operator.

    return result  # Return the augmented token list.


def to_postfix(tokens: List[str]) -> List[str]:
    """
    Convert tokens (with explicit concat '·') to postfix using shunting-yard.
    Operator precedence (high to low): postfix unary (* + ?) > concat (·) > union (|)
    """
    output: List[str] = []  # Output list that becomes the postfix expression.
    stack: List[str] = []   # Operator stack used by shunting-yard.

    # Define precedence for each operator.
    prec = {'|': 1, '·': 2, '*': 3, '+': 3, '?': 3}  # Higher number = higher precedence.

    # Define associativity: unary postfix operators are effectively right/none; concat/union left.
    left_assoc = {'|': True, '·': True}  # For these, pop operators of >= precedence.

    for tok in tokens:  # Process tokens one-by-one.
        if tok == '(':
            stack.append(tok)  # Push '(' to mark a group.
        elif tok == ')':
            # Pop until '(' is found.
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if not stack or stack[-1] != '(':
                raise ValueError("Mismatched parentheses in regex.")
            stack.pop()  # Remove '('
        elif tok in prec:
            # tok is an operator.
            if tok in {'*', '+', '?'}:
                # Postfix unary operators: they apply immediately to the previous atom in postfix,
                # so in shunting-yard we can just output them directly.
                output.append(tok)
            else:
                # Binary operators (concat and union): handle precedence popping.
                while stack and stack[-1] in prec:
                    top = stack[-1]
                    # Pop if top has higher precedence, or same precedence and tok is left-assoc.
                    if (prec[top] > prec[tok]) or (prec[top] == prec[tok] and left_assoc.get(tok, True)):
                        output.append(stack.pop())
                    else:
                        break
                stack.append(tok)
        else:
            # tok is a literal (including '.' wildcard token)
            output.append(tok)

    # Pop remaining operators.
    while stack:
        if stack[-1] in {'(', ')'}:
            raise ValueError("Mismatched parentheses in regex.")
        output.append(stack.pop())

    return output


# ----------------------------
# Thompson construction: postfix -> NFA
# ----------------------------

def build_nfa_from_postfix(postfix: List[str]) -> NFA:
    """
    Thompson construction from postfix regex tokens.
    Returns an epsilon-NFA.
    """
    # Initialize an NFA with an empty transitions dict.
    nfa = NFA(start=0, accept=0, transitions={})

    # Create an initial dummy state so add_state works cleanly.
    nfa.add_state()  # state 0 exists now.

    stack: List[Fragment] = []  # Stack of NFA fragments for Thompson construction.

    def new_fragment_for_symbol(sym: str) -> Fragment:
        """Create an NFA fragment for a single symbol transition."""
        s = nfa.add_state()  # start state for this fragment
        t = nfa.add_state()  # accept state for this fragment

        if sym == '.':
            # Wildcard transition: store special token WILDCARD
            nfa.add_edge(s, WILDCARD, t)
        else:
            # Literal transition
            nfa.add_edge(s, sym, t)

        return Fragment(start=s, accept=t)

    for tok in postfix:  # Process postfix tokens in order.
        if tok not in {'|', '·', '*', '+', '?'}:
            # Literal token: push its fragment.
            stack.append(new_fragment_for_symbol(tok))
        elif tok == '·':
            # Concatenation: pop right then left, connect left.accept ->ε-> right.start
            right = stack.pop()
            left = stack.pop()
            nfa.add_edge(left.accept, EPS, right.start)
            stack.append(Fragment(start=left.start, accept=right.accept))
        elif tok == '|':
            # Union: pop right then left, create new start/accept with ε-splits/joins
            right = stack.pop()
            left = stack.pop()
            s = nfa.add_state()
            t = nfa.add_state()
            nfa.add_edge(s, EPS, left.start)
            nfa.add_edge(s, EPS, right.start)
            nfa.add_edge(left.accept, EPS, t)
            nfa.add_edge(right.accept, EPS, t)
            stack.append(Fragment(start=s, accept=t))
        elif tok == '*':
            # Star: pop fragment F, create new start/accept with ε edges (0 or more)
            frag = stack.pop()
            s = nfa.add_state()
            t = nfa.add_state()
            nfa.add_edge(s, EPS, frag.start)   # enter the loop
            nfa.add_edge(s, EPS, t)            # or skip entirely (epsilon)
            nfa.add_edge(frag.accept, EPS, frag.start)  # repeat
            nfa.add_edge(frag.accept, EPS, t)           # exit
            stack.append(Fragment(start=s, accept=t))
        elif tok == '+':
            # Plus: one-or-more. Equivalent to F · F*
            frag = stack.pop()
            # Build F* around a copy of frag (we cannot reuse frag safely without copying states),
            # so we implement plus as: new start -> frag.start, frag.accept -> loop back, etc.
            s = nfa.add_state()
            t = nfa.add_state()
            nfa.add_edge(s, EPS, frag.start)             # must enter once
            nfa.add_edge(frag.accept, EPS, frag.start)   # repeat
            nfa.add_edge(frag.accept, EPS, t)            # exit after >=1
            stack.append(Fragment(start=s, accept=t))
        elif tok == '?':
            # Optional: zero-or-one. Equivalent to (F | ε)
            frag = stack.pop()
            s = nfa.add_state()
            t = nfa.add_state()
            nfa.add_edge(s, EPS, frag.start)  # take it
            nfa.add_edge(s, EPS, t)          # or skip it
            nfa.add_edge(frag.accept, EPS, t)
            stack.append(Fragment(start=s, accept=t))
        else:
            raise ValueError(f"Unknown operator in postfix: {tok}")

    if len(stack) != 1:
        raise ValueError("Invalid regex: postfix did not reduce to a single NFA.")

    final_frag = stack.pop()
    nfa.start = final_frag.start
    nfa.accept = final_frag.accept
    return nfa


# ----------------------------
# NFA simulation
# ----------------------------

def epsilon_closure(nfa: NFA, states: Set[int]) -> Set[int]:
    """Compute epsilon-closure of a set of states."""
    stack = list(states)         # Work stack for DFS over epsilon edges.
    closure = set(states)        # Start closure with the given states.

    while stack:
        s = stack.pop()
        # Get epsilon transitions out of s, if any.
        for nxt in nfa.transitions.get(s, {}).get(EPS, set()):
            if nxt not in closure:
                closure.add(nxt)
                stack.append(nxt)

    return closure


def move(nfa: NFA, states: Set[int], ch: str) -> Set[int]:
    """
    Take one symbol transition from any state in states on input ch.
    Handles wildcard transitions.
    """
    nxt_states: Set[int] = set()

    for s in states:
        trans = nfa.transitions.get(s, {})
        # Literal transition on ch
        if ch in trans:
            nxt_states |= trans[ch]
        # Wildcard transition
        if WILDCARD in trans:
            nxt_states |= trans[WILDCARD]

    return nxt_states


def nfa_full_match(nfa: NFA, text: str) -> bool:
    """Return True iff the NFA matches the entire text."""
    current = epsilon_closure(nfa, {nfa.start})

    for ch in text:
        current = epsilon_closure(nfa, move(nfa, current, ch))

    return nfa.accept in current


def nfa_search(nfa: NFA, text: str) -> bool:
    """
    Return True iff the regex matches some substring of text.
    This simulates starting the NFA at every position (simple, correct).
    """
    n = len(text)

    for i in range(n + 1):
        current = epsilon_closure(nfa, {nfa.start})

        # If empty-string is accepted, we matched at position i immediately.
        if nfa.accept in current:
            return True

        for j in range(i, n):
            current = epsilon_closure(nfa, move(nfa, current, text[j]))
            if nfa.accept in current:
                return True

    return False


# ----------------------------
# Public API: compile + run
# ----------------------------

def compile_regex_to_nfa(regex: str) -> NFA:
    """Compile a regex string into an epsilon-NFA."""
    raw_tokens = tokenize_regex(regex)
    concat_tokens = insert_concat(raw_tokens)
    postfix = to_postfix(concat_tokens)
    return build_nfa_from_postfix(postfix)


def main() -> None:
    """
    Standalone entry point (PyCharm-friendly).

    Edit DEFAULT_REGEX / DEFAULT_TEXT / DEFAULT_MODE below and click Run.
    """
    # -----------------------------
    # EDIT THESE DEFAULTS
    # -----------------------------
    DEFAULT_REGEX = "(a|b)*abb"   # Regular expression to compile
    DEFAULT_TEXT = "xxabbxx"      # Input text to test against
    DEFAULT_MODE = "search"       # "search" (substring) or "full" (entire string)

    # Compile regex into an epsilon-NFA, then run the chosen simulation.
    nfa = compile_regex_to_nfa(DEFAULT_REGEX)

    if DEFAULT_MODE == "full":
        ok = nfa_full_match(nfa, DEFAULT_TEXT)
    else:
        ok = nfa_search(nfa, DEFAULT_TEXT)

    print(f"regex={DEFAULT_REGEX!r} text={DEFAULT_TEXT!r} mode={DEFAULT_MODE!r}")
    print("ACCEPT" if ok else "REJECT")


if __name__ == "__main__":
    main()