
from random import randint


def how_many_wins_did_i_get(win_percent):
    wins = 0
    loses = 0
    while True:
        if randint(0, 99) >= win_percent:
            loses += 1
            if loses == 3:
                break
        else:
            wins += 1
            if wins == 7:
                break
    return wins

for win_percent in range(0, 101, 1):
    tries = 100000
    wins = 0
    for i in range(0, tries):
        wins += how_many_wins_did_i_get(win_percent)
    print("If you win " + str(win_percent) + "% of games, you will win an average of " + str(wins * 1.0 / tries) + " times")

