A simple text-based game where the player can navigate through different rooms of a house.

In this project, the game is represented by a dictionary called rooms that contains information about each room in the house. 
Each room has a description and a list of available exits to other rooms.

The play_game function handles the main game logic. 
It initializes the current room to the "living room" and enters a loop where it displays the current room's description, available exits, and prompts the player for their choice. 
If the player's choice matches one of the available exits, the current room is updated accordingly. Otherwise, an error message is displayed.
