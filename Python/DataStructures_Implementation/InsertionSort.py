'''Implementation of Insertion Sort'''

def InsertionSort(list1):

    for i in range(1,len(list1)):
        element=list1[i]
        pos=i

        while(pos > 0 and list1[pos-1] > element):
            list1[pos]=list1[pos-1]
            pos=pos-1
        list1[pos]=element
    return list1

if __name__ == '__main__':
    list1 = [10, 2, 3, 8, 12, 99, 19, 5]
    print(InsertionSort(list1))