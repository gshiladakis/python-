from numpy.random import unifrom 

def binomial_rv(n, p):
    count = 0
    for i in range(n):
        U = uniform()
        if U < p:
            count = count + 1 # Or count += 1
    return count

binomial_rv(10, 0.5)
