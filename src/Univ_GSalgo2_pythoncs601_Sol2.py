def unhappy_friends(n, preferences, pairs):
    """
    n: number of friends (0..n-1)
    preferences[i]: list of friends in order of i's preference (best -> worst)
    pairs: list of [x, y] meaning x paired with y and y with x
    Returns: number of unhappy friends.
    """
    # Build rank matrix: rank[i][j] = preference rank of j for person i
    # Lower rank = higher preference
    rank = [[0] * n for _ in range(n)]
    for i in range(n):
        for idx, friend in enumerate(preferences[i]):
            rank[i][friend] = idx

    # Build partner mapping
    partner = [None] * n
    for x, y in pairs:
        partner[x] = y
        partner[y] = x

    unhappy_count = 0

    # Check each friend x
    for x in range(n):
        y = partner[x]  # x's current partner

        # Check all friends that x prefers more than y
        for a in preferences[x]:
            if a == y:
                # Reached current partner, everyone after is less preferred
                break

            b = partner[a]  # a's current partner

            # Is this a blocking pair?
            # x prefers a over y (guaranteed by loop structure)
            # AND a prefers x over b?
            if rank[a][x] < rank[a][b]:
                unhappy_count += 1
                break  # x is unhappy, no need to check further

    return unhappy_count



def main():
        print("Running test cases for Problem 2:\n")

        # Example 1
        n1 = 4
        preferences1 = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]]
        pairs1 = [[0, 1], [2, 3]]
        print("Example 1 initial state:")
        print("  n =", n1)
        print("  preferences =", preferences1)
        print("  pairs =", pairs1)
        result1 = unhappy_friends(n1, preferences1, pairs1)
        print(f"Example 1: {result1} (expected 2) {'\u2713' if result1 == 2 else '✗'}\n")

        # Example 2
        n2 = 2
        preferences2 = [[1], [0]]
        pairs2 = [[1, 0]]
        print("Example 2 initial state:")
        print("  n =", n2)
        print("  preferences =", preferences2)
        print("  pairs =", pairs2)
        result2 = unhappy_friends(n2, preferences2, pairs2)
        print(f"Example 2: {result2} (expected 0) {'\u2713' if result2 == 0 else '✗'}\n")

        # Example 3
        n3 = 4
        preferences3 = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]]
        pairs3 = [[1, 3], [0, 2]]
        print("Example 3 initial state:")
        print("  n =", n3)
        print("  preferences =", preferences3)
        print("  pairs =", pairs3)
        result3 = unhappy_friends(n3, preferences3, pairs3)
        print(f"Example 3: {result3} (expected 4) {'\u2713' if result3 == 4 else '✗'}\n")

        # Example 4
        n4 = 4
        preferences4 = [[1, 3, 2], [2, 3, 0], [1, 0, 3], [1, 0, 2]]
        pairs4 = [[2, 1], [3, 0]]
        print("Example 4 initial state:")
        print("  n =", n4)
        print("  preferences =", preferences4)
        print("  pairs =", pairs4)
        result4 = unhappy_friends(n4, preferences4, pairs4)
        print(f"Example 4: {result4} (expected 0) {'\u2713' if result4 == 0 else '✗'}\n")


if __name__ == "__main__":
    main()