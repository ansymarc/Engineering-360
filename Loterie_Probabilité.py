import numpy as np

# Parameters
number_range = 100
n_play = 50
chosen_numbers = np.random.choice(number_range, size=n_play, replace=False)
n_simulations = 20000



# Lottery simulation function
def simulate_lottery():
    results = np.random.randint(0, number_range, size=3)
    win = 0
    if results[0] in chosen_numbers: win += 50
    if results[1] in chosen_numbers: win += 20
    if results[2] in chosen_numbers: win += 10
    return win, results



wins = []

for i in range(0, n_simulations):
    reward, numbers = simulate_lottery()
    is_benefit = reward > n_play
    wins.append(is_benefit)
    
    
prob = sum(wins) / len(wins)
n_wins = sum(wins)


print(prob)







