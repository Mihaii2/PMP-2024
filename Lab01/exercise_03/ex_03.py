import numpy as np
import arviz as az
import matplotlib .pyplot as plt

""" helper pseudocode
frizer_1 = exp(1/3)
frizer_2 = exp(1/6)
frizer_3 = exp(1/4)

def get_serve_time()
    nr_frizer = np.random.choice(range(13), size=1) 0 - 2 => frizer1, 3-8 => frizer2, 9-12 => frizer3
    X = 0
    if(nr_frizer <= 2):
        X = exp(1/3)
    elif(nr_frizer <= 8):
        X = exp(1/6)
    else:
        X = exp(1/4)

simulations = []
loop 10000 times
    simulations.append(get_serve_time())

mean = simulations.mean()
stdev = simulations.stdev()

plot_pdf(normal, mean, stdev)

"""
def get_serve_time():
    nr_frizer = np.random.choice(range(13), size=1)
    X=0
    if(nr_frizer <= 2):
        X = np.random.exponential(scale=1/3)
    elif(nr_frizer <= 8):
        X = np.random.exponential(scale=1/6)
    else:
        X = np.random.exponential(scale=1/4)
    return X

simulations = np.empty(10000)

for i in range(0, 10000):
    simulations[i] = get_serve_time()

print("Mean: ", simulations.mean())
print("Stdev: ", simulations.std())

az.plot_kde(simulations)

plt.title('Density Function')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()