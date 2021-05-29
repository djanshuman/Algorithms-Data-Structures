
'''Exponent of a number'''
def exponent(m, n):
    if n == 0:
        return 1
    else:
        return exponent(m, n - 1) * m


print(exponent(2, 5))