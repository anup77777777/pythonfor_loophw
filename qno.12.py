
print("Welcome to the Pirate Ship Adventure")
choice = input("Do you want to 'search for treasure' or 'battle enemy ships'? ")

if choice == "search for treasure":
    treasure_choice = input("Do you want to 'dig on the island' or 'explore the cave'? ")
    if treasure_choice == "dig on the island":
        print("You found a hidden treasure chest. You Win!")
    elif treasure_choice == "explore the cave":
        print("You were trapped inside. Game Over.")
    else:
        print("Invalid choice.")
elif choice == "battle enemy ships":
    battle_choice = input("Do you want to 'attack' or 'defend'? ")
    if battle_choice == "attack":
        print("You won the battle. You Win!")
    elif battle_choice == "defend":
        print("You were outnumbered. Game Over.")
    else:
        print("Invalid choice.")
else:
    print("Invalid choice.")
