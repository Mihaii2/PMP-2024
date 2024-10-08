import random
import numpy as np

def simulate_experiment():
    urn = ['red', 'red', 'red', 'blue', 'blue', 'blue', 'blue', 'black', 'black']

    dice_value = random.randint(1, 6)

    if dice_value in [2, 3, 5]:  # Prime numbers
        urn.append('black')
    elif dice_value == 6:
        urn.append('red')
    else:
        urn.append('blue')

    ball = random.choice(urn)
    return ball

# Run 10000 simulations
simulations = np.array([simulate_experiment() for _ in range(100000)])

# Calculate probability of drawing a red ball
red_ball_probability = np.sum(simulations == 'red') / len(simulations)

print(f"Probability of drawing a red ball: {red_ball_probability:.4f}")