print("Welcome to the Cybersecurity Mission")
task = input("Do you want to trace the hacker or secure the system? ")
if task == "trace the hacker":
    action = input("Do you want to track their IP or decode their message? ")
    if action == "track their IP":
        print("You caught the hacker. You Win!")
    elif action == "decode their message":
        print("The message was a trap. Game Over.")
    else:
        print("Invalid choice.")
elif task == "secure the system":
    action = input("Do you want to shut down the server or upgrade the firewall? ")
    if action == "shut down the server":
        print("The attack was stopped. You Win!")
    elif action == "upgrade the firewall":
        print("The hacker bypassed it. Game Over.")
    else:
        print("Invalid choice.")
else:
    print("Invalid task.")
