rooms = {
    "living room": {
        "description": "You are in the living room. There is a cozy sofa and a TV.",
        "exits": {"kitchen": "Go to the kitchen", "bedroom": "Go to the bedroom", "exit": "Exit the house"}
    },
    "kitchen": {
        "description": "You are in the kitchen. There is a dining table and a fridge.",
        "exits": {"living room": "Go to the living room"}
    },
    "bedroom": {
        "description": "You are in the bedroom. There is a comfortable bed and a wardrobe.",
        "exits": {"living room": "Go to the living room"}
    }
}

def play_game():
    current_room = "living room"

    while True:
        print()
        print(rooms[current_room]["description"])
        print("Available exits:")
        for index, (exit_room, exit_desc) in enumerate(rooms[current_room]["exits"].items(), start=1):
            print(f"{index}. {exit_desc}")

        user_choice = input("Enter the number of your choice: ")
        print()

        if user_choice.isdigit():
            index = int(user_choice)
            if index in range(1, len(rooms[current_room]["exits"]) + 1):
                selected_room = list(rooms[current_room]["exits"].keys())[index - 1]
                if selected_room == "exit" and current_room == "living room":
                    print("Exiting the house...")
                    break
                else:
                    current_room = selected_room
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Invalid input. Please enter the number corresponding to your choice.")

# Start the game
if __name__ == '__main__':
    play_game()
