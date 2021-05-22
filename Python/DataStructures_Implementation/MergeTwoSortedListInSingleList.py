'''Two Separate Sorted List are present in a single list, we have to
sort them back to original list using an auxillary array

list1=[2,5,8,12,24,45,99,120,130,3,6,7,10,102,105,150,160]
first list from 2 to 130
second list 3 to 160

'''
def MergeTwoList(list1):
    print("Original List:", list1)
    len_list1 = len(list1)

    i = 0
    j = i + 1

    '''Find starting point of 2nd list from main list which is considered as mid-point, then call SortMerge function 
    to sort into auxillary array then copy back to original array'''
    while (list1[i] < list1[j] and i < len_list1 and j < len_list1):
        i += 1
        j += 1
    SortnMerge(list1,j)

def SortnMerge(list1,mid_point):

    m=mid_point
    i=0
    list3=[]

    while(i<mid_point and m<len(list1)):

        if(list1[i] < list1[m]):
            list3.append(list1[i])
            i+=1
        else:
            list3.append(list1[m])
            m+=1

    '''Validate and insert bigger elements which were left behind while inserting into auxillary list'''
    for p in range(i,mid_point):
        list3.append(list1[p])

    for q in range(m,len(list1)):
        list3.append(list1[q])

    '''Copy into original list from auxillary list'''
    for i in range(0,len(list3)):
        list1[i]=list3[i]

    print("Sorted Original list post copy from auxillary list",list1)

if __name__=="__main__":
    list1=[2,5,8,12,24,45,99,120,130,3,6,7,10,102,105,150,160]
    MergeTwoList(list1)

'''Output

Original List: [2, 5, 8, 12, 24, 45, 99, 120, 130, 3, 6, 7, 10, 102, 105, 150, 160]
Sorted Original list post copy from auxillary list [2, 3, 5, 6, 7, 8, 10, 12, 24, 45, 99, 102, 105, 120, 130, 150, 160]
'''