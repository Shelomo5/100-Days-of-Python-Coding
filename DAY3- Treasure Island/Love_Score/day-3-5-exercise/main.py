# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#TRUE and LOVE TOTAL then Concatenate for Love Score

full_name = name1 + name2 
lower_name = full_name .lower()

t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count('e')
count_true = (t+r+u+e)

l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count('e')
count_love = (l+o+v+e)

love_score = str(count_true) + str(count_love)

if int(love_score) < 10 or int(love_score) > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif int(love_score) <= 50 and int(love_score) >= 40:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")