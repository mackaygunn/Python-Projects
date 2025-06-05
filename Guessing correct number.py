import random

def guess_number():

    i = random.randint(1,10)
    attempts = 3
    x = None

    while attempts > 0 and x != i:
 
        x = int(input("enter a number between 1 and 10: "))
  
        if i - 1 == x or i - 2 == x:
            print("little low, try again")
        elif x < i - 2:
            print("too low, try again")
        elif i + 1 == x or i + 2 == x:
            print("little high, try again")

        elif x > i + 2:
            print("too high")
        elif i == x:
            print("You won")
        
        attempts -= 1

        if attempts == 0 and x != i:
            print(f"Out of attempts, answer is {i}. Thank you for participating")

guess_number()


















