import os
import subprocess
import pickle

# Define a list of games
games = []

# Get the path to the Documents folder
documents_path = os.path.join(os.environ['USERPROFILE'], 'Documents')

# Get the path to the games.p file in the Documents folder
games_path = os.path.join(documents_path, 'games.p')

try:
    with open(games_path, "rb") as f:
        games = pickle.load(f)
except:
    # If the file does not exist or there is an error opening it, use the default empty list
    pass

# Print the "SHINNI" message in red font (do not change this if you are going to use it or at least give me credit ty <3)
print("\033[91m" + "MADE BY SHINNI" + "\033[0m")

while True:
    # Print the list of games and get the user's choice
    print("What kind of game do you want to play? Choose a number:")
    print("0. Add a new game")
    print("-1. Remove a game")
    for i, game in enumerate(games):
        print(f"{i + 1}. {game[0]}")
    choice = input()

    # Try to launch the chosen game
    if str(choice) == "0":
        # Add a new game to the list
        game_name = input("Enter the name of the game: ")
        while not game_name:  # Prompt the user to enter a game name until they do
            print("Please enter a game name.")
            game_name = input("Enter the name of the game: ")
        game_dir = input("Enter the directory of the game executable: ")
        if game_dir == "return":  # Allow the user to go back
            continue  # Go back to the menu
        # Add the r prefix to the game directory
        game_dir = r"{}".format(game_dir)
        while not os.path.exists(game_dir):
            # Handle invalid game directory
            print("Game executable not found. Please check the directory you provided.")
            print("Would you like to change the directory or stop adding the game to the list?")
            print("1. Change directory")
            print("2. Stop adding the game to the list")
            directory_choice = input("Enter your choice: ")
            if directory_choice == "1":
                # Change the directory
                game_dir = input("Enter the new directory of the game executable: ")
                # Add the r prefix to the game directory
                game_dir = r"{}".format(game_dir)
            elif directory_choice == "2":
                # Stop adding the game to the list
                game_dir = None  # Set game_dir to None to exit the loop
                break  # Exit the loop
        if game_dir:  # Check if game_dir is not None
            # Add the game to the list
            games.append([game_name, game_dir])
            with open(games_path, "wb") as f:
                pickle.dump(games, f)  # Save the list of games
            print(f"{game_name} was added to the game list.")
        elif str(choice) == "-1":
            game_number = input("Enter the number of the game you want to remove: ")
            if game_number.isnumeric() and 0 < int(game_number) <= len(games):
                # Remove the chosen game from the list
                game_name, game_dir = games.pop(int(game_number) - 1)
                with open(games_path, "wb") as f:
                    pickle.dump(games, f)  # Save the list of games
                print(f"{game_name} was removed from the game list.")
            else:
                # Handle invalid input
                print("Invalid game number. Please choose a number from the list.")
        elif choice.isnumeric() and 0 < int(choice) <= len(games):
            # Open the chosen game
            game_name, game_dir = games[int(choice) - 1]
            print(f"Opening {game_name}...")
            subprocess.call(game_dir)
        else:
            # Handle invalid input
            print("Invalid input. Please choose a number from the list.")
