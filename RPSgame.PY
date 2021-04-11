import random
game=["rock","paper","scissor"]
p1,p2,i=0,0,1
pr1=input("enter name of player 1: ")
pr2=input("enter name of player 2: ")
n=int(input("total no. of points to decide winner(5,10) = "))
while p1<n and p2<n :
  n1=random.randint(0,2)
  random.shuffle(game)
  n2=random.randint(0,2)  
  if (game[n1]=="rock" and game[n2]=="paper"):
    print(f"player 1 outcome is { game[n1]} and player 2 outcome  is {game[n2]} \n            round {i} winner is {pr2}" )
    p2+=1
  elif (game[n1]=="rock" and game[n2]=="scissor"):
    print(f"player 1 outcome is { game[n1]} and player 2 outcome is {game[n2]} \n            round {i} winner is {pr1}" )
    p1+=1
  elif (game[n1]=="paper" and game[n2]=="scissor"):
    print(f"player 1 outcome is { game[n1]} and player 2 outcome is {game[n2]} \n            round {i} winner is {pr2}" )
    p2+=1   
  elif (game[n1]=="paper" and game[n2]=="rock"):
    print(f"player 1 outcome is { game[n1]} and player 2 outcome is {game[n2]} \n            round {i} winner is {pr1}" ) 
    p1+=1 
  elif (game[n1]=="scissor" and game[n2]=="rock"):
    print(f"player 1 outcome is { game[n1]} and player 2 outcome is {game[n2]} \n            round {i} winner is {pr2}" ) 
    p2+=1
  elif (game[n1]=="scissor" and game[n2]=="paper"):
    print(f"player 1 outcome is { game[n1]} and player 2 outcome is {game[n2]} \n            round {i} winner is {pr1}" )
    p1+=1    
  else: print(f"\n       round {i} winner is no one(DRAW)\n") 

  i+=1 

if p1>p2:
  print(f"\n*********************FINAL WINNER IS {pr1.upper()} *************************")  
else:
  print(f"\n*********************FINAL WINNER IS {pr2.upper()} *************************")
