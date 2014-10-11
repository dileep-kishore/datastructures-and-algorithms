'''QUEUE'''
class Queue:
    '''A queue class'''
    def __init__(self, length):
        self._elem = []
    def delete(self):
        '''Delete queue'''
        del self._elem
    def is_empty(self):
        ''' Is stack empty '''
        return len(self._elem) == 0
    def push(self, item):
        '''Add item to queue'''
        self._elem.append(item)
    def pull(self):
        '''Pull first item out of queue'''
        val = self._elem[0]
        self._elem = self._elem[1:]
        return val
    def disp(self):
        '''Display the contents of the queue'''
        return self._elem

if __name__ == '__main__':
    test_queue = Queue()
    test_queue.push('D')
    test_queue.push('L')
    test_queue.pull()
    test_queue.push('Z')
    print(test_queue.disp())
