import random

def flip_coin(n_flips):
    results = []
    for n in range(n_flips):
        flip = random.randint(0,1)
        if flip == 0:
            result = 'H'
        if flip == 1:
            result = 'T'
            
        results.append(result)
    return results

def count_streak(streak_length, flip_results):
    #number of n_count streaks for H or T inside the results.
    pass

(flip_coin(100))