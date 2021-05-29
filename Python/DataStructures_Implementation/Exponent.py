
'''Exponent of a number'''
def exponent(m, n):
    if n == 0:
        return 1
    else:
        return exponent(m, n - 1) * m

print(exponent(2, 100))


'''Exponent of a number in an efficient way'''
def exponent_new(m, n):
    if n == 0:
        return 1
    if n%2==0:
        res=exponent_new(m,n/2)
        return res*res
    else:
        return exponent_new(m,n-1)*m

print(exponent_new(2, 100000))