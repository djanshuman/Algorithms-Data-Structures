
'''Factorial of a number'''
def facto(n):
    if n==0:
        return 1
    return facto(n-1)*n

print(facto(997))



'''Factorial of a number using memorization of optimization'''
def facto(n,k):
    if n==0:
        return k

    return facto(n-1,k*n)

print(facto(997,1))
