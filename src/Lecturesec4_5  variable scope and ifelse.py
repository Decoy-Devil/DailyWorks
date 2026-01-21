#
#
# # when function is returned the local variable doesnt exsits
#
# veg = input("type the name of vegetable")
#
# if veg == "corn":
#     print(veg)
#  else:
#     print("fruits")

gpa = float(input("what was the applicant's gpa?"))
inst_app = input("is student going to edu at uni")

if gpa >= 3.7:
    if inst_app == "yes":
        print("app qualifies for loan")
    else:
        print("app doesnt qualify")
else:
    print("app doesnt have grades")

