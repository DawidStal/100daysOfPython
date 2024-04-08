import random
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
lives=0
if input("Choose a difficulty 'easy' or 'hard': ")=="hard":
  lives=5
else:
  lives=10
number=random.randint(1,100)
guess=-1
while(guess!=number and lives>0):
  print(f"You have {lives} attempts remaining to guess the nubmer.")
  guess=int(input("Make a guess: "))
  if(guess>number):
    print("Too high")
    lives-=1
  elif(guess<number):
    print("Too low")
    lives-=1
  if(guess!=number and lives>0):
    print("Guess again")

if(guess==number):
  print(f"You got it! the answer was {number}.")
elif(lives==0):
  print("You've run out of lives you lose.")
