'''Program to Implement Bubble sort

No of passes= n-1, No of comparision =O(n^2), No of Swaps= O(n^2)
Min complexity =O(n) [For an already sorted list]
Max complexity is O(n^2)'''

def BubbleSort(list1):

    n=len(list1)
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if list1[j]>list1[j+1]:
                swap(j,j+1)
    return list1

def swap(pos1,pos2):
    temp = list1[pos1]
    list1[pos1] = list1[pos2]
    list1[pos2] = temp

list1=[4,10,3,1,8]
print(BubbleSort(list1))