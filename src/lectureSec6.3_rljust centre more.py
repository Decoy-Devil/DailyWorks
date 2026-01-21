# .rjust , .ljust , .centre(x) x is the character that addsspace
# .strip(), .rstrip(), istrip removes spaces

# print("i had an exciting trip !!11")
# print("i had an exciting trip !!11".strip("1"))
# print("i had an exciting trip !!11".rstrip("1"))
# print("i had an exciting trip !!11".lstrip("1"))

print("demon had an exciting, trip".rstrip("trip")) # works
print("demon had an exciting, trip !@#$%^".rstrip("trip")) #doesnt work
print("demon had an exciting, trip !@#$%^".strip("trip")) #doesnt work
print("demon had an exciting, trip".rstrip("prit")) #works on charac not seq
print("blueeulbbluexxxxeulbblueeulb".strip())
print("blueeulbbluexxxxeulbblueeulb".strip("lbue"))


print("demon had an exciting, trip !!".replace("!!","to hell"))