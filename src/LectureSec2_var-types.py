from operator import truediv



ex_var = 5
ex_var = 7
float_1 = 0.01
int_x = 7
bool_1 = True  #true incorrect
print(ex_var)

# type section 3
print(type(ex_var))
print(type(bool_1))
print(type(float_1))
ex_var = 'c'
print(str(ex_var)) # because the str() doesnt change the global scope level type
# but only the current in-line temp conversion/operation
# doesnt work but below will work
print(type(ex_var), 'type conv of variable by print')
ex_var = str(7)
print(type(ex_var))

# escape sequence
# /t for tab
# /n for new line
# \' AND \" for apostrophe or double quotes <print("here i \'say ")>
print("here i /say ")


