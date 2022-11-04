#Write your code below this row 👇
for number in range(1,101):
  #divisible by 3 and divisible by 5 first bc they overlap
  #with other conditionals
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz") 
  else:
    print(number)
