print("Welcome to the Hogwarts Sorting Hat")

trait = input("What trait best describes you?").lower()  

house = "Unknown"

print(trait)

print("Hmmmmmm. . .")

if trait == ("brave" or trait == "daring") and not "tired":
    print("You belong in Gryffindor!")
    house = "Gryffindor"
elif trait == "intelligent":
    print("You belong in Ravenclaw!")
    house = "Ravenclaw"
elif trait == "loyal":
    print("You belong in Hufflepuff!")
    house = "Hufflepuff"
elif trait == "ambitious":
    print("You belong in Slytherin!")
    house = "Slytherin"
elif trait == "hungry":
    print("You belong in the dining hall!")
    house = "Dining Hall"
else:
    print("I'm confused.")

print(house)