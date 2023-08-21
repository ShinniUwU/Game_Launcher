**Game Launcher Script README**

This repository contains a Python script for a simple game launcher tool that allows users to add, remove, and launch games. The script uses command-line interaction to manage a list of games and their corresponding executable directories.

## How to Use

1. **Installation**: No installation is required. Simply download or clone the repository to your local machine.

2. **Prerequisites**: Ensure that you have Python 3.x installed on your system.

3. **Run the Script**: Open a terminal or command prompt and navigate to the directory where the script is located. Run the script using the command:

   ```
   python script_name.py
   ```

   Replace `script_name.py` with the actual name of the script file.

4. **Interaction**:
   - Upon running the script, you'll see a list of existing games (if any) and options for adding, removing, and launching games.
   - Use the provided numbers to select an option:
     - `0`: Add a new game to the list.
     - `-1`: Remove a game from the list.
     - Numbers corresponding to existing games: Launch the selected game.

5. **Adding a New Game**:
   - To add a new game to the list, select option `0`.
   - Enter the name of the game.
   - Provide the directory of the game's executable.
   - If the directory is invalid, you'll have the option to change the directory or cancel the addition.

6. **Removing a Game**:
   - To remove a game from the list, select option `-1`.
   - Enter the number of the game you want to remove.

7. **Launching a Game**:
   - To launch a game, select the corresponding number associated with the game in the list.

8. **Persistence**:
   - The list of games is saved to a file named `games.p` in the Documents folder (`USERPROFILE/Documents`).
   - This ensures that your game list is preserved across sessions.

9. **Credits**:
   - The script was created by "SHINNI". The "MADE BY SHINNI" message is displayed in red at the start of the script.

10. **Note**:
   - The script uses Python's built-in `subprocess` module to launch game executables.
   - Use this script responsibly and only with games and directories you trust.

## Contact
If you encounter any issues or have suggestions for improvements, feel free to contact the script author, "SHINNI". You can also explore the code and make modifications according to your needs.

**Disclaimer**: This script is provided as-is, and any modifications or usage are at your own risk.

---
Remember to replace `"script_name.py"` with the actual name of the script file.
