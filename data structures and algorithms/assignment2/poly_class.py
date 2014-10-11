# Implementing a polynomial class
class poly:
    '''A polynomial class'''
    def __init__(self, coefficients):
        '''Defining the polynomial class
        >>> a = poly([1, 2, 3])
        >>> a.disp()
        [1, 2, 3]
        '''
        self._coeff = coefficients
        self._order = len(coefficients) - 1

    def __add__(self, other):
        '''Addition of  2 polynomials
        >>> a = poly([1, 2, 3])
        >>> b = poly([1,2])
        >>> (a + b).disp()
        [2, 4, 3]
        '''
        if type(other) != type(self):
            raise TypeError
        polysum = poly([])
        big = max([self._coeff, other._coeff], key=len)
        small = min([self._coeff, other._coeff], key=len)
        for i, op2 in enumerate(big):
            if i < len(small):
                polysum._coeff.append(small[i] + op2)
            else:
                polysum._coeff.append(big[i])
        polysum._order = len(polysum._coeff) - 1
        return polysum

    def __sub__(self, other):
        '''Subtration of  2 polynomials
        >>> a = poly([1, 2, 3])
        >>> b = poly([1,2])
        >>> (a - b).disp()
        [0, 0, 3]
        '''
        if type(other) != type(self):
            raise TypeError
        temp = poly([])
        temp._order = other._order
        temp._coeff = [-1 * dummy for dummy in other._coeff]
        return self + temp

    def __mul__(self, other):
        '''Multiplication of  2 polynomials
        >>> a = poly([1, 2, 3])
        >>> b = poly([1,2])
        >>> (a * b).disp()
        [1, 4, 7, 6]
        '''
        # Multiplication with scalar
        if type(other) == type(1):
            temp = poly([])
            temp._order = self._order
            temp._coeff = [other * s for s in self._coeff]
            return temp
        if type(other) != type(self):
            raise TypeError
        polymul1 = poly([])
        polymul2 = poly([])
        big = max([self._coeff, other._coeff], key=len)
        small = min([self._coeff, other._coeff], key=len)
        for i, op2 in enumerate(small):
            if i == 0:
                polymul1._coeff = [op2 * x for x in big]
            else:
                polymul1._order = len(polymul1._coeff) - 1
                polymul2._coeff = [0] * i + [op2 * y for y in big]
                polymul2._order = len(polymul2._coeff) - 1
                polymul1 = polymul1 + polymul2
        polymul1._order = len(polymul1._coeff) - 1
        return polymul1

    def polyval(self, x):
        '''Evaluates the function at x
        >>> a = poly([1, 2, 3])
        >>> a.polyval(5)
        86
        '''
        expr = 0
        for i, val in enumerate(self._coeff):
            expr += val * (x ** i)
        return expr

    def differentiate(self, order=1):
        '''Differential of the polynomial
        >>> a = poly([1, 2, 3])
        >>> a.differentiate(2).disp()
        [6]'''
        temp = self._coeff
        for n in range(order):
            polydiff = poly([])
            for i, val in enumerate(temp):
                polydiff._coeff.append(i * val)
            polydiff._coeff = polydiff._coeff[1:]
            polydiff._order = len(polydiff._coeff) - 1
            temp = polydiff._coeff
        return polydiff

    def disp(self):
        '''Print coefficients'''
        return self._coeff


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose='true')
    print('Additional test case')
    a = poly([1, 2, 3, 4])
    b = poly([1, -2, 3])
    c = a + b
    d = b - a
    e = a * b
    f = a.differentiate(2)
    g = a.polyval(5)
    print('a', a.disp())
    print('b', b.disp())
    print('addition', c.disp())
    print('subtraction b-a', d.disp())
    print('multiplication', e.disp())
    print('2nd order derivative of a', f.disp())
    print('polyval of a at 5', g)
