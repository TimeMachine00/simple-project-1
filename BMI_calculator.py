print("created by hussainatphysics@gmail.com(hussainsha syed")
print("welcome to BMI calculator")

"""
we are creating BMI calculator....i am adding but variable as i am creating exe file noting morethan this

"""


height = float(input("enter your height in m: "))
but1=input("press enter")
weight = float(input("enter your weight in kg: "))

but2= input("press enter")


BMI = round((weight/height**2),2)


if BMI <18.5:
  print(f"your BMI is {BMI}, you are under weight")
elif BMI < 25:
  print(f"your BMI is {BMI}, you have a normal weight")
elif BMI <30:
  print(f"your BMI is {BMI}, you are slightly overweight")
elif BMI<35:
  print(f"your BMI is {BMI}, you are obese")
else:
  print(f"your BMI is {BMI}, you are clinically obese")
print()

but3= input("press enter for BYE!!!!!!!!!!!!!!!dear")