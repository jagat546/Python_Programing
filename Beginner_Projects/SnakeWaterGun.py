#A simple game made in python language
import random

def gameWin(comp, you):
    # Possibility that the game will be tie 
    if comp == you:
        return None
    # all possibilities when computer chooses the Snake
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True 
    # all possibilities when computer chooses the Water
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True 
    # all possibilities when computer chooses the Gun
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True 


print("Comp turn: Snake(s, 1) Water(w, 2) or Gun(g, 3)?")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Your Turn: Snake(s, 1) Water(w, 2) or Gun(g, 3)?")
a = gameWin(comp, you)

print(f"Computer Choose {comp}")
print(f"You Choose {you}")

if a == None:
    print("The Game is a Tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")
