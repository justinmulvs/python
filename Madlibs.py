"""Done as part of Code Academy Pro's Python track.
This program is meant to create a mad libs story.
It will take input in the form of words from the reader, and insert them into a pre-composed story which it will print.
"""

print "Mad libs has begun! Input the given word types."
name = raw_input("A name: ")
adj1 = raw_input("An adjective: ")
adj2 = raw_input("Another adjective: ")
adj3 = raw_input("One last adjective! ")
verb1 = raw_input("A verb: ")
verb2 = raw_input("Another verb: ")
verb3 = raw_input("One more verb: ")
noun1 = raw_input("How about a noun?: ")
noun2 = raw_input("How about another noun? ")
noun3 = raw_input("How about a THIRD noun? ")
noun4 = raw_input("This is the last noun, I promise: ")

print "Now for the fun stuff."
animal = raw_input("An animal: ")
food = raw_input("A food: ")
fruit = raw_input("A fruit: ")
number = raw_input("A number: ")
hero = raw_input("A superhero name: ")
country = raw_input ("A country: ")
dessert = raw_input("A dessert: ")
year = raw_input("A year: ")

#The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rythym of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world." % (adj1, name, verb1, adj2, noun1, noun2, animal, food, verb2, noun3, fruit, adj3, name, verb3, number, name, hero, hero, name, country, name, dessert, name, year, noun4)

print STORY
