from random import randint
from time import sleep

print("Gosht game!")
feelingbrave = True
score = 0
while feelingbrave:
    ghostdoor = randint(1, 3)
    print("Tree doors are ahead...")
    sleep(1)
    print("One has a ghost in it!!")
    sleep(1)
    print("You have to open one, witch one?")
    door = input('1, 2, or 3?')
    doornum = int(door)
    if doornum == ghostdoor:
        print("GOSHT!!!")
        feelingbrave = False
    else:
        print("No Ghost")
        sleep(0.5)
        print("Go to next level!")
        score = score + 1
print("You ran away!")
sleep(1)
print("Game over! you scored", score, "!")