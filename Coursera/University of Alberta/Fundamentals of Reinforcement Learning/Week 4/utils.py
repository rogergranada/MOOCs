# utils.py
# 
# This file contains functions that may be imported by `Module 4.ipynb`,
# such as plotting functions.

import matplotlib.pyplot as plt
import numpy as np
import itertools

# Definitions
LEFT = 0
UP = 1
RIGHT = 2
DOWN = 3

ARROW_ORIENTATION = {
    0: [[1.7,1.0,-1.1,0.0]], # arrow LEFT
    1: [[1.0,0.3,0.0,1.1]],  # arrow UP
    2: [[0.3,1.0,1.1,0.0]],  # arrow RIGHT
    3: [[1.0,1.7,0.0,-1.1]], # arrow DOWN
    4: [[1.7,0.3,-1.1,0.0],  # arrow LEFT-UP
        [1.7,0.3,0.0,1.1]],  
    5: [[1.0,1.0,-0.4,0.0],  # arrow LEFT-RIGHT
        [1.0,1.0,0.4,0.0]],
    6: [[1.7,1.7,-1.1,0.0],  # arrow LEFT-DOwN
        [1.7,1.7,0.0,-1.1]],
    7: [[0.3,0.3,0.0,1.1],   # arrow UP-RIGHT
        [0.3,0.3,1.1,0.0]],
    8: [[1.0,1.0,0.0,0.4],   # arrow UP-DOWN
        [1.0,1.0,0.0,-0.4]],
    9: [[0.3,1.7,0.0,-1.1],  # arrow RIGHT-DOWN
        [0.3,1.7,1.1,0.0]],
    10: [[1.0,0.3,0.0,1.1],  # arrow LEFT-UP-RIGHT
        [1.0,0.3,-1.1,0.0],
        [1.0,0.3,1.1,0.0]],
    11: [[1.7,1.0,-1.1,0.0], # arrow LEFT-UP-DOWN
        [1.7,1.0,0.0,0.4],
        [1.7,1.0,0.0,-0.4]],
    12: [[1.0,1.7,0.0,-1.1], # arrow LEFT-RIGHT-DOWN
        [1.0,1.7,-0.4,0.0],
        [1.0,1.7,0.4,0.0]],
    13: [[0.3,1.0,1.1,0.0],  # arrow UP-RIGHT-DOWN
        [0.3,1.0,0.0,0.4],
        [0.3,1.0,0.0,-0.4]],
    14: [[1.0,1.0,0.0,0.4],  # arrow LEFT-UP-RIGHT-DOWN
        [1.0,1.0,0.0,-0.4],
        [1.0,1.0,-0.4,0.0],
        [1.0,1.0,0.4,0.0]]
}

def generate_encoding():
    """ Return a dictionary with the set of keys and their
        corresponding id. The first id of the list is zero
        and the last contains all elements. An excerpt of the
        output dictionary is:
        
        {(0,):0, (1,):1, ..., (0,3):6, ... (1,2,3):13, (1,2,3,4):14
    """
    indexes = [LEFT, UP, RIGHT, DOWN] 
    combine = lambda x: itertools.combinations(indexes, x)
    sequences = itertools.chain(*map(combine, range(1, len(indexes)+1)))
    encoded = [(key, i) for i, key in enumerate(sequences)]
    return dict(encoded)


def encode_to_arrow(pos_index):
    """ Convert values in the array to a representation for
        arrows.

    Parameters:
    -----------
    pos_index: 1D array
        index of the position to the arrow. For example, the
        index=0 represents the arrow to the left. If the array
        contains more than one value, the representation is 
        composed by multiple arrows. 

    Example:
    --------
    >>encode_to_arrow([0, 1, 3])
      #generates the LEFT-UP-DOWN arrow, represented by the id=11
    """
    pos_index = tuple(pos_index)
    denc = generate_encoding()
    if pos_index in denc:
        return denc[pos_index]
    print('ERROR: Could not find key {}'.format(pos_index))
    return None
    '''
    if len(pos_index) == 2:
        if pos_index[0] == 0 and pos_index[1] == 1:
            return 4
        if maxargs[0] == 0 and maxargs[1] == 2:
            return 5
        if maxargs[0] == 0 and maxargs[1] == 3:
            return 6
        if maxargs[0] == 1 and maxargs[1] == 2:
            return 7
        if maxargs[0] == 1 and maxargs[1] == 3:
            return 8
        if maxargs[0] == 2 and maxargs[1] == 3:
            return 9
        else:
            print("NO: ", maxargs)
    if len(maxargs) == 3:
        if maxargs[0] == 0 and maxargs[1] == 1 and maxargs[1] == 2:
            return 10
        if maxargs[0] == 0 and maxargs[1] == 1 and maxargs[1] == 3:
            return 11
        if maxargs[0] == 0 and maxargs[1] == 2 and maxargs[1] == 3:
            return 12
        if maxargs[0] == 1 and maxargs[1] == 2 and maxargs[1] == 3:
            return 13
    if len(maxargs) == 4:
        return 14
    return maxargs[0]
    '''



# Plotting functions
def plot_arrows(matrix, figsize=(4,4)):
    """ Plot a matrix with arrows for each cell.
        Each cell in the matrix has a size of 2x2

    Parameters:
    -----------
    matrix: 2D array
        matrix containing the ids representing each row
        For example, the matrix [[1, 2], [7, 13]] would
        generate the arrows:
        [[LEFT, UP], [UP-RIGHT, UP-RIGHT-DOWN]]
    """
    xdist, ydist = figsize
    plt.figure(figsize=figsize)
    plt.title('Optimal Policies')
    plt.xlim((0,2*xdist))
    plt.ylim((0,2*ydist))
    matrix = np.array(matrix)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            id_arrow = int(matrix[i][j])
            arrows = ARROW_ORIENTATION[id_arrow]
            for arrow in arrows:
                x, y, w, h = arrow
                px = 2*j + x
                py = 2*(matrix.shape[0] - i - 1) + y
                plt.arrow(px, py, w, h, fc="b", ec="b", head_width=0.3, head_length=0.3)
    plt.xticks(range(2*xdist), " ")
    plt.yticks(range(2*ydist), " ")
    plt.show()

