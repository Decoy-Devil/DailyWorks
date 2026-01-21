the_string = "North Dakota"

print(the_string.rjust(17))
print(the_string.ljust(17))

center_plus = the_string.center(16) + "+"
print(center_plus)

print(the_string.lstrip("north")) # case sensitive
print(the_string.lstrip("orthN"))
print(the_string.lstrip("+"))
print(the_string.replace("North","South"))


#len()
print(len(the_string))
print(len("tree brown")) # counts spaces
print(len("tree " + "brown"))
print("antidisestablishmentariananism" [7:20])
#antidis - 7 | 20 ment
print(len("antidisestablishmentariananism" [7:20]))


