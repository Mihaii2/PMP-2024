import random
import numpy as np
import matplotlib.pyplot as plt

# a) N urmeaza o distributie exponentiala, P(1 pas) = 1/2, P(2 pasi) = 1/2^2, P(n pasi) = 1/2^n


""" helper pseudocode
function play(prob=0.5)
N = 0
player2_debt = 0
while(1)
    coin = player1.flip_coin(prob = 0.5)
    if(coin < 0.5) # stema
        dice = player2.throw
        player2_debt = dice - 3
        break
    else 
        player2_debt -= 0.5
    N += 1
"""
# b)
def play(prob = 0.5):
    N = 0
    player2_debt = 0
    while(1):
        coin_flip = random.random()
        if(coin_flip < prob):
            dice = np.random.choice(range(6), size=1) + 1 # player2 throws dice, add 1 because random.choice picks from 0 to 5 in our line
            player2_debt = dice - 3
            break
        else:
            player2_debt -= 0.5
        N += 1
    return N, player2_debt

simulations = np.empty(20000)

for i in range(0, 20000):
    result = play(0.5)
    simulations[i] = result[0]

plt.hist(simulations, bins=60, edgecolor='black')

plt.title('Histogram of N')
plt.xlabel('N')
plt.ylabel('Frequency')
plt.show()

# c)
print("Mean with fair coin: ",simulations.mean())

# d)

simulations_03_tails = np.empty(20000)

for i in range(0, 20000):
    result = play(0.3)
    simulations_03_tails[i] = result[0]

plt.hist(simulations_03_tails, bins=60, edgecolor='black')

plt.title('Histogram of N')
plt.xlabel('N')
plt.ylabel('Frequency')
plt.show()

print("Mean with 0.3 tails probability: ", simulations_03_tails.mean())

simulations_07_tails = np.empty(20000)

for i in range(0, 20000):
    result = play(0.7)
    simulations_07_tails[i] = result[0]

plt.hist(simulations_07_tails, bins=60, edgecolor='black')

plt.title('Histogram of N')
plt.xlabel('N')
plt.ylabel('Frequency')
plt.show()

print("Mean with 0.3 tails probability: ", simulations_07_tails.mean())