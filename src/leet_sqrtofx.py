# # def sqqrt(x):
# #
# #     a = x/2
# #     if x <= 0: return
# #     while (a * a > x):
# #         a = a/2 # 16 x , 8-64,
#
# place = 0
# # s = str(3.67892)
# s = str(0.97892)
# from operator import truediv

# """ # tool 1
# t = 233.97892
# print(s[1])
#
# while (t > 1):
#     t = t / 10
#     print(t)
#
# s = str(t)
# print(s)"""

#
# print(len(s))
# print(i)
#
# ## psudo code for round off
# # first we will iterate from 0th position to end position to see
# #     if the right character is bigger or smaller
# #         if smaller, we take the current character and return its place
# #     we save the new int value to the place found value
#

# tool 2
def not4(x):
t = 233.97892
dot = 1 # as we have reduced it to single digit the decimal is at 1.
print(t, "this is the starting number")
while (t > 1):
    t = t / 10
    print(t)
n = t
print(n, "this is the truncated no.")
s = str(t)
print(s)


if int(s[dot + 1]) >= 5: n = 1
if int(s[dot + 1]) < 4: n = 0
if int(s[dot + 1]) == 4 :
    if int(s[dot + 2]) != 4 : n = 3
    else: n = 0



print(n, " this is the value added to the main number")



