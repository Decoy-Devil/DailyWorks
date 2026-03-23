# def para_check():
## fail in the case of bracket are intersecting each other like : {}{{(}})
mylist = []
s = ["(", "(", "{", ")" ,"}" ,")"]
a = b = c = 0
print("printing s initial ", s)
print("printing len of s is = ", len(s))

for i in range(len(s)):  # range(len(list))
    print(s[i])
    if (s[i] == "("):  # testing lefts
        mylist.append(i)
        a += 1
    elif (s[i]== "["):
        mylist.append(i)
        b += 1
    elif (s[i] == "{"):
        mylist.append(i)
        c += 1
    elif (s[i] == ")"):  # testing rights
        mylist.append(i)
        a -= 1
    elif (s[i] == "]"):
        mylist.append(i)
        b -= 1
    elif s[i] == "}": # testing no parentheses to if/else if
        mylist.append(i)
        c -= 1
    
    else:
        print("incorrect input")
        print(mylist)

print( a, b, c)
if( a == 0 and b == 0 and c == 0 ):
    print("the input was valid parentheses")
else:
    print("the input was invalid parentheses")
    #x = "()[]{}"
# para_check(x)

    # if (i == "("):  # testing lefts
    #     mylist.append(i)
    #     a += 1
    # elif (i == "["):
    #     mylist.append(i)
    #     b += 1
    # elif (i == "{"):
    #     mylist.append(i)
    #     c += 1
    # elif i == "[":  # testing rights
    #     mylist.append(i)
    #     a -= 1
    # elif (i == "["):
    #     mylist.append(i)
    #     b -= 1
    # elif (i == "["):
    #     mylist.append(i)
    #     c -= 1
    # else:
    #     print("incorrect input")
