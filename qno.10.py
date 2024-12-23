print("Welcome to the Haunted Castle")
choice = input("Do you want to 'enter the castle' or 'run away'? ")
if choice == "enter the castle":
    door = input("Choose a door: 'red', 'green', or 'black': ")
    if door == "red":
        print("You entered a room full of flames. Game Over.")
    elif door == "green":
        print("You found the treasure. You Win!")
    elif door == "black":
        print("You were captured by ghosts. Game Over.")
    else:
        print("Invalid door.")
elif choice == "run away":
    print("You escaped safely.")
else:
    print("Invalid choice.")
