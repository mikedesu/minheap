from node import Node

class Heap:
    """
    Class definition is partially completed.
    Method signatures and provided methods may not be edited in any way.
    """
    __slots__ = ('_size', '_capacity', '_data')

    def __init__(self, capacity):
        self._size = 0
        self._capacity = capacity + 1  # additional element space for push
        self._data = [None for _ in range(self._capacity)]

    def __str__(self):
        return ', '.join(str(el) for el in self._data if el is not None)

    __repr__ = __str__

    def __len__(self):  # allows for use of len(my_heap_object)
        return self._size

#    DO NOT MODIFY ANYTHING ABOVE THIS LINE
#    Start of Student Modifications

    def _percolate_up(self):
        i = self._size - 1
        while i/2 > 0:
            child = self._data[i]
            parentIndex = (i-1)//2
            parent = self._data[parentIndex]
            if child is not None and parent is not None:
                if self._data[i] < self._data[parentIndex]:
                    tmp = self._data[parentIndex]
                    self._data[parentIndex] = self._data[i]
                    self._data[i] = tmp 
            i = parentIndex

    def _percolate_down(self):
        i = 0
        while i*2 <= self._size-1:
            mc = self._min_child(i)
            if mc == -1:
                break
            if self._data[i] > self._data[mc]:
                tmp = self._data[i]
                self._data[i] = self._data[mc]
                self._data[mc] = tmp
            i = mc

    def _min_child(self, i):
        if self.empty:
            return -1
        if i*2+1 > self._size:
            return -1
        if self._data[i] is None:
            return -1
        left = i*2+1
        right = i*2+2
        left_val = self._data[left]
        right_val = self._data[right]
        if left_val is None and right_val is None:
            return -1
        if left_val is not None and right_val is None:
            return left
        if left_val is None and right_val is not None:
            return right
        if self._data[left] < self._data[right]:
            return left
        return right

    def push(self, key, val):
        self._data[self._size] = Node(key,val)
        self._size += 1
        self._percolate_up()
        if self._size == self._capacity:
            self.pop()

    def pop(self):
        if self.empty:
            return None
        rv = self._data[0].val
        self._data[0] = self._data[self._size-1]
        self._size -= 1
        self._data[self._size] = None
        self._percolate_down()
        return rv

    @property  # do not remove
    def empty(self):
        if self._size == 0:
            return True
        return False

    @property  # do not remove
    def top(self):
        if self.empty is False:
            return self._data[0].val
        return None

    @property  # do not remove
    def levels(self):
        ourList = []
        if self.empty:
            return ourList
        prevStartIndex = 0
        while prevStartIndex < len(self._data):
            thisLevel = []
            if len(ourList) == 0:
                thisLevel.append(self._data[0])
                prevStartIndex = 0
                ourList.append(thisLevel)
            else:
                startIndex = (prevStartIndex * 2) + 1
                endIndex = startIndex * 2
                j = startIndex 
                while j < len(self._data) and j <= endIndex:
                    node = self._data[j]
                    if node is not None:
                        thisLevel.append(self._data[j])
                    j += 1
                prevStartIndex = startIndex 
                if len(thisLevel) != 0:
                    ourList.append(thisLevel)
        return ourList 

