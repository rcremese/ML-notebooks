import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

STD = 1
NB_SAMPLES = 50

f = lambda x: 2 * x + 1
g = lambda x: x**2 - 24*x
h = lambda x: 0.1 * np.exp(x)

def animate_time_evolution(time : np.ndarray, history : np.ndarray):
    # create a figure and axis to plot on
    fig, ax = plt.subplots()
    ax.set(xlabel='time (in days)', ylabel='number of positive cases', title='Time evolution of the infection')
    ax.set_xlim(min(time), max(time))
    ax.set_ylim(min(history), max(history))

    def update(frame):
        # for each frame, update the data stored on each artist.
        ax.plot(time[:frame], history[:frame], 'ob')

    return animation.FuncAnimation(fig=fig, func=update, frames=len(time), interval=30)

def generate_propagation(function, tmax=7, noise_std=STD, nb_samples=NB_SAMPLES):
    time = np.linspace(0, tmax, nb_samples)
    history = function(time)
    noise = np.random.normal(0, noise_std, nb_samples)
    return time, history + noise

def plot_propagation_evolutions(time, history, interp_poly : np.polynomial.Polynomial = None):
    fig, ax = plt.subplots()
    ax.set(xlabel='time (in days)', ylabel='number of positive cases', title='Time evolution of the infection')
    ax.plot(time, history, 'ob')
    if interp_poly is not None:
        ax.plot(time, interp_poly(time), '-r')
    fig.show()

def first_propagation():
    time, history = generate_propagation(f)
    anim = animate_time_evolution(time, history)
    plt.show()

def second_propagation():
    time, history = generate_propagation(g)
    anim = animate_time_evolution(time, history)
    plt.show()

def third_propagation():
    time, history = generate_propagation(h)
    anim = animate_time_evolution(time, history)
    plt.show()

if __name__ == '__main__':
    first_propagation()
    second_propagation()
    third_propagation()