import random
print("Welcome to Guess the no. game!!!")
print("Rules:")
print("1. There will be 3 levels of difficulty")
print("2. Level 1: You will get 2 Chances to guess the correct number between 1 and 5")
print("3. Level 2: You will get 3 Chances to guess the correct number between 1 and 10")
print("4. Level 3: You will get 5 Chances to guess the correct number between 1 nad 20")
def level_1():
    num = random.randint(1,5)
    print("Welcome to Level 1")
    print("Here you will get 2 chances")
    for i in range(2):
        guess = int(input("Guess the number: "))
        if guess == num:
            print("Computer chose: ", num)
            print("You chose: ", guess)
            print("You Won!!!")
            break
        else:
            
            print("Better Luck Next Time!!!")
            if i==1:
                print("Computer chose: ", num)

def level_2():
    num2 = random.randint(1,10)
    print("Welcome to Level 2")
    print("Here you will get 3 chances")
    for i in range(3):
        guess = int(input("Guess the number: "))
        if guess == num2:
            print("Computer chose: ", num2)
            print("You chose: ", guess)
            print("You Won!!!")
            break
        else:
            
            print("Better Luck Next Time!!!")
            if i==2:
                print("Computer chose: ", num2)

def level_3():
    num3 = random.randint(1,20)
    print("Welcome to Level 3")
    print("Here you will get 5 chances")
    for i in range(5):
        guess = int(input("Guess the number: "))
        if guess == num3:
            print("Computer chose: ", num3)
            print("You chose: ", guess)
            print("You Won!!!")
            break
        else:
            
            print("Better Luck Next Time!!!")
            if i==4:
                print("Computer chose: ", num3)

print()
print()
print()

while True:
    print("1. Start Level 1")
    print("2. Start Level 2")
    print("3. Start Level 3")
    print("4. Leave the Game")
    print()
    print()
    choice = int(input("Enter your choice[1/2/3]: "))
    if choice==1:
        level_1()
    elif choice==2:
        level_2()
    elif choice==3:
        level_3()
    elif choice==4:
        print("Game Over......")
        break
    else:
        ask = int(input("GO TO MAIN MENU?[y/n]: "))
        if ask.lower()=="y":
            continue
        else:
            break




