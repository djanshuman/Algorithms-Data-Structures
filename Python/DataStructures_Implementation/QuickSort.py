'''Implementation of QuickSort Algo'''


def QuickSort(alist):
    QuickSortHelper(alist, 0, len(alist) - 1)


def QuickSortHelper(alist, first, last):
    if first < last:
        split_partition = Partition(alist, first, last)

        QuickSortHelper(alist, first, split_partition - 1)
        QuickSortHelper(alist, split_partition + 1, last)


def Partition(alist, first, last):
    ele=alist[first]
    left_mark=first+1
    right_mark=last

    Flag = False
    while not Flag:
        while left_mark <= right_mark and alist[left_mark] <= ele:
            left_mark += 1

        while alist[right_mark] >= ele and right_mark >= left_mark:
            right_mark -= 1

        if right_mark < left_mark:
            Flag = True

        else:
            temp = alist[right_mark]
            alist[right_mark] = alist[left_mark]
            alist[left_mark] = temp

    temp = alist[first]
    alist[first] = alist[right_mark]
    alist[right_mark] = temp

    return right_mark

if __name__ == "__main__":
    alist = [100, 1, 30, 42, 77, 23, 5, 55, 9]
    QuickSort(alist)
    print(alist)



