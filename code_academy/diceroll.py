"""
This is a project for Code Academy Pro's python track.

This program asks the user to guess a number. The program will then roll two die. If the user's guess is greater than the total value of the roll, the user wins.

The program:
	1. Prompts the user for how many sides they'd like the die to have (I added this part ,anually- it wasn't included in the project) 
  2. Randomly rolls dice and adds the values.
  3. Asks the user to guess a number
  4. Compares the guess to the roll.
  5. Decide the winner and infrom the user
"""
from random import randint
from time import sleep

def get_user_guess():
  user_guess = int(raw_input("What is your guess? "))
  return user_guess

def get_sides():
  sides = int(raw_input("How many sides would you like the die to have? "))
  return sides

def roll_dice():
  number_of_sides = get_sides()
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = 2 * number_of_sides
  print "The maximum roll is " + str(max_val)
  sleep(1)
  user_guess = get_user_guess()
  
  if user_guess > max_val:
    print "Your guess is greater than the maximum possible value of" + str(max_val)
    return
  else:
    print "Rolling..."
    sleep(2)
    print "The first roll is: %d" % (first_roll)
    sleep(1)
    print "The second roll is: %d" % (second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print "The total value is: %d" % (total_roll)
    print "Result..."
    sleep(1)
    if user_guess > total_roll:
      print "Hooray! You won!"
    else:
      print "Sorry, you lost =("

roll_dice()
    
  