import random
import time
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""






#Pick a card
def pick_a_card(card_list):
  pickCard=random.choice(cards)
  card_list.append(pickCard)

def getScore(card_list):
  score=sum(card_list)
  if(sum(card_list)>21 and 11 in card_list):
    for card in card_list:
      if(card==11 and sum(card_list)>21):
        score-=10
  elif(sum(card_list)==21 and len(card_list)==2):
    score=0
    
  return score


def game():
  #Deal hands
  user_cards=[]
  dealer_cards=[]
  for i in range(2):
    pick_a_card(user_cards)
    pick_a_card(dealer_cards)
  
  print("Your cards:")
  print(user_cards)
  print(f"Dealer's first card: {dealer_cards[0]}")
  
  gameOver=False
  #Check for winners
  if(getScore(dealer_cards)==0):
    print("Dealer's cards:")
    print(dealer_cards)
    gameOver=True
  elif(getScore(user_cards)==0):
    gameOver=True
  
  
  #Let user draw cards
  if not gameOver:
    continue_blackjack=True
    while(continue_blackjack and not gameOver):
      if input("Do you want to draw another card? 'y' for yes: ")=="y":
        pick_a_card(user_cards)
        print("Your cards:")
        print(user_cards)
        print(getScore(user_cards))
        if(getScore(user_cards)==0):
          gameOver=True
        elif(getScore(user_cards)>21):
          gameOver=True
      else:
        continue_blackjack=False
  
  #Dealer draws cards until his score is greater than user
  if not gameOver:
    while(getScore(dealer_cards)<=getScore(user_cards)) and getScore(dealer_cards)<21:
      pick_a_card(dealer_cards)
      print("Dealers cards:")
      print(dealer_cards)
      time.sleep(0.5)
      

  print(f"Your final hand: {user_cards}, score={getScore(user_cards)}")
  print(f"Dealer's final hand: {dealer_cards}, score={getScore(dealer_cards)}")
    
  if(getScore(dealer_cards)==0):
    print("Dealer has a blackjack, he wins.")
  elif(getScore(user_cards)==0):
    print("You have a blackjack, you win.")
  elif(getScore(dealer_cards)>21):
    print("Dealer score above 21, You win.")
  elif(getScore(user_cards)>21):
    print("Your score is above 21, You lose.")
  elif(getScore(dealer_cards)==getScore(user_cards)):
    print("Same score, It's a draw.")
  elif(getScore(dealer_cards)>getScore(user_cards)):
    print("Dealer score greater than yours, You lose.")
  else:
    print("Your score greater than dealer's, You win.")
    

print(logo)
while(input("Play a game of blackjack? 'y' for yes: ")=='y'):
  game()

print("Thank you for playing.")
