number1=300
number2=300
sum=number1+number2

print(sum)

print("hello again")
#this is the comment in Python

fullName='Muheto Hodal'
email ="mhthodol@gmail.com"
phone_number= 782439775
is_boy = True
price = 9.67


print('Your name is ', fullName, ' Your Email is ', email, ' your Phone number is ', phone_number)


#Function Declaration

def greet_and_check_age(name,age):
    if name == "Eric" :
        print("Hello, Eric")
        
    if age >= 18 :
        print("you are an adult.")
    else:
        print("you are a Minor")
        
greet_and_check_age("Hodal", 36)

#How concantanatio works

first_name = "Muheto"
last_name = "Hodal"
full_name = first_name + " " + last_name

print(full_name)

first_number = 12
last_number = 12
# sum_of_two_numbers = first_number + " " + last_number # This should result an error
sum_of_two_numbers = first_number + last_number 

print(sum_of_two_numbers) 

#Another concantenation is 

message = "This is "
message +="my message that "
message +="\n from the heaven"

print(message)

#Using f-String

name ="today class"
greeting = f"Hello", name
print(greeting)

#Let us dive into List

words = ["Data", "Science","Is", "fun"]

sentence = " ".join(words)

print(sentence)

student_info ={ "name": "Eric","age":30}

print(student_info)

print("Student Name is : ",student_info["name"])

name = "Hoodal"
age = 30

info = "My name is {} and I am {} years old.".format(name,age)
print(info)

#Condition 

# user_name = input("Enter your name: ")
# user_age = int(input("Enter your age: "))

# greet_and_check_age(user_name,user_age)

def greet_user(name):
    "You are welcome ", print("you are welcome ",name)
    
    print("Muheto Hodal")
    
greet_user("Keza")


#Store Function in a variable

def add_number(a,b):
    """Function to add Two Number"""
    return a + b
my_sum = add_number(40,80)
print(my_sum)

#Loops


    