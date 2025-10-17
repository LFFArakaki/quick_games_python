from games.guess import guess
import helpful.util as util

games = [guess]
end_game = False
while not end_game:
    util.game_menu(games)
    choice = int(input())
    if choice == 0:
        end_game = True
        print("Thanks for playing!")
    else:
        if util.valid_input(games, choice):
            game = games[choice-1]
            util.difficulty_menu(game)
            choice = int(input())
            if util.valid_input(game.difficulties, choice):
                mode = game.difficulties[choice-1]
                mode.play()