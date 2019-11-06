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
q2 = input(' Question #2 In the epic of Gilgamesh, what is the name of the wild man (please capitalize the name, use proper grammar.\n')

if q2 == "Enkidu":
  print("Good job!")
  print(" ")
  points +=1
else:
  print("No, that is incorrect.")


print("%s, you got")
print(points)
print("correct out of 2")
