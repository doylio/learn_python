import random

def menu():
    #Get user numbers
    user_numbers = get_player_numbers()
    #Get lottery numbers
    lottery_numbers = create_lottery_numbers()
    #Check matches
    matches = user_numbers.intersection(lottery_numbers)
    #Print winnings
    print("You matched {num}.  You won ${money}!!".format(money=100**len(matches), num=matches))

#User picks 6 numbers
def get_player_numbers():
    numbers_csv = input("Enter your 6 numbers, separated by commas:  ")
    number_list = numbers_csv.split(",")
    user_numbers = {int(num) for num in number_list}
    return user_numbers


#Lottery calculates 6 random numbers (between 1 and 20)
def create_lottery_numbers():
    values = set()
    while len(values) < 6:
        values.add(random.randint(0,20))
    return values

menu()
