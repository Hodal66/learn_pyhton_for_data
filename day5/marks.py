# define a function to calculate total and average of a list of numbers
# def get_stats(numbers):
#     total = sum(numbers)
#     average = total / len(numbers)
#     return total, average

# # Example usage of the function
# nums = [10, 20, 30]
# # Call the function to get total and average
# t, avg = get_stats(nums)
# print("Total:", t)
# print("Average:", avg)

# #create a function that will accept the list of marks and return the total and average
# def get_marks_from_user():
#     #Ask the user How many marks they want to enter 
#     num_marks = int(input("How many marks do you want to enter? "))
#     def get_number_of_marks(num_marks):
#         marks = []
#         for i in range(num_marks):
#             mark = int(input(f"Enter mark {i + 1}: "))
#             marks.append(mark)
#         return marks
#     marks = get_number_of_marks(num_marks)
#     sum_marks = sum(marks)
#     average_marks = sum_marks / num_marks if num_marks > 0 else 0
#     print("You have entered the following marks:")
#     print("-" * 30)  # Separator for each person
#     print("You have entered the following marks:", marks)
#     print("Total marks:", sum_marks)
#     print("Average marks:", average_marks)
    

# get_marks_from_user()

# def manage_student_courses():
#     # Create an empty dictionary to store student information
#     # student_info = {}   
#     # # Ask the user how many students they want to enter
#     # num_students = int(input("How many students do you want to enter? "))
    
#     example_of_courses = {
#         "Python Basics": ["Alice", "Bob"],
#         "Data Structures": ["Bob", "Charlie"],
#         "Machine Learning": ["Alice", "Charlie"]
#     }
#     return example_of_courses
# print(manage_student_courses())

def get_courses_and_marks():
    courses_info = {}
    num_courses = int(input("How many courses do you want to enter? "))
    for i in range(num_courses):
        course_name = input(f"Enter name for course {i+1}: ")
        num_students = int(input(f"How many students in {course_name}? "))
        student_marks = {}
        for j in range(num_students):
            student_name = input(f"Enter student {j+1} name: ")
            mark = float(input(f"Enter {student_name}'s mark for {course_name}: "))
            student_marks[student_name] = mark
        courses_info[course_name] = student_marks
    return courses_info

# Example usage:
courses_data = get_courses_and_marks()
print("Courses and marks entered:")
for course, students in courses_data.items():
    print(f"Course: {course}")
    for student, mark in students.items():
        print(f"  {student}: {mark}")