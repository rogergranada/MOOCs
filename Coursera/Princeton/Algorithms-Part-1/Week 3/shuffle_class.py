import random
class Shuffle(object):
    def __init__(self):
        pass

    def shuffle(self, vec):
        N = len(vec)
        for i in range(1, N):
            r = random.randint(0, i-1)
            self.exchange(vec, i, r)
            #print('i={} : r={} :: {}'.format(i, r, vec))
        return vec
    
    def exchange(self, vec, i, j):
        swap = vec[i]
        vec[i] = vec[j]
        vec[j] = swap
        return vec
