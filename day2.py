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

# print(text.find("gram"))
# print(text.count("m"))

# full_name = input("Enter your Full name: ")
# splited_names = full_name.split()
# last_name = "Not provided"

# first_name = splited_names[0]
# if(len(splited_names)>1):
#     last_name = splited_names[1] 

# print(f"You first name is {first_name}, your last name is {last_name}")


#CREATING LISTS

#EMPTY_LISTS

# empty_list = []
# empty_list2 = list()
# print(empty_list)
# print(empty_list2)

#LIST WITH DATA
# numbers = [1,2,3,4,5]
# fruits = ['apple','banana','orange']
# mixed = [1, 'hello', 3.14, True, [1,2,3]]
# print(fruits)
# print(mixed[-1])

#LIST FROM A RANGE

range_list = list(range(1,10))
# print(range_list)

#ACCESSING LIST ELEMENTS
fruits = ['apple','banana','orange','grape','kiwi']
# print(fruits)
# print(fruits[0])
# print(fruits[-1])
# print(fruits[-2])

#SLICING

# print(fruits)
# print(fruits[1:4])
# print(fruits[:3])
# print(fruits[2:])
# print(fruits[::2])
# print(fruits[::-1])

#MODIFYING LIST

fruits = ['apple','banana','orange','umugati']

#Adding Element

# fruits.append('grape')
# fruits.insert(1, 'kiwi')
# fruits.extend(['mango','peach'])
# print(fruits)

# fruits.remove('banana')
# fruits.remove(input("Enter to remove: "))
# print(fruits)
# number_of_contents = int(input("How many record you want to insert :"))
# i=1
# if(number_of_contents > 0):
#   while i <= number_of_contents :
#     fruits.insert(1, input("Enter to Add: "))
#     i=i+1
# print(f"The Updated List are : {fruits}")

# print(fruits)

#REMOVING ELEMENTS IN THE LIST

# fruits.remove('banana')
# print(fruits)
# popped = fruits.pop()
# print(fruits)
# print(popped)
# popped_index = fruits.pop(1)
# print(popped_index)
# print(fruits)
# del fruits[1]
# print(fruits)
# print(fruits.clear())

#MODIFYING ELEMENTS

# print(fruits)
# fruits[0] = 'pineapple'
# print(fruits)
# fruits[1:4] = ['cherry','plum','umuganura','umwenda','urubuto']
# fruits.extend(['burigihe','burimunsi'])
# print(fruits)

#LIST METHODS AND OPERATION

numbers = [3,1,4,1,5,9,2,6]

#SORTING AND REVERTING

# numbers.sort()
# numbers.sort(reverse=True)
# numbers.reverse()

# print(numbers)

#DON'T MODIFY ORIGINAL 

sorted_nums = sorted(numbers)
# print(f"Sorted List : {sorted_nums}")
# print(f"Orginal LIst : {numbers}")
# reversed_nums = list(reversed(numbers))
# print(f"List Of Reserved : {reversed_nums}")

# index = sorted_nums.index(4)
# count = numbers.count(1)
# print(count)

# print(len(numbers))
# print(sum(numbers))
# print(max(numbers))
# print(min(numbers))

#LIST OF COMPLEHENSIONS

#BASIC LIST OF COMPREHENSION

# squares = []
# for x in range(10):
#     squares.append(x**2)
# print(squares)

# squares = [x**2 for x in range(10)]
# print(squares)
# even_square = [x**2 for x in range(10) if x % 2 == 0]
# print(even_square)

# words = ['python','java','javascript']

# upper_words = [word.upper() for word in words]
# print(words)
# print(upper_words)

# matrix = [[i*j for j in range(3)] for i in range(3)]

# print(matrix)
number_of_grades = int(input("How Many Number of grades : "))
list_of_grades = []
if(number_of_grades>0):
    i=1
    while i <= number_of_grades : 
        list_of_grades.append(int(input(f"Enter {i} Marks :")))
        i = i + 1
    print(list_of_grades)
    average = sum(list_of_grades) / number_of_grades
    maximum_grade = max(list_of_grades)
    lowest_grade = min(list_of_grades)
    print("You have Entered {} Number of Marks and their Average is {}, The Highest Marks is {} the Lowest Marks is {} ".format(number_of_grades, average, maximum_grade, lowest_grade))
print("You are welcome to this new Tutorial!!!")