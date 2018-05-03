class player():
    def player_inventory():
        print("This is what is in your inventory")
        print("A small dagger")
    def player_hand():
        print("This is what is in your hand")

    def player_health():
        life = int(100)
        if life <= 0:
            print("You have died")
            exit()


def goblin():
    goblife = int(50)
    if goblife <= int(50):
        print("The goblin died")


def dagger_att(name):
    health = int(100)
    goblife = int(50)
    s = 0
    while s <= 1:
        s = s + 1
        dagger_att.value = int(30)
        battle = input(name + " do you want to fight? Y/N ")
        if battle == "Y":
            print("the monster shanks you")
            health = (int(health) - 10)
            print ("Your health is now " + str(health))
            option = input("attack the goblin back? Y/N ")
            if option == "Y":
                print("you stab the goblin back")
                goblife = (int(goblife) - int(30))
                goblin()
                Travel(name)
        
                
            
        else:
            print("You ran away")
            exit()


      
def fight():
    choice = input("Would you like to see what is in your inventory? Y/N ")
    if choice == ("Y"):
        print(player.player_inventory())
    else:
        print("Ok, you're about to get into a fight")
    dagger_att(name)
    print("testing this code")
    
def Travel(name):
    print("You're doing well on your journey! Your first fight went very well " + name + "!")
    exit()

    
name = input("What is your name ")       
fight()


    
