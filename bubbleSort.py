# bubbleSort.py

import sorting

'''
Algorithmic efficiency:
Time:
  Average case: O(n**2)
  Worst case:   O(n**2)
  Best case:    O(n)
Auxiliary Space:
  Worst case:   O(1)
'''

def bubble():
    """ Bubble Sort algorithm. """
    data = sorting.start()

    # Elements after last swap are already sorted.
    n = len(data)-1
    while n != 0:
        sorting.iteration()
        last_swap = 0
        for i in range(n):
            if data[i] > data[i+1]:
                sorting.swap(i,i+1)
                last_swap = i
        n = last_swap
        
    sorting.end()

    return data



