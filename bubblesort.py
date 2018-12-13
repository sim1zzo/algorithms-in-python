'''
the babble sort makes multiple passes throught the list.
It compares adjacent items and exchanges those that are out of ored.
'''

def bubblesort(alist):
    for passum in range(len(alist)-1, 0, -1):
        for i in range(passum):
            if alist[i] > alist[i+1]:
                # swapping vatialbles
                alist[i], alist[i+1] = alist[i+1], alist[i]


newlist = [1,34,54,23,65,23,76,98,23,76,12,89,66]
bubblesort(newlist)
print(newlist)


'''
bubble sort is often considered the most inefficient sorting method sice it much
exchange items before the final location is knows. These "wasted" exchange
operations are very costly
'''
