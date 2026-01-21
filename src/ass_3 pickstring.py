"""
A customer of a grocery store is purchasing 6 items. The names and prices of the items are as follows:
Penne 16 oz Pack of 12 -            $16.68
Arrabiata Pasta Sauce 24 oz -       $6.98
Bag of 20 Organic Garlic Cloves -   $16.78
Italian Seasoning 1.5 oz Bottle -   $15.26
Artisan Baguettes Twin Pack -       $3.00
12 oz Bag of Meatballs -            $4.39

In a .py file, write a program which calculates the subtotal of all 6 of these items using an expression.
The subtotal is just the sum of all of their prices. Use print() to display the result of the expression."""

# ex = 16.68 + 6.98 + 16.78 + 15.26 + 3.00 + 4.39  # 63.089999999999996
# ex = (1668 + 698 + 1678 + 1526 + 300 + 439) / 100  # 63.09
ex = 16.68 + 6.98 + 16.78 + 15.26 + 3.00 + 4.39  # 63.09
print (round(ex,2))

#strings
x = "orange"
print (x[3])
print("orange"[4])

print(x[:3])
print(x[3:4])
print(x[2:])


print("fuck" + " " +"you")
y= "fuck" + " " +"you"
print (y[2])
print (y[:4])
print (y[2:4])