from sys import exit

def food_room():
    print("This is a room with a fullfil of many kinds of food with danger and safe food,So pick one kind of any food")
    choice=input("> ")
    if "barger" in choice:
        print("That barger will turn into a gosh and catch you")
    elif "cheesecake" in choice:
        print("That cake will turn into a monster and catch you")
    else:
        print("You can safely eat your food")

def witch_room():
    print("This room has a witch")
    print("In this room has clever broom that help people and bad black cat that catch people and give to his master-witch")
    print("try yourself to escape from this bad room")
    while True:
        choice=input("> ")
        if choice=="touchcleverbroom":
            escape()
        elif choice=="kickcat":
            print("Oh!you are really stupid.So you will panish ")
            angry()
        else:
            print("Oh!Poor person,you will be a servent forever for me")
            witch_room()


def escape(why):
    print(why,"You have Grate Good Job")
    exit(0)

def angry():
    print("You must be placed at monster room")
    print("There is 2 escape ways :steal king diamond room and place fire at cotton ")
    choice=input("> ")
    if choice=="steal" or choice=="fire":
        print("Con Con,you  are escape from this room")
    else:
        print("Sorry,monsters will fight you")


