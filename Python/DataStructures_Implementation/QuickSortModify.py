'''Implementation of Quick sort using for loop'''

def Quicksort(alist, start, end):

    if start < end:
        split_partition = Partition(alist, start, end)

        Quicksort(alist, start, split_partition - 1)
        Quicksort(alist, split_partition + 1, end)

def Partition(alist, start, end):
    pivot = alist[end]
    pindex = start

    for i in range(start, end + 1):
        if alist[i] < pivot:
            temp = alist[i]
            alist[i] = alist[pindex]
            alist[pindex] = temp
            pindex += 1
    temp = alist[end]
    alist[end] = alist[pindex]
    alist[pindex] = temp

    return pindex

if __name__=="__main__":
    alist = [2, 7, 1, 6, 3, 100, 44, 4]
    Quicksort(alist, 0, len(alist) - 1)
    print(alist)



'''Implementation Using Swap function'''


def Quicksort(alist, start, end):
    if start < end:
        split_partition = Partition(alist, start, end)

        Quicksort(alist, start, split_partition - 1)
        Quicksort(alist, split_partition + 1, end)

def Partition(alist, start, end):
    pivot = alist[end]
    pindex = start

    for i in range(start, end + 1):
        if alist[i] < pivot:
            Swap(alist, pindex, i)
            pindex += 1

    Swap(alist, end, pindex)
    return pindex


def Swap(alist, pos1, pos2):
    temp = alist[pos1]
    alist[pos1] = alist[pos2]
    alist[pos2] = temp


alist = [100, 1, 5, 6, 99, 42, 2]
Quicksort(alist, 0, len(alist) - 1)
print(alist)


'''Implementation Using Randomized QuickSort'''

import random
def Quicksort(alist, start, end):
    if start < end:
        split_partition = RandomizedPartition(alist, start, end)

        Quicksort(alist, start, split_partition - 1)
        Quicksort(alist, split_partition + 1, end)

def RandomizedPartition(alist, start, end):

    '''Randomized logic'''
    pindex=random.randrange(start,end)
    Swap(alist,pindex,end)
    '''logic end'''

    pivot = alist[end]
    pindex = start

    for i in range(start, end + 1):
        if alist[i] < pivot:
            Swap(alist, pindex, i)
            pindex += 1

    Swap(alist, end, pindex)
    return pindex


def Swap(alist, pos1, pos2):
    temp = alist[pos1]
    alist[pos1] = alist[pos2]
    alist[pos2] = temp


alist = [100, 1, 5, 6, 99, 42, 2]
Quicksort(alist, 0, len(alist) - 1)
print(alist)