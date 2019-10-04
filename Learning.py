# this is an octothorpe -- it makes a comment (line ignored by computer)
# print("hello world")
print("Howdy, y'all")
print("I like typing this")
print("this is fun")

# math skills demo
# prints the following sentence
print("I will not count my chickens", 2)
# calculates the  equation giving the number of hens
print("Hens: ", (.25 * 10) + 30 / 6)
# calculates the number of roosters in the equation
print("Roosters: ", (10 * 10) - 25.0 * 3 % 4)
# prints the phrase "I will count the eggs
print("Now I will count the eggs", 7)
# solves the equation for the number of eggs
print(+ 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
# Solves a greater than less than equation
print(3 + 2 < 5 - 7)
print("I will now count my chicks and geese")
print(50.0 - 25.0 + 5.0 - 10.0)

# Variables and some of their powers
cars = 80
spaceInACar = 4.0
drivers = 45
passengers = 115
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = spaceInACar * cars_driven
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("there are", drivers, "drivers available today.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put approximately", average_passengers_per_car, "in each car.")

# a story using variables
teams = 10
number_of_games = 100
games_per_team = number_of_games / teams
player_to_a_team = 9
players = 120
players_that_can_play = teams * player_to_a_team
players_who_cannot_play = players - players_that_can_play


print("There are", teams, "teams available.")
print("There will be", players_who_cannot_play, "who will not make a team.")
print("There will be", players_that_can_play, "as a whole.")
print("")

# More variables and playing with output
myName = "Adrian Vasquez"
myAge = "17"
myHeight = 60 # inches
myEyes = "brown"
myHair = "black"

print("Let's talk about %s." % myName)
print("He's %d inches tall." % myHeight)
print("He's got %s eyes amd %s hair." % (myEyes, myHair))
print("add %d and %d, I get %d" % (myAge, myHeight, myAge+myHeight))