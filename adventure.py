name=input("Type your name : ")
print("WELCOME ",name,"to this adventure!")
answer=input("You are on a dirt road, it has come to an end and you can go left or right which way would you like to go?").lower()
if answer=="left":
    answer=input("You come to a river, you can walk around it or swim across? type walk to walk around and swim if you to swimacross?")
    if answer=="swim":
        print("You can swam across the river and were eaten by an alligator")
    elif answer=="walk":
        print("You walked miles, ran out of water and lost the game.")
    else:
        print("Not a valid option. You lose!!")
elif answer=="right":
    answer=input("You came across a bridge, it lokks wobbly, do you want to cross it or head back (cross/back) ?" )
    if answer=="back":
        print("You go back and lose.")
    elif answer=="cross":
        answer=input("You cross the bridge and met a stranger. Do you want to talk to him (yes / no)")
        if answer=="yes":
            print("you talk to the stranger and they gift you the treasure. You WON!!!!")
        elif answer=="no":
            print("You ignore the stranger and they got offended and you lose.")
        else:
            print("invalid option You lose.")
    else:
        print("invalid option you lose.")
else:
    print("Invalid option buy you LOSE^^^")
print("thank you for trying ",name)