from random import randint

intro = "to quit press k"
print(intro)

while True: # game will not stop until k is inputted
  player = input("rock (r), paper (p), scissors (s): ")

  if player not in ("r", "s", "p", "k"): # invalid input
    print("pls enter correctly")
  elif player == "k": # input to stop game
    print("play stopped")
    break # ends game
  else:
    options = ["r", "p", "s"] # r = rock, p = paper, s = scissors
    comp = options[randint(0, 2)]
  
    print(player, "vs", comp)
  
  # display results
  if (player == "r" and comp == "r") or (player == "p" and comp == "p") or (player == "s" and comp == "s"):
    print("Draw")
  elif (player == "r" and comp == "p") or (player == "s" and comp == "r") or (player == "p" and comp == "s"):
    print("Lose")
  elif (player == "p" and comp == "r") or (player == "r" and comp == "s") or (player == "s" and comp == "p"):
    print("Win")

