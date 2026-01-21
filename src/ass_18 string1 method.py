mixed_case = "A Song of Ice and Fire"
print(mixed_case.isupper())
print(mixed_case.islower())
print(mixed_case.upper())
print(mixed_case.lower())
print(mixed_case.istitle())

title_case = mixed_case.title()
print(title_case)
print(mixed_case.startswith("A"))
print(mixed_case.endswith("ire"))

# --------------------
words = mixed_case.split()
print(words)
# print(mixed_case.join())
print("belows the result")
print("".join(words))
# print(words.isalpha())
# words = "".join(mixed_case)
# print("words_after_assign--", words)
# print("-".join(words).isalpha())

