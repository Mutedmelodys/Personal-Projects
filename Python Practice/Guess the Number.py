import random



print("Hello traveler! what is your name?  ")

MyName = input()


guesses = 0

number = random.randint (1, 20)

while guesses < 10:
    print(MyName + " I'm thinking of a number between 1 and 20")
    print("Take a guess and see how it goes")
    guess = input()
    guess = int(guess)

    guesses = guesses + 1

    if guess < number:
        print("Well you're a wee bit low")


    if guess > number:
        print("Stop! you're a lil bit too high")

    if guess == number:
        print("Well fuck.... you got it right")
        break

if guess == number:
    print("Congrats! you aren't such a big idiot after all")

if guess != number:
    print("You messed up, the number was actually " + number)

    

        
    
