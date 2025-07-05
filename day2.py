# x = input("X : ")
# my_age = 50
# my_full_name = 0.990
# is_boy = False
# y= x + 1
# print(type(x))
# print(type(my_age))
# print(type(my_full_name))
# print(type(is_boy))
# print(f"the value of y {y}")

#let's add two Numbers 
# first_number = input("Enter first Number :")
# last_number = input("Enter last Number :")

# sum_of_two_numbers = int(first_number) + int(last_number)

# print(f"The Sum of {first_number} and {last_number} is equal to {sum_of_two_numbers}")

# print(bool(""))
# print(bool(0))
# print(bool(1))
# print(bool(-1))
# print(bool("False"))
#Quiz What are the primitive types in python?

# print("int, bool, string, float, ")

# fruit = "Apple"
# print(fruit[1])
# print(fruit[1:-1])

#Fundamental of Programming

# if(10>3):
#     print("You are welcome!")

# age =int(input("Enter Your Ages : "))
# message = "Eligible" if age>=30 else "Not Eligible"
# print(message)

# high_income = True
# good_credit = False
# student = False
# if (high_income  or good_credit) and not student:
#     print("Eligible")
# else:
#     print("Not Eligible")

# if not student :
#     print("Eligible")
# else:
#     print("Not Eligible")

# age = int(input("Please Enter your Ages: "))
# if 18 <= age >= 65:
#     print("You are in the Range")
# else:
#     print("You are Not")
# record = 0
# for i in range (1, 6):
#     if i % 2 == 0:
#         record = i
#     if i == 5:
#         break
#     print(record, end=" ")
    
name = "Alice"
age = 25
score = 95.5055

# message = f"Hello {name}, you are {age} years old and scored {score:.1f}"
# message = "Hello {} , you are {} years old and scored {}".format(name,age,score)

# print(message)    

#Common String Methods

text = "  Python Programming  "

# print(text.startswith("Python"))
# print(text.startswith(text.strip("Python")))
# print(text.endswith("Programming"))
# print(text.endswith(text.strip("Programming")))
# print(text.replace("Python","Hodal"))
# length_of_string = len(text.strip())
# print(length_of_string)


#check if the Entered characters contain space and inform the user that there are space

# my_password = input("Enter your Password of 5 characters : ")

# if(len(my_password) == 5):
#     print("The password is correct")
# elif (len(my_password.strip()) == 5):
#     print("The password is correct but contain space")
# else:
#     print("please character should not exceed 5 characters check well : ")


# print(text.isdigit())
# print("1234".isdigit())
# print("Muheto".isdigit())
# print("1234dj".isdigit())
# print(text.isalpha())
# print("A".isalpha())
 
 #cleaning Method
# print(len(text))
# print(len(text.rstrip()))
# print(len(text.lstrip()))
# print(len(text.strip()))

#finding and Counting

print(text.find("gram"))
print(text.count("m"))

full_name = "Muheto Hodal"
splited_names = full_name.split()

first_name = splited_names[0]
last_name = splited_names[1] 

print(f"You first name is {first_name}, your last name is {last_name}")