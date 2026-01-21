"""# string methods 1
# .upper() and .lower()
all_low = " There are No Caps Here."
print(all_low.upper())
print(all_low)
print(all_low.lower())


# .isupper() and .islower()
print("Mixed Cases".isupper())
print("Mixed Cases".islower())
print(all_low.islower())


# .isalpha() , isalnum(), isdecimal(), isspace(), istitle()
print("MMM".isalpha())
print("3456".isdecimal())
print("Mixed23".isalnum()) # Mixed or 23, true for either case
print(" ".isspace())  #"" false
print("mixed cases"[5].isspace(), "mixed spaces")  # true as count.char
print("Mixed Cases".istitle())
print("mixed cases".title())

# .startswith, .endswith
print("this is a string".startswith("This")) #"this", true
print("this is a string".endswith("ing")) #ending char or str, true
"""

# .join

print("---".join(["add1","add2","add3"])) #adds only uin between
print("eggs,milk,waffles, beacon".split())
print("eggs milk waffles, beacon".split(" "))
# splits the exact input based on whats inside split
#
# mixed_case = "the string is mixed case"
# x= mixed_case.split()
# print(x)
# print("".join(x))
