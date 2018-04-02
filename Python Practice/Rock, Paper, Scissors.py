import random

Opponent = random.choice (['Rock', 'Paper', 'Scissors'])

print("What is your name?")
MyName = input()
print("Let's play rock, paper, scissors " + MyName + "!")
print("Rock = 1")
print("Paper = 2")
print("Scissors = 3")


"Rock" = 1
"Paper" = 2
"Scissors" = 3

Score = 0
Myscore = 0

while Score <3 and Myscore <3:
    print("Now input your guess ")
    guess = input()
    
    "Rock" = 1
    "Paper" = 2
    "Scissors" = 3

    if guess == 1:
        if Opponent == "rock":
        Myscore = Myscore + 1
            print("You... tied")
            print(Myscore, Score)

        elif Opponent == Paper:
        Score = Score + 1
            print("You lost!")
            print(Myscore, Score)

    elif guess == 2:
        if Opponent == Paper:
        Myscore = Myscore + 1
            print("You tied on some paper")
            print(Myscore, Score)
            
        elif Opponent == Scissors:
        Score = Score + 1
            print("Yah lost, now go fight some pirates")
            print(Myscore, Score)
    

    elif guess == 3:
        if Opponent == Scissors:
        Myscore = Myscore + 1
            print("You need to stop scissoring.. you tied")
            print(Myscore, Score)

        elif Opponent == Rock:
        Score = Score + 1
            print("Someone lost, and it wasn't the robot")
            print(Myscore, Score)
            
         

print("Thanks for playing!")
print(Myscore, Score)
    
    
    
      



