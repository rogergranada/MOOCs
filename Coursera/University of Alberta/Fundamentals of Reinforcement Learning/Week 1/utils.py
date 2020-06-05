# utils.py
# 
# This file contains functions that may be imported by `Module 1.ipynb`,
# such as plotting functions.

from IPython.display import display, clear_output
import matplotlib.pyplot as plt
from collections import defaultdict
import numpy as np
import random
random.seed(6)
np.random.seed(5)

# Plotting functions
def plot_distribution(dists, means):
    """ Plots the distribution using a violin plot 
    
    Parameters:
    -----------
    dists: array 
        array containing a numpy distribution for each arm.
        In the example it has a shape (10, 1000)
    means: array
        array containing the mean of each distribution
        In the example, it has a shape (10,)
    """
    minimum_mean = np.argmin(means)
    maximum_mean = np.argmax(means)
    print('Arm with minimum reward:', minimum_mean)
    print('Arm with maximum reward:', maximum_mean)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.violinplot(dists, showmeans=True, points=20)
    ax.plot([0]*(len(means)+2), 'k--', linewidth=1)

    plt.xticks(np.arange(1, len(dists)+1, 1.0), range(0, len(dists)))
    plt.xlabel('Action', fontsize=14)
    plt.ylabel('Reward Distribution', fontsize=14)
   
    pos = range(len(means))
    for tick,label in zip(pos, ax.get_xticklabels()):
        ax.text(pos[tick]+1.1,  means[tick]+.3, means[tick])
    plt.show()

    
def plot_multiple(list_1, list_2, list_3, x_axis, y_axis, labels, title):
    """ Plot three distribution of selected arms.

    Parameters:
    -----------
    list_1: array
        array containing the number of the selected arm in a 
        single run. In the example it has the shape (1000,).
    list_2: array
        array containing the number of the selected arm in a 
        single run. In the example it has the shape (1000,).
    list_3: array
        array containing the number of the selected arm in a 
        single run. In the example it has the shape (1000,).
    x_axis: string
        text for the x-axis
    y_axis: string
        text for the y-axis
    labels: array
        array containing the label of each one of the three plots
    title: string
        title of the plot
    """
    data = [list_1, list_2, list_3]
    fig, axis = plt.subplots(1, 3, figsize=(20, 5))
    fig.suptitle(title)
    for i, ax in enumerate(axis):
        ax.plot(range(len(data[i])), data[i], color='#007BA7')
        ax.set_title(labels[i])
        ax.set(xlabel=x_axis, ylabel=y_axis)
    plt.show()


def plot_both_distributions(bandit, arm_low, arm_high):
    """ Plot two distributions in the same plot

    Parameters:
    -----------
    bandit: Bandit class
        class containing information about the bandit
    arm_low: int
        number of the arm with the lowest mean
    arm_high: int
        number of the arm with the highest mean
    """
    # Plot distribution of two distinct arms of the bandit
    minimum_mean = np.argmin(bandit.means)
    maximum_mean = np.argmax(bandit.means)
    print('Arm with minimum reward:', minimum_mean)
    print('Arm with maximum reward:', maximum_mean)
    plt.clf()
    rwds_low = []
    rwds_high = []
    for i in range(1000):
        rwds_low.append(bandit.pull(arm_low))
        rwds_high.append(bandit.pull(arm_high))

    fig, ax = plt.subplots(figsize=(10, 6))
    plt.hist(rwds_low, bins=100, color='green', alpha=0.5, label='Arm number: '+str(arm_low))
    plt.axvline(x=np.mean(rwds_low), color='k', linestyle='--')
    plt.hist(rwds_high, bins=100, color='#007BA7', alpha=0.5, label='Arm number: '+str(arm_high))
    plt.axvline(x=np.mean(rwds_high), color='k', linestyle='--')
    plt.xlabel('Reward', fontsize=14)
    plt.ylabel('Times Reward is Selected', fontsize=14)
    ax.legend()
    plt.show()


def plot_multiple_arms(list_arms):
    """ Plot all the steps of multiple arms

    Parameters:
    -----------
    list_arms: array
        array containing for each arm the reward in each steps.
        In the example, the shape is (3, 1000)
    """
    plt.clf()
    color = ['green', 'red', '#007BA7']
    mean_rwd = np.mean(list_arms, axis=0)
    fig, ax = plt.subplots(figsize=(10, 6))
    for i, run in enumerate(list_arms):
        plt.plot(run, color=color[i], label='Run {}'.format(i), alpha=0.4)

    x = range(len(mean_rwd))
    coefs = np.polyfit(x, list_arms[0], deg=10)
    p_obj = np.poly1d(coefs)
    y_line = p_obj(x)
    plt.plot(x, y_line, 'r--', label='Fit runs')

    plt.xlabel('Steps', fontsize=14)
    plt.ylabel('Reward', fontsize=14)
    plt.legend()
    plt.show()


def plot_average_reward(dist_1, dist_2, dist_3, labels, nb_runs):
    """ Plot the average reward for three different distributions.

    Parameters:
    -----------
    dist_1: array
        Distribution of rewards for all steps
    dist_2: array
        Distribution of rewards for all steps
    dist_3: array
        Distribution of rewards for all steps
    """
    plt.clf()
    rwd_dist_1 = np.divide(dist_1, len(dist_1))
    rwd_dist_2 = np.divide(dist_2, len(dist_2))
    rwd_dist_3 = np.divide(dist_3, len(dist_3))
    plot_multiple(rwd_dist_1, rwd_dist_2, rwd_dist_3, 
                  'Steps', 'Average Reward', labels,
                  'Average reward for {} runs of 10-armed bandit'.format(nb_runs))
    plt.show()

def plot_average_in_one(dist_1, dist_2, dist_3, labels):
    """ Plots the average reward distribution in one plot.

    Parameters:
    -----------
    dist_1: array
        Distribution of rewards for all steps
    dist_2: array
        Distribution of rewards for all steps
    dist_3: array
        Distribution of rewards for all steps
    """
    plt.clf()
    rwd_dist_1 = np.divide(dist_1, len(dist_1))
    rwd_dist_2 = np.divide(dist_2, len(dist_2))
    rwd_dist_3 = np.divide(dist_3, len(dist_3))
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.plot(rwd_dist_1, color='green', label=labels[0])
    plt.plot(rwd_dist_2, color='red', label=labels[1])
    plt.plot(rwd_dist_3, color='#007BA7', label=labels[2])
    plt.xlabel('Steps', fontsize=14)
    plt.ylabel('Average Reward', fontsize=14)
    plt.legend()
    plt.show()


def plot_distribution_each_arm(bandit, acc_distributions, nb_runs, labels, title):
    """ Plot the accumulated distribution of each arm.

    Parameters:
    -----------
    bandit: Bandit class
        Bandit containing the means array
    acc_distribution: array
        Array containing the distribution of arms for each step.
        In the example, the shape is (1000, 10) 
    nb_runs: int
        Number of runs the simulation performed
    """
    print('Arm with minimum reward: {}'.format(np.argmin(bandit.means)))
    print('Arm with maximum reward: {}'.format(np.argmax(bandit.means)))

    plt.clf()
    fig, axis = plt.subplots(1, 3, figsize=(20, 5))
    fig.suptitle(title)

    for index, ax in enumerate(axis):
        acc_distribution = acc_distributions[index]
        dic = defaultdict(list)
        for i in range(len(acc_distribution)):
            for j in range(len(acc_distribution[i])):
                dic[j].append(acc_distribution[i][j]*100/nb_runs)
        
        for i in dic:
            ax.plot(dic[i], label='arm = {}'.format(i))
        ax.set(xlabel='Steps', ylabel='% selected arm')
        ax.set_title(labels[index])
        ax.legend()
    plt.show()


def plot_two_columns(target, data, title):
    """ Plot a 2x2 graphics with vectors in data dictionary.
    
    Parameters:
    -----------
    target: array
        array containing ground elements
    data: dict
        dictionary containing the label in the key and an array
        of values in the value.
    title: string
        string containing the text in the top of the plots. 
    """
    plt.clf()
    fig, axis = plt.subplots(2, 2, figsize=(20, 7))
    fig.suptitle(title)
    pos = [(0, 0), (0, 1), (1, 0), (1, 1)]
    labels = sorted(data.keys())
    for i, val in enumerate(pos):
        x, y = val
        key = labels[i]
        axis[x, y].plot(range(len(target)), target)
        axis[x, y].plot(range(len(data[key])), data[key], color='red')
        axis[x, y].set_title('Answer ({})'.format(key))
    plt.show()
