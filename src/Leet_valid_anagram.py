# Input: s = "anagram", t = "nagaram"
# Output: true

s = ["a","n","a","g","r","a","m"]
t = ["n","a","g","a","r","a","i"]

# for i in s:
#     for j in t:
#

for x in s:
    if x in t:
        print(x, "true")
    else:
        print(x, "not matched")
