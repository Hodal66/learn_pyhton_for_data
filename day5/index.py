print("Welcome to the Unique Person Data Generator!")
print("=====================================================")

# def greet(name="Hodal"):
#     print(f"Hello, {name}! Let's generate some unique person data.")
    
# greet()
# greet(input("Please enter your name: "))

# def check_user_input(user_data):
#     # count = 0
#     # for char in user_data:
#     #     count += 1
#     print(f"Your input has {len(user_data)} characters.")

# user_data = input("Please enter your contents: ")
  
# check_user_input(user_data)

#App to check the square of a number 

# def check_square(number):
#     return number * number
# user_input = int(input("Please enter a number to find its square: "))
# result = check_square(user_input)
# print(f"The square of {user_input} is {result}.")
# print(f"The square of {user_input} is {check_square(user_input)}.")

#How to check factorial of a number

# def check_factorial(number):
#     if number == 0:
#         return 1
#     else:
#         return number * check_factorial(number - 1)
# user_input = int(input("Please enter a number to find its factorial: "))
# result = check_factorial(user_input)
# print(f"The factorial of {user_input} is {result}.")

marks = [85, 90, 78, 92, 88, 76, 95, 89, 84, 91]
numbers = 0
for index, number in enumerate(marks):
    print(f"Index: {index}, Mark: {number}")
    numbers += number

print(f"The sum of all marks is {numbers}.")
print(f"The average of all marks is {numbers / len(marks)}.")
print(f"The highest mark is {max(marks)}.")
print(f"The lowest mark is {min(marks)}.")
print(f"The total marks is {sum(marks)}.")
