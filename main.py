points = 0
name = input('What is your name?\n')
print('Hi, %s.' % name)
print('%s, I will give you a quiz.' % name)
q1 = input("Question #1: what is 9907878 X 80097?\n")
if q1 == "793591304166":
  print("Good job!")
  print(" ")
  points += 1
else:
  print("No, that is incorrect.")
print("%s, you got")
print(points)
print("correct out of 1")
