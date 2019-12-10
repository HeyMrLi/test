import random

money = 100

#Write your game of chance functions here

def coin_flip(guess,bet):
  print("-" * 40)
  # Check bet
  if bet <= 0:
    print("You haven't bet anything")
    return 0
  elif bet > money:
    print("You don't have enough money")
    return 0

  # Start game
  print("Let's flip a coin! You guessed " + guess + ".")
  result = random.randint(1, 2)

  if result == 1:
    result = "Heads"
    print("Coin Lands Heads!")
  else:
    result = "Tails"
    print ("Coin Lands Tails!")

  if guess == result:
    print("You won your bet of $" + str(bet))
    return bet
  else:
    print("Sorry, you lost your bet of $" + str(bet))
    return -bet
  
def cho_han(guess,bet):
  print("-" * 40)
  # Check bet
  if bet <= 0:
    print("You haven't bet anything")
    return 0
  elif bet > money:
    print("You don't have enough money")
    return 0

  # Start game
  print("Let's play Cho-Han! You guessed " + guess + ".")
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  result = dice1 + dice2
  
  if result % 2 == 0:
    result = "Even"
    print(str(dice1) + " + " + str(dice2) + " = " + result)
  else:
    result = "Odd"
    print(str(dice1) + " + " + str(dice2) + " = " + result)

  if guess == result:
    print("You won your bet of $" + str(bet))
    return bet
  else:
    print("Sorry, you lost your bet of $" + str(bet))
    return -bet

def game_of_war(bet):
  print("-" * 40)
  # Check bet
  if bet <= 0:
    print("You haven't bet anything")
    return 0
  elif bet > money:
    print("You don't have enough money")
    return 0

  # Start game
  card1 = random.randint(1,10)
  print("Let's play war!")
  print("You draw " + str(card1) + ".")
  card2 = random.randint(1,10)
  print("Your opponent draws " + str(card2) + ".")
  
  if card1 > card2:
    print("You Win! Your " + str(card1) + " beats Their " + str(card2))
    print("You won $" + str(bet))
    return bet
  elif card1 == card2:
    print("It's a tie!")
    return 0
  else:
    print("You Lose! Their " + str(card2) + " beats Your " + str(card1))
    print("You lost your $" + str(bet))
    return -bet  

def roulette(guess,bet):
  print("-" * 40)
  # Check bet
  if bet <= 0:
    print("You haven't bet anything")
    return 0
  elif bet > money:
    print("You don't have enough money")
    return 0

  # Start game
  ball_lands = random.randint(0,37)
  print("Let's play Roulette!")

  # Win if number guess is equal to random Int 
  if guess == ball_lands and ball_lands != 37:
    print("You guessed " + str(guess) + " and the ball landed on " + str(ball_lands) + "!")
    print("You win $" + str(bet * 35) + "!")
    return bet * 35
  # Win if bet on "00"
  elif guess == "00" and ball_lands == 37:
    print("You guessed " + str(guess) + " and the ball landed on 00!")
    print("You win $" + str(bet * 35) + "!")
    return bet * 35
  # Win if bet Odds
  elif guess == "Odd" and ball_lands % 2 != 0 and ball_lands != 37 and ball_lands != 0:
    print("You guessed " + str(guess) + " and the ball landed on " + str(ball_lands) + "!")
    print(str(ball_lands) + " is an Odd number.")
    print("You win $" + str(bet) + "!")
    return bet
  # Win if bet Even
  elif guess == "Even" and ball_lands % 2 == 0 and ball_lands != 0 and ball_lands != 37:
    print("You guessed " + str(guess) + " and the ball landed on " + str(ball_lands) + "!")
    print(str(ball_lands) + " is an Even number.")
    print("You win $" + str(bet) + "!")
    return bet
  # Win if bet First Third
  elif guess == "First" and ball_lands / 3 <= 4 and ball_lands != 0 and ball_lands != 37:
    print("You guessed " + str(guess) + " and the ball landed on " + str(ball_lands) + "!")
    print(str(ball_lands) + " is in the First Third.")
    print("You win $" + str(bet * 2) + "!")
    return bet * 2
  # Win if bet Second Third
  elif guess == "Second" and ball_lands / 3 > 4 and ball_lands / 3 <= 8 and ball_lands != 0 and ball_lands != 37:
    print("You guessed " + str(guess) + " and the ball landed on " + str(ball_lands) + "!")
    print(str(ball_lands) + " is in the First Third.")
    print("You win $" + str(bet * 2) + "!")
    return bet * 2
  # Win if bet Third Third
  elif guess == "Third" and ball_lands / 3 > 8 and ball_lands != 0 and ball_lands != 37:
    print("You guessed " + str(guess) + " and the ball landed on " + str(ball_lands) + "!")
    print(str(ball_lands) + " is in the First Third.")
    print("You win $" + str(bet * 2) + "!")
    return bet * 2
  # Else you lose on "00"
  elif ball_lands == 37:
    print("You guessed " + str(guess) + " and the ball landed on 00!")
    print("You lost $" + str(bet) + ".")
    return -bet
  # Else you lose
  else:
    print("You guessed " + str(guess) + " and the ball landed on " + str(ball_lands) + "!")
    print("You lost $" + str(bet) + ".")
    return -bet
    
#Calling game of chance functions here
money += coin_flip("Heads",10)
money += cho_han("Even",10)
money += game_of_war(10)
money += roulette("First",10)
money += roulette("Second",10)
money += roulette("Third",10)
money += roulette("Even",25)
money += roulette("Odd",25)
money += roulette(15,5)
money += roulette(33,5)
money += roulette(2,5)
money += roulette(4,5)
money += roulette(12,5)
money += roulette("00",5)
money += roulette(0,5)
print("-" * 40)
print("Your ending total is $" + str(money))

