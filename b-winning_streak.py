import sys, itertools

def longest_streak(wins_and_losses):
    streak, resulting_streak = 0, 0
    for state in wins_and_losses:
        if state != 1:
            streak = 0
        else:
            streak = streak + 1
            if streak > resulting_streak:
                resulting_streak = streak
    return resulting_streak

def cummulative_probability(wins_and_losses, winning_probability):
    losing_probability = 1 - winning_probability
    probability = 1
    for state in wins_and_losses:
        if(int(state) == 1):
            probability = probability*winning_probability
        else:
            probability = probability*losing_probability
    return probability

for i in sys.stdin:
    arguments = i.split()
    amount_of_tries = int(arguments[0])
    winning_probability = float(arguments[1])
    expected_length = 0
    
    for combo in itertools.product([0, 1], repeat=amount_of_tries):
        win_loss_combo = combo
        expected_length = expected_length + (longest_streak(win_loss_combo)*cummulative_probability(win_loss_combo,winning_probability))
    print(expected_length)
