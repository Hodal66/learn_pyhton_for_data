print("Welcome to Learn Data with python!")
person_data=[
    {
        "id": 1,
        "full_name":"Muheto Hodal",
        "age": 25,
        "city": "Harare",
        "skills": ["Python", "Data Analysis", "Machine Learning"],
        "is_student": True,
        "courses": ["Python Basics", "Data Science", "Machine Learning"],
        "graduation_year": 2023,
        "email": "muheto.hodal@gmail.com"
    },
    {
        "id": 2,
        "full_name":"Muheto Hodal",
        "age": 25,
        "city": "Harare",
        "skills": ["Python", "Data Analysis", "Machine Learning"],
        "is_student": True,
        "courses": ["Python Basics", "Data Science", "Machine Learning"],
        "graduation_year": 2023,
        "email": "muheto.hodal@gmail.com"
    },
    {
        "id": 3,
        "full_name":"Muheto Hodal",
        "age": 25,
        "city": "Harare",
        "skills": ["Python", "Data Analysis", "Machine Learning"],
        "is_student": True,
        "courses": ["Python Basics", "Data Science", "Machine Learning"],
        "graduation_year": 2023,
        "email": "muheto.hodal@gmail.com"
    }
]


print("Person Data:")
for person in person_data:
    print("-" * 30)  # Separator for each person
    for key, value in person.items():
        print(f"{key}: {value}")


