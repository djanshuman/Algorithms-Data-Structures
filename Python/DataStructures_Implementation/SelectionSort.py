'''Implementation of Selection Sort'''

def SelectionSort(list1):

    for i in range(0,len(list1)):
        k=i
        j=i
        for j in range(i, len(list1)):
            if (list1[j]< list1[k]):
                k=j
        temp=list1[i]
        list1[i]=list1[k]
        list1[k]=temp

    return list1

if __name__ == '__main__':
    list1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(SelectionSort(list1))