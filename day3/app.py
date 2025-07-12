# app.py
import utils # another_script.py
import day3  # This will NOT run main() from day3.py
import basic_calculator  # Importing the basic calculator module

day3.check_age("Alice", 20)  # You can use functions from day3.py
print(utils.add(100, 300))# Uses add function, does NOT print 5 from utils.py

if __name__ == "__main__":
    print("Hello! you have called Basic Calculator")  # This will run when app.py is executed directly
    print("Running the basic calculator...")
    check_user_preference = input("Do you want to use the basic calculator? (yes/no): ").strip().lower()
    if check_user_preference == 'yes':
        print("Starting the basic calculator...")
        basic_calculator.main()  # Run the main function of the basic calculator
    else:
        print("Exiting the basic calculator. Goodbye!")