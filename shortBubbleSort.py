 # a modify version of bubble sort.
 # this version stops early if it finds that the list has become sorted.

def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                exchanges = True
                alist[i], alist[i+1] = alist[i+1], alist[i]
        passnum -= 1


newlist = [99,65,34,76,23,61,44,3,78,30,10,20]
shortBubbleSort(newlist)
print(newlist)
