# Input: s = "anagram", t = "nagaram"
# Output: true

# s = ["a","n","a","g","r","a","m"]
s = ["p","p","o","l"]
t = ["p","o","o","l"]
# t = ["n","a","g","a","r","a","t"]
# t = ["n","a","g","a","r","a"]

# for i in s:
#     for j in t:
#
if (len(s) != len(t)):
    print("unmatched strings")
    exit()
else:
    for x in s:
        if x in t:
            print(x, "true")
        else:
            print(x, "not matched")


# failing on test case of pool vs ppol, where characters are same but duplicates are different in same length