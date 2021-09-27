file = open("calculation.txt", "w")
print("Would you like to 1. add, 2. divide, 3. multiply or 4. subtract? Enter 1 to 4")
operation = int(input())
print("Enter a number:")
num1 = int(input())
print("Enter another number:")
num2 = int(input())
if operation == 1:
  answer = num1 + num2
elif operation == 2:
  answer = num1 / num2
elif operation == 3:
  answer = num1 * num2
elif operation == 4:
  answer == num1 - num2
else:
  print("Invalid input")
file.write(str(answer))
file.close()