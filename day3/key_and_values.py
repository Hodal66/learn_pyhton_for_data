student_information ={
    "full_name":"Muheto Hodal",
    "ages":30,
    "isPayed":False,
    "current_salary":200.40
}
# print("The current student information you have are :", student_information)

# #This an other way to display more information using loop
# for key, value in student_information.items():
#     print(f"{key}: {value}")

# # Update the value of "ages"
# student_information["ages"] = 31  # Update value
# print("Updated student information:", student_information)

# # Add a new key-value pair
# student_information["is_graduated"] = True  # Add new key-value pair
# print("After adding new key-value pair:", student_information)

# # Delete a key-value pair
# del student_information["isPayed"]  # Delete key-value pair
# print("After deleting 'isPayed':", student_information)

# print("Full Name :", student_information.get("full_name"))
# student_information['name'] = student_information['fullname']
print("New database keys and valus are : ", student_information)
if "fullname" in student_information:
    print("Full Name key Available in the database")
else:
    print(f"Full Name is not availabe, the available key is Name : {student_information['full_name']}")

basic_info = "Your Name is {} and your ages is {} ".format(student_information["full_name"], student_information["ages"])
print(basic_info)

def add_two_number(x,y):
    print(f'the firs Number is {x} and the second number is {y}')
    return x + y
addition = add_two_number(int(input("Enter First Number : ")), int(input("Enter Second Number : "))) 
print("The sum of those number is : {} ".format(addition))