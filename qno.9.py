print("Welcome to the Space Adventure")
choice = input("Do you want to 'land on Mars' or 'fly to Jupiter'? ")
if choice == "land on Mars":
    mars_choice = input("Do you want to 'explore' or 'build a base'? ")
    if mars_choice == "explore":
        print("You found alien artifacts. You Win!")
    elif mars_choice == "build a base":
        print("You ran out of resources. Game Over.")
    else:
        print("Invalid choice.")
elif choice == "fly to Jupiter":
    print("Your spaceship crashed. Game Over.")
else:
    print("Invalid choice.")
