# Building a vector class
class vector:
    """ Represent a vector in multidimensional space"""
    def __init__(self, elem_list):
        self.coords = elem_list
    def __len__(self):
        return len(self.coords)
    def __getitem__(self, j):
        return self.coords[j]
    def __setitem__(self, j, val):
        self.coords[j] = val
    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    def __eq__(self, other):
        return self.coords == other.coords
    def norm(self):
        ''' Magnitude of the vector '''
        ans = 0
        for num in self.coords:
            ans += num ** 2
        ans = ans ** 0.5
        return ans
