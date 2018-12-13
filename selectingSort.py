'''
the selecting sort improves from the bubble sort by making only one exchange
for every pass through the list
'''

def selectingSort(alist):
    for fillslot in range(len(alist)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp



newList = [99,65,34,76,23,61,44,3,78,30,10,20]
selectingSort(newList)
print(newList)
