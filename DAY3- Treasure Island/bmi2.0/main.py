# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = (weight)/((height)**2)
BMI_int = round(BMI)


if BMI_int < 18.5:
  print(f"Your BMI is {BMI_int}, you are underweight")
elif BMI_int > 18.5 and BMI_int< 25:
  print(f"Your BMI is {BMI_int}, you have normal weight")
elif BMI_int > 25 and BMI_int< 30:
  print(f"Your BMI is {BMI_int}, you are slightly overweight")
elif BMI_int > 30 and BMI_int< 35:
  print(f"Your BMI is {BMI_int}, you are obese")
else:
  print(f"Your BMI is {BMI_int}, you are clinically obese")
  

  

