from sys import exit


def food_room():
    print("This is a room with a fil of many kinds of food with danger and safe food,So pick one kind of any food")
    choice = input("> ")
    if "burger" in choice:
        print("That burger will turn into a gosh and catch you")
    elif "cheesecake" in choice:
        print("That cake will turn into a monster and catch you")
    else:
        print("You can safely eat your food")


def witch_room():
    print("This room has a witch")
    print("This room has clever broom,help people and bad black cat that catch people and give to his master-witch")

    print("try yourself to escape from this bad room")
    while True:
        choice = input("> ")
        if choice == "broom":
            escape()
        elif choice == "cat":
            print("Oh!you are really stupid.So you will panish ")
            angry()
        else:
            print("Oh!Poor person,you will be a servent forever for me")
            witch_room()


def escape(why):
    print(why, "You have Grate Good Job")
    exit(0)


def angry():
    print("You must be placed at monster room")
    print("There is 2 escape ways :steal king diamond room and place fire at cotton ")
    choice = input("> ")
    if choice == "steal" or choice == "fire":
        print("Con Con,you  are escape from this room")
    else:
        print("Sorry,monsters will fight you")
    exit(0)
def start():
    print("Oh! you enter in a magic room.")
    print("There is two rooms in your left and right.")
    choice = input("> ")
    if choice == "left":
        food_room()
    elif choice == "right":
        witch_room()
    else:
        print("Please choice for your escape.")

start()