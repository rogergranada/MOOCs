import numpy as np
import matplotlib.pyplot as plt

def sigmoid(X):
    X = np.array(X)
    return 1./(1+np.exp(-X))

def plot_sigmoid():
    """ Plot an example of sigmoid """
    X = np.linspace(-10, 10, 100)
    sX = sigmoid(X)
    plt.figure(figsize=(15,5))
    plt.xlabel(r'$\theta^Tx^{(i)}$')
    plt.ylabel(r'$h(x^{(i)}, \theta)$')
    plt.plot(X, sX)
    plt.show()

def load_examples():
    """ Load some examples from dataset """
    X = []
    Y = []
    with open('examples.txt') as fin:
        for i, line in enumerate(fin):
            if line[0].isdigit():
                bias, pos, neg, label = map(float, line.strip().split(','))
                X.append([bias, pos, neg])
                Y.append(label)
    X = np.array(X)
    Y = np.array(Y).reshape(i, 1)
    return X, Y
