weight=float(input("enter your weight in kg:"))
height=float(input("enter your height in m:67"))
BMI=weight/height**2
if BMI>30:
    print("obese")
elif BMI<18.5:
    print("underweight")
else:
    print("normal weight")