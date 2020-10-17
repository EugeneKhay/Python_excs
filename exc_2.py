# returns a list with user's inputs
def get_input():  
    res = ()
    try:
        str = input("Enter numbers: ('exit for quit'): ")
        if str == 'exit':
            return
        res = list(map(int, str.split()))
    except ValueError:
        print("Wrong input, try again")
        res = get_input()
    return res

# calculate the sum of the list
def calculate(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

while True:
    user_input = get_input()
    if not user_input:   # if list is empty
        break
    print(calculate(user_input))







