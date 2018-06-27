import random

magic_numbers = [random.randint(0,9), random.randint(0,9)]

def ask_user_and_check_number():
    user_number = int(input("Enter a number between 0 and 9:  "))
    if user_number in magic_numbers:
        return "You're right!"
    if user_number not in magic_numbers:
        return "WRONG!"

def run_program_x_times(chances):
    for attempt in range(chances):
        print (ask_user_and_check_number())
        print("You have {n} attempts remaining.".format(n = chances - attempt - 1))
    

tries = int(input("How many tries do you want? "))

run_program_x_times(tries)


    
