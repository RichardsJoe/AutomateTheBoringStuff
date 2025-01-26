#Determine the odds a 6 consecutive H or T flips.
#Based on how many flips are done and how many times this is repeated

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

def has_streak(flip_results):
    has_streak = False
    #convert the list into a string
    result_string = ''
    for result in flip_results:
        result_string += result
    
    if ('HHHHHH') in result_string:
        has_streak = True
    if ('TTTTTT') in result_string:
        has_streak = True
    
    return has_streak
        
        
experimentNumber = 10000
n_streaks = 0
for count in range(experimentNumber):
    if has_streak(flip_coin(100)) == True:
        
        n_streaks += 1
    else:
        continue
print(n_streaks)

probability_of_streak = (n_streaks / experimentNumber) * 100  
print(f"Chance of streak: {probability_of_streak}%")