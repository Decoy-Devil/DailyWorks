# Python Collections (Arrays)
# There are four collection data types in the Python programming language:
#
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


mylist = ['a','b','c','d', 'a']

print(mylist)
print(type(mylist))

print(mylist[1])
print(mylist[-1]) # iterates from behind
print(mylist[2:4]) # include 2 and till 4
print(mylist[:4]) #excluding 4
mylist[2] = "harmless" # change list items
print(mylist)
mylist[2:4] = ["hero", "zero"] # changing range of items
print(mylist)
mylist[2:3] = ["name", "hiren"] # changing range of items
print(mylist)
mylist[2] = ["pit"]

mylist.append("zzpc")
print(mylist)
mylist.insert(3,'blissful')
print(mylist)
mylist.remove('blissful')  # can use del mylist[1] or del mylist ,to delete all items
print(mylist)
mylist.pop(2)   # can use mylist.clear() to clear all items
print(mylist)