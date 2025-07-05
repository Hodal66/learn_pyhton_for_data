#While Loop
    

#Do While Loop

# count = 0
# while count <=10 :
#     print(count)
#     count=count+1
    
# #For Loop

# for i in range(30):
#     print(i)
    
# for letter in "Hello":
#     print(letter)


# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
#     def great(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years")
        
# person1 = Person("Alice", 30)

# print(person1)

# psescaped = "she said \"Hello\""
# newline = "let us go 1\n new line"
# triple_quote = """This is my triple comment!"""

# print(psescaped)
# print(newline)
# print(triple_quote)

# text ="  Python Programming"

# print(len(text))
# print(text[0])
# print(text[-1])
# print(text[0:8])
# print(text[::2])

# print(text.upper())
# print(text.startswith("Python"))
# print("2344".isdigit())

# fruit =["Orange","Banana","Pineaple","Umuceri","Ubugari"]
# other_fruit = ["Onga","Sugar","Piripiri"]
# print(fruit)



# car_speed = int(input("Please Enter the car Speed : "))
# amount_of_money = 30

# if(car_speed < 60):
#     print("This car is in normal speed")
# if(car_speed>=60):
#     print("this car is on high speed")
#     print("You have to pay :", amount_of_money)
    

# even_squares = [x**2 for x in range(20) if x % 2 == 0]
# print(even_squares)

# tudent = {
# 'name': 'Alice Johnson',
# 'age': 20,
# 'grade': 'A',
# 'courses': ['Math', 'Physics', 'Chemistry']
# }
# # Using dict() constructor
# student2 = dict(name='Bob Smith', age=22, grade='B')

# print(student2)

# student = {'name': 'Alice', 'age': 20}
# # Adding/updating values
# student['grade'] = 'A' # Add new key-value
# student['age'] = 21 # Update existing value
# student.update({'phone': '123-456-7890', 'email': 'alice@email.com'})
# print(student)

# my_fruits = {'apple', 'banana', 'orange'}
# my_fruits.add('Mangoes')
# my_fruits.discard({0})
# my_fruits.update({"water","Enter"})
# my_fruits.clear()
# print(my_fruits)


# course = "Python Programming"
# number_of_course=len(course)
# print(number_of_course)
# print(course[0])
# print(course[-1])
# print(course[0:3])
# print(course[0:])
# print(course[:3])

# course = "Python \nProgramming"
# print(course)

# first = "Muheto"
# last = "Hodal"
# full = f"{len(first)} {last}"
# print(full)

course = "  Python Programming"

# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course.title())
# print(course.find("Pro"))
print(course.replace("P","j"))
print("Pro" in course)
count_number = 0
while True :
    text = input("Enter any text contain pro: ")
    if("pro" in text):
        print("Yeg Good")
        count_number = count_number + 1
    else:
        print("No try again")
    if(count_number == 2):
        break