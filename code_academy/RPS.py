"""
This a project for codeacademy pro's python track.

This program
1. Prompt's the user to select either rock, paper, or scissors.
2. Instructs the computer to randomly select Rock, Paper, or Scissors.
3. Computers the user's choice to the computer's.
4. Determine a winner.
5. Inform the user who the winner is.
"""
from random import randint
from time import sleep

options = ["R", "P", "S"]
LOSS_RESULT = "You lost, nerd."
WIN_RESULT = "You are... the winner!"

def decide_winner(user_choice, computer_choice):
  print "Your choice is %s." % (user_choice)
  print "Computer selecting..."
  sleep(1)
  print "The computer chose %s." % (computer_choice)
  user_choice_index = options.index(user_choice)
  computer_choice_index = options.index(computer_choice)
  if user_choice == computer_choice:
    print "It's a tie!"
  elif user_choice_index == 0 and computer_choice_index == 2:
    print WIN_RESULT
  elif user_choice_index == 1 and computer_choice_index == 0:
    print WIN_RESULT
  elif user_choice_index == 2 and computer_choice_index == 1:
    print WIN_RESULT
  elif user_choice_index > 2:
    print "An invalid option was selected"
    return
  else:
    print LOSS_RESULT

def play_RPS():
  print "Rock, Paper, Scissors"
  user_choice = raw_input("Select R for rock, P for paper, or S for scissors: ").upper()
  computer_choice = options[randint(0,len(options)-1)]
  decide_winner(user_choice, computer_choice)
  
play_RPS()
