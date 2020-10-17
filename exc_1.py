import random

num = random.randint(0, 100)
attempts = 10

def user_input():
    res = 0
    try:
        inp = int(input("Enter the number: "))
        res = inp
    except ValueError:
        print("Your input is wrong!")
        res = user_input()
    return res
    
while True:
    if attempts == 0:
        print("Too many attempts, you lose!")
    s = user_input()
    attempts -= 1
    if s == num:
        print(f"Your number {s} is correct!")
        break
    if s > num:
        print(f"Your number {s} is too big!")
    if s < num:
        print(f"Your number {s} is too low!")