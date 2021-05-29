'''Fibonacci using loop'''
def fibo(n):

    if n<=1:
        return n
    t0=0
    t1=1
    s=0

    for i in range(2,n+1):
        s=t0+t1
        t0=t1
        t1=s
    return s

print(fibo(1000))


'''Fibonacci using memorization and recursion'''

fibo_array=[-1]*1000
def fibo(n):

    global fibo_array

    if n <=1:
        fibo_array[n]=n
        return n
    else:
        if (fibo_array[n-2]== -1):
            fibo_array[n-2]=fibo(n-2)
        if (fibo_array[n-1]== -1):
            fibo_array[n-1]=fibo(n-1)

        return fibo_array[n-2] + fibo_array[n-1]

print(fibo(1000))
