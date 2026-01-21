arr = [10, 11, 12, 13, 14, 15]

i = 0
y = len ( arr) - 1 # handled the case of outbound at start

print (y)

while (i <= y):    # handling by ignoring the <= trying new != with risk of run away code
    print(arr[y])
    y -= 1
