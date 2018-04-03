import sys
for i in sys.stdin:
    arguments = i.split()
    attempts = int(arguments[0])
    winning_probability = float(arguments[1])
    answer = 0.0
    probable_streak, amount_of_games = attempts + 1, attempts + 1
    #Max streak chance will hold chance of having <probable_streak> after <amount_of_games>
    max_streak_chance = [[0 for x in range(probable_streak)] for y in range(amount_of_games)]
    #Chance to win all games holds chance to win all games, winning x out of x games in a row.
    chance_to_win_all_games = [0 for x in range(attempts+1)]

    chance_to_win_all_games[0] = 1.0
    max_streak_chance[0][0] = 1.0
    for i in range(1, attempts + 1):
        chance_to_win_all_games[i] = chance_to_win_all_games[i-1]*winning_probability
        max_streak_chance[0][i] = 1.0
    for i in range(1, attempts + 1):
        for j in range(0, attempts + 1):
            max_streak_chance[i][j] = max_streak_chance[i-1][j]
            if j == (i-1):
                max_streak_chance[i][j] -= chance_to_win_all_games[i]
            if j < (i - 1):
                max_streak_chance[i][j] -= max_streak_chance[i - j - 2][j]* (1-winning_probability) * chance_to_win_all_games[j+1]
            if i == attempts:
                answer += (j*(max_streak_chance[attempts][j] - max_streak_chance[attempts][j - 1]))
    print(answer)