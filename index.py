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