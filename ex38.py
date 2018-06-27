ten_things = "Apples Oranges crows Telephone Light Sugar"

print("Wait there are not 10 things in that list.Let's fix")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Gitl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding:", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items nows.")
    
print("There w go:", stuff)

print("Let's go do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('***'.join(stuff[3:5]))
