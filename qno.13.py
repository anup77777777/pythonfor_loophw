print("Welcome to the Wizarding World")
subject = input("Choose a subject: spells or potions? ")

if subject == "spells":
    action = input("Do you want to practice magic or compete in duels? ")
    if action == "practice magic":
        print("You mastered a powerful spell. You Win!")
    elif action == "compete in duels":
        print("You lost to a rival wizard. Game Over.")
    else:
        print("Invalid choice.")
elif subject == "potions":
    action = input("Do you want to brew an elixir or create poison? ")
    if action == "brew an elixir":
        print("You healed a village. You Win!")
    elif action == "create poison":
        print("Your potion backfired. Game Over.")
    else:
        print("Invalid choice.")
else:
    print("Invalid subject.")
