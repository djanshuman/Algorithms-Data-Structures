'''Implementation of Merge Sort'''

def MergeSort(alist):

    print("splitting list",alist)
    if(len(alist)>1):
        mid=len(alist)//2
        left_half=alist[:mid]
        right_half=alist[mid:]
        MergeSort(left_half)
        MergeSort(right_half)

        i=0
        j=0
        k=0

        while(i < len(left_half) and j < len(right_half)):
            if left_half[i] < right_half[j]:
                alist[k]=left_half[i]
                i+=1
            else:
                alist[k]=right_half[j]
                j+=1
            k+=1

        while i < len(left_half):
            alist[k]=left_half[i]
            i+=1
            k+=1
        while j < len(right_half):
            alist[k]=right_half[j]
            j+=1
            k+=1

    print("Merging",alist)

alist=[100, 45, 99, 120, 130, 3]
MergeSort(alist)
print(alist)