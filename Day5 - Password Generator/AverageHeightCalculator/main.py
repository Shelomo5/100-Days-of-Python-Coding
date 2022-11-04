# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#Testing #'s 156 178 165 171 187
height_total = 0
item_count = 0
for height in student_heights:
  height_total+=height
  item_count+=1

average_height = round(height_total/item_count)
print(average_height)


