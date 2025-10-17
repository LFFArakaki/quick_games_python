def game_menu(games):
    print("Which game would you like to play today?")
    for i, x in enumerate(games):
        print(f'{i+1} - {x}')
    print("0 - Stop playing")
def difficulty_menu(game):
    print("Which difficulty would you prefer?")
    for i, x in enumerate(game.difficulties):
        print(f'{i+1} - {x}')
def valid_input(options, choice):
    if choice > len(options) or choice < 0:
        print("Invalid Option!")
        return False
    return True