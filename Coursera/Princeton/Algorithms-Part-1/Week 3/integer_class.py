class Integer(object):
    def __init__(self, v):
        self.v = v
        
    def __str__(self):
        print(self.v)
        
    def __repr__(self):
        return str(self.v)
        
    def compare_to(self, w):
        if self.v < w.v: return -1
        if self.v > w.v: return 1
        return 0
