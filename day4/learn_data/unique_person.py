import random

print("Welcome to Learn Data with python!")

names = [
    "Muheto Hodal", "Alice Smith", "John Doe", "Jane Miller", "Robert Brown",
    "Emily Davis", "Michael Wilson", "Sarah Johnson", "David Lee", "Linda Clark",
    "James Lewis", "Patricia Walker", "Christopher Hall", "Barbara Allen", "Matthew Young",
    "Elizabeth King", "Joshua Wright", "Susan Scott", "Daniel Green", "Karen Adams",
    "Anthony Baker", "Nancy Nelson", "Mark Carter", "Lisa Mitchell", "Paul Perez",
    "Sandra Roberts", "Steven Turner", "Donna Phillips", "Andrew Campbell", "Carol Parker"
]

cities = [
    "Harare", "Bulawayo", "Gweru", "Mutare", "Kwekwe", "Chinhoyi", "Masvingo", "Victoria Falls",
    "Kadoma", "Bindura", "Marondera", "Chegutu", "Zvishavane", "Rusape", "Redcliff",
    "Kariba", "Hwange", "Chiredzi", "Beitbridge", "Shurugwi", "Chipinge", "Norton",
    "Karoi", "Chivhu", "Mvurwi", "Gokwe", "Epworth", "Banket", "Lupane", "Plumtree"
]

skills_list = [
    ["Python", "Data Analysis", "Machine Learning"],
    ["Java", "Web Development", "SQL"],
    ["C++", "Algorithms", "Statistics"],
    ["JavaScript", "React", "CSS"],
    ["R", "Data Visualization", "Excel"],
    ["PHP", "Laravel", "HTML"],
    ["Go", "Microservices", "Docker"],
    ["Swift", "iOS Development", "UI Design"],
    ["Kotlin", "Android", "APIs"],
    ["Ruby", "Rails", "Testing"]
]

courses_list = [
    ["Python Basics", "Data Science", "Machine Learning"],
    ["Web Development", "JavaScript", "React"],
    ["Algorithms", "C++", "Statistics"],
    ["Data Visualization", "R", "Excel"],
    ["Mobile Apps", "Swift", "UI Design"],
    ["Microservices", "Go", "Docker"],
    ["Android Apps", "Kotlin", "APIs"],
    ["Backend", "PHP", "Laravel"],
    ["Frontend", "HTML", "CSS"],
    ["Testing", "Ruby", "Rails"]
]

person_data = []

for i in range(30):
    name = names[i]
    city = cities[i]
    skills = random.choice(skills_list)
    courses = random.choice(courses_list)
    age = random.randint(20, 40)
    is_student = random.choice([True, False])
    graduation_year = random.randint(2018, 2025)
    email = f"{name.lower().replace(' ', '.')}{i+1}@gmail.com"
    person = {
        "id": i + 1,
        "full_name": name,
        "age": age,
        "city": city,
        "skills": skills,
        "is_student": is_student,
        "courses": courses,
        "graduation_year": graduation_year,
        "email": email
    }
    person_data.append(person)

print("Person Data:")
for person in person_data:
    print("-" * 30)  # Separator for each person
    for key, value in person.items():
        print(f"{key}: {value}")

print("You have done!! conglatulations!!")