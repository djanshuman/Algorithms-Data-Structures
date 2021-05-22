'''Implementation of Merging two Sorted List into a Single new List'''

def MergeTwoSortedList(list1,list2):

    len_list1=len(list1)
    len_list2=len(list2)
    list3=[]
    i=j=0

    while(i<len(list1) and j < len(list2)):
        if(list1[i]<list2[j]):
            list3.append(list1[i])
            i+=1
        else:
            list3.append(list2[j])
            j+=1

    '''Only one for loop will execute as the smaller list had already reach end of list'''
    for k in range(i,len_list1):
        list3.append(list1[k])

    for m in range(j,len_list2):
        list3.append(list2[m])

    print("Merged Sorted List : ",list3)

if __name__=="__main__":
    list1=[2,4,6,10,45,99,102]
    list2=[5,8,13,21,25,88,120,234,400]
    MergeTwoSortedList(list1,list2)

#OUTPUT=>[2, 4, 5, 6, 8, 10, 13, 21, 25, 45, 88, 99, 102, 120, 234, 400]