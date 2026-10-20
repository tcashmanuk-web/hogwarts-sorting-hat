print("Welcome to the Hogwarts Sorting Hat")

trait = input("What trait best describes you?").lower()  

print(trait)

print("Hmmmmmm. . .")

if trait == "brave" and trait == "intelligent":
    print("You could belong in Gryffindor or Ravenclaw!")
elif trait == "loyal":
    print("You belong in Hufflepuff!")
elif trait == "ambitious":
    print("You belong in Slytherin!")
elif trait == "hungry":
    print("You belong in the dining hall!")
else:
    print("I'm confused.")
