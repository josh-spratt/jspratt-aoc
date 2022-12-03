def get_game_result(opponent_plays, you_play):
    if you_play == opponent_plays:
        return 'draw'
    elif you_play == 'rock':
        if opponent_plays == 'paper':
            return 'lose'
        elif opponent_plays == 'scissor':
            return 'win'
    elif you_play == 'paper':
    elif you_play == 'scissor':