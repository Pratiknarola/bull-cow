import random
cows = 0
bulls = 0
megaloop = True
print("Welcome to Cow and Bull game!!!!")
while megaloop:
    cont1 = True
    cont = True
    guess = ''
    print("Choose difficulty: ")
    n = input("1. 1 digit guess\n2. 2 digit guess\n3. 3 digit guess\n4. 4 digit guess\n5. exit\n==> ")
    while cont:
        if n == '1':
            number = random.randint(0,9)
        elif n == '2':
            number = random.randint(10,99)
        elif n == '3':
            number = random.randint(100,999)
        elif n == '4':
            number = random.randint(1000,9999)
        elif n == '5':
            break
        else:
            print("incorrect input")
            break
        print("Computer has guessed " + n + " digit number")
        
        loop = True
        while loop:
            guess = input("Enter a number(exit to exit): ")
            if guess == 'exit':
                break
            elif int(number) == int(guess):
                print("Yes! You are correct")
                cows += 1
                print("You have", cows , "cows" + " and you have", bulls , "bulls")
                choice = input("do you want to continue with same difficulty? (Y/N)").lower()
                if choice == 'y':
                    loop = False
                    break
                elif choice == 'n':
                    cont1 = False
                    break
                else:
                    print("incorrect input")
                    continue
            else:
                print("Oops!! Incorrect guess. Try again!")
                bulls += 1
                print("You have", cows, "cows" + " and you have", bulls, "bulls")
        if guess == 'exit':
            break
        if cont1 == False:
            break
    if guess == 'exit' or n == '5':
        megaloop = False
    if cont1 == False:
        pass
print("Good bye!!!")
