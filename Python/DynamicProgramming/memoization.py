'''
Created on 27-Jul-2020

@author: dibyajyoti

Illustration of Dynamic Programming memoization concept of caching.
'''

calculation1=0
def fibo1(number):

    global calculation1
    calculation1+=1
    fibo_dict=dict()
    if number < 0:
        return False
    elif(number==1):
        return 0
    elif(number==2):
        return 1
    else:
        return fibo1(number-1)+fibo1(number-2)

print(fibo1(30))
print("calculation we doing without memoization",calculation1)

calculation2=0
memoir=dict()
def fibo(n):
    global calculation2
    global memoir
    calculation2+=1
    if n in memoir.keys():
        return memoir[n]
    else:
        if (n ==1):
            return 0
        elif (n==2):
            return 1
        else:
            memoir[n]=fibo(n-1)+fibo(n-2)
    return memoir[n]

print(fibo(30))
print("calculation we doing with memoization",calculation2)


'''
OUTPUT:

/Users/dibyajyoti/PycharmProjects/DsAlgo/venv/bin/python /Users/dibyajyoti/PycharmProjects/DsAlgo/Fibonacii.py
514229
calculation we doing without memoization 1664079
514229
calculation we doing with memoization 57

Process finished with exit code 0
'''
