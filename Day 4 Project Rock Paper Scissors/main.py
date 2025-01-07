rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

rockpaperscisors=[rock,paper,scissors]

player1=int(input("What do you choose? 0 for rock, 1 for paper, 2 for scissors\n"))


if(player1>=3 or player1<0):
  print("Invalid number, you lose")
else:
  print(rockpaperscisors[player1])

  player2=random.randint(0,2)
  print(rockpaperscisors[player2])
  if(player1==0 and player2==2):
    print("You win")
  elif(player1==2 and player2==0):
    print("You lose")
  elif(player1>player2):
    print("You win")
  elif(player2>player1):
    print("You lose")
  elif(player1==player2):
    print("Draw")
  

