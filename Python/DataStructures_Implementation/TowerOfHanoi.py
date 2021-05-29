

'''Implementation of Tower of Hanoi Problem usin recursion'''

def Toh(n,A,B,C):
    if n==1:
        print("Move "+ str(n) +" Disc from " + A +" to "+ C)

    else:
        Toh(n-1,A,C,B)
        print("Move " + str(n) + " Disc from " + A + " to " + C)
        Toh(n-1,B,A,C)

Toh(3,'A','B','C')