print("welcome to Python day 3")
#LET US CREATE A FUNCTION THAT will ask the user names and ages and check if she is an adult and a minor


def check_age(name, age):
    """Check if the person is an adult or a minor based on age."""
    if name == "" or age < 0:
        print("Invalid input. Please enter a valid name and age.")
        return
    if age >= 18:
        print(f"{name} is an adult.")
    else:
        print(f"{name} is a minor.")

def main():
    """Main function to execute the age check."""
    while True:
        full_name = input("Enter your Full Names : ")
        input_ages = int(input("Enter your age: "))
        try:
            input_ages = int(input_ages)
        except ValueError:
            print("Please enter a valid number for age.")
            continue
        if full_name == "" or input_ages <= 0:
            print("Invalid input. Please enter a valid name and age.")
            continue
        check_age(full_name, input_ages)
        break
    
        
if __name__ == "__main__":
    main()