import time

#options
opt_A = ["A".lower()]
opt_B = ["B".lower()]
opt_C = ["C".lower()]
yes = ["Y".lower()]
nope = ["N".lower()]

#option_enjoy = "stand by and enjoy the show"

#Objects
sword = 0
unknown= 0

required = ("\n Use only A, B, C or Y and N\n")#Only these options are allowed

name = input("State your name, O Great Adventurer: ")
print("Welcome", name, "to this new Adventure!")


#The Tale Of A Great Adventurer
def intro():
    print("Okay, so", name,", you just left the supermarket with your some groceries and you see a child crossing the road "
        "\nwithout looking to grab his ball. A white truck with failed breaks approaches as he tries\n to go for the ball."
        " Upon seeing this You: ")
    time.sleep(3)
    print("A. stand by and enjoy the show\nB. rush to push the kid from the truck\'s way\nC. try to get the driver\'s attention to stop.")
    
    choice = input(">>>")
    if choice in opt_A:
        print("Wow you are such a maniac. Kid is surely gonna hunt you forever.")
        input("")
    elif choice in opt_B:
        option_rush()
    elif choice in opt_C:
        print("\nThe Driver sees the kid but he was too late and the sad part is, you died along the kid as the truck explods. RIP",name)    
        input("")
    else:
        print(required)
        intro()


def option_rush():
    print("\nWell you saved the kid but,",name,"Welcome Aincard, a world of numereous races and Yes! magic as well."
        "\nAnd YES, you died but got reincarnated into a land of fantasy. You wake up and see you are beside a river,"
        "\nyou turn to the other side and surprisingly, you see a girl infront of you with Bunny Ears."
        "\nWhat will you do?: " )
    time.sleep(3)
    print("A. Jump into the river.\nB. Eliminate the Bunny Girl out of fear. ")

    choice = input(">>>")
    if choice in opt_A:
        option_save()
    elif choice in opt_B:
        print("It seems you love to die. A magic circle is drawn around you and drags you down to the earth\'s core. You died!!")
        input("")
    else:
        print(required)
        intro()


def option_save():
    print("\nWhat were you thinking, you are the most terrible swimmer ever to exist and you decided" 
        "\nto jump into the river.. Luckily for you the Bunny Girl is still around so she hops into the" 
        "river and saves you.\nWhat are you gonna do now that you are concious again. You rise up and see an Ogre coming your direction,"
        "\nWhat will be your next action?: ")
    time.sleep(3)
    print("A. Run..\nB.Thank her for saving your life and listen to what she has to say.\nC. Run towards a nearby cave. ")

    choice = input(">>>")
    if choice in opt_A:
        option_run()
    elif choice in opt_B:
        print("The Bunny Girl tells you her name, which is Freia. You also tell her your name"
            "\nand she says'Well,'",name,' welcome to our world of Aincard. Come on let me show you around.'
            "\nAnd by around she meant her BELLY.These creatures are so sincere they will let  you know they are gonna devour you.\nAnd that is what happened.\nThe End!!")
        input("")
    elif choice in opt_C:
        option_cave()
    else:
        print(required)
        option_save()


def option_cave():
    print("\nYou were hesitant, since the cave was dark. Before you fully enter, you noticed a shinny sword on at entrance."
    "\nDo you pick it up? Y/N")
    choice = input(">>>")
    if choice in yes:
        sword = 1  #acquired the item; sword
    else:
        sword = 0
    print("\nWhat do you do next?: ")
    time.sleep(3)
    print("A. Stay hidden in silence..\nB. Fight..\nC. Run")

    choice = input(">>>")
    if choice in opt_A:
        print("Sriously, you are going to stay hidden from a creature that has night vision"
        "\nwell done. As usual your grave awaits.""\nYou died...")
        input("")
    elif choice in opt_B:
        if sword > 0:
            print("\nYou laid in wait. The shinning sword attracts the Ogre, which upon seeing thought"
            "\nyou are no match for it. As it walked closer and closer, you heart beats rapidly. As the Ogre"
            "\nreaches out to grab the sword you rush and push the sword through it\'s chest.\nYou Survived...")
            input("")
        else:
            print("Seriously, you should have picked up the sword. You just lost your only defense.\nYou died..")
            input("")
    elif choice in opt_C:
        print("As the Ogre enters the dark cave, You quietly sneak out. You are several feets away,"
        "\nthe Ogre turns around sees you running")
        option_run()
    else:
        print(required)
        option_cave()


def option_run():
    print("\nYou run as fast as you can, but the Ogre\'s speed is far greater than yours.\nSo now you will: ")
    time.sleep(3)
    print("A. Hide behind a boulder.\nB. Fight back..\nC. Run toward the nearby town..")

    choice = input(">>>")
    if choice in opt_A:
        print("Oops, it spots you.\nYou died...")
    elif choice in opt_B:
        print("Wow you are indeed brave but not this time.\nYou died...")
        input("")
    elif choice in opt_C:
        option_town()
    else:
        print(required)
        option_run()


def option_town():
    print("\nWhile wildly running, you noticed a a huge club in mud. You quickly reach down to grab it,but missed. You tried to"
    "\ncalm your breathing as you hide in the town without even noticing it was abandoned. Waiting for your pursuer who was charging"
    "\naround the corner, you noticed an unknown artifact before you."
    "\nDo you pick it or leave it be? Y/N")
    choice = input(">>>")
    if choice in yes:
        unknown = 1
    else:
        unknown = 0
    print("You hear the heavy footsteps of the Ogre approaching as it gets closer.")  
    time.sleep(3)
    if unknown > 0:
        print("\nYou hold out the artifact, hoping it will perform some sort of magic.What do you know, the Ogre stopped at once."
        "\nIt seems to have seen something familiar and reaches out for it. The artifact seem to be a lost treasure of it\'s people."
        "\nThe Ogre is pleased and thanks you."
        "\nYou Survived...")
        input("")
    else:
        print("I think you should picked the artifact.\n You died...")
        input("")
intro()        

    


        



