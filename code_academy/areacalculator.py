'''This is a project for Code Academy Pro's python track.

This calculator will calculate the area for a given shape which the user selects and then print it'''

from math import pi
from time import sleep
from datetime import datetime

now = datetime.now()

print "The calculator is starting up!"
print "The date and time is %s/%s/%s %s:%s." % (now.month, now.day, now.year, now.hour, now.minute)

sleep (1)

hint = "Don't forget to include the correct units! \nExiting..."

option = raw_input("Enter C for Circle, T for Triangle, or S for square: ").upper()

if option == "C":
  radius = float(raw_input("What is the circle's radius? "))
  area = pi * (radius ** 2)
  print "The pi is baking..."
  sleep(1)
  print ("Area: %.2f \n%s" % (area, hint))
elif option == "T":
  base = float(raw_input("What is the length of the triangle's base? "))
  height = float(raw_input("What is the triangle's height? "))
  area = 0.5 * base * height
  print "Uni Bi Tri..."
  sleep(1)
  print ("Area: %.2f \n%s" % (area, hint))
elif option == "S":
  side = float(raw_input("What is the length of one side? "))
  area = side ** 2
  print "Calculating..."
  sleep(1)
  print("Area: %.2f \n%s" % (area, hint))
else:
  print "You didn't enter a valid shape! The program will now exit."