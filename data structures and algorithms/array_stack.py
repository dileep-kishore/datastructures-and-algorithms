# Implementing an Array Stack
class Arraystack:
    ''' An array stack '''
    def __init__(self):
        self._elem = []
    def delete(self):
        ''' Delete the stack '''
        del self._elem
    def __str__(self):
        return str(self._elem)
    def is_empty(self):
        ''' Is stack empty '''
        return len(self._elem) == 0
    def top(self):
        ''' View the top element '''
        if self.is_empty():
            raise IndexError('Stack is empty')
        else:
            return self._elem[-1]
    def push(self, item):
        ''' Add item to stack '''
        self._elem.append(item)
    def pop(self):
        ''' POP the top item of a stack '''
        if self.is_empty():
            raise IndexError('Stack is empty')
        else:
            return self._elem.pop()
    def disp(self):
        ''' Displays the whole stack '''
        return self._elem
