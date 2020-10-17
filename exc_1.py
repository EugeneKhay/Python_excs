import random

available_attempts = 3
num = random.randint(0, 100)
attempts = available_attempts

def user_input():
    res = 0
    try:
        inp = int(input("Enter the number: "))
        res = inp
    except ValueError:
        print("Your input is wrong!")
        res = user_input()
    return res

def play_again():
    again = input("Play again (Y/N)?: ")
    if again == "N":
        return False
    elif again == "Y":
        global attempts   # needed to use global var, not local one
        attempts = available_attempts
        return True
    else:
        print("Unknown command")
        return play_again()
    
while True:
    if attempts <= 0:
        print("Too many attempts, you lose!")
        if not play_again():
            break
    s = user_input()
    attempts -= 1
    if s == num:
        print(f"Your number {s} is correct!")
        if not play_again():
            break   
    if s > num:
        print(f"Your number {s} is too big!")
    if s < num:
        print(f"Your number {s} is too low!")