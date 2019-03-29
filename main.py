from node import Node
from heap import Heap

def most_common_x(vals, X):
    # step 1 - build the dictionary
    d = {}
    for element in vals:
        # check to see if there is a count for our given element
        # if not, return 0 for default
        count = d.get(element, 0)
        # increment count
        count += 1
        # re-assign new count back to dictionary
        d[element] = count
    # step 2 - build the heap from the dictionary
    d_keys = d.keys()
    heapSize = len(d_keys)
    heap = Heap(heapSize)
    for key in d_keys:
        count = d[key]
        #print(key, ':', count)
        heap.push(count, key)
    # step 3 - grab the leaf nodes and add to our return set
    returnSet = set()
    while len(heap) > X:
        heap.pop()
    while not heap.empty:
        returnSet.add(heap.pop())
    return returnSet

def main():
    r = most_common_x(['a','a','a','b','b','c'],1)
    print(r)

if __name__ == '__main__':
    main()

