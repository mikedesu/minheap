# minheap

An example minimum-heap implementation written in Python3.

This was a homework project that a student of mine received. We worked on it to completion, earning 100% of the points possible. 

I am provided the source on Github for blogging material and to pad my visible portfolio. Plus, it is a good example of a data structures project.

-----

# Getting started

First, import the `Heap` class to make it available to your project.

```
from heap import Heap
```

To create a new `Heap` object:

```
sizeOfHeap = 10

# heap must be instantiated with a valid maximum capacity
heap = Heap(sizeOfHeap)
```

-----

# Using the Heap object

To add a key-value pair to your heap:

```
heap.push(someKey, someValue)
```

Items will be stored in a list such that they obey the heap ordering property with smallest first / on-top.

To get the smallest key-value and remove it from the heap:

```
poppedValue = heap.pop()
```

To get a list of all the key-value pairs on each "level" of the heap:

```
listOfLevels = heap.levels
```

To check if the heap is empty:

```
if heap.empty:
    # do something
```

