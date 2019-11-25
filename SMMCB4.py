#import numpy
#from matrix import *
#from fraction import *

#Matrices of the form 2*(mn) - the solutions to A(m, n) - can be uniquely determined by the number of occurrences of the numbers 2, 3, ... m-3 in the first row.
#This is because the positions of 1's and m's are fixed, and determining the number of occurrences of m-2-1 numbers uniquely determines the position of the remaining number.
#The program below varies the number of occurrences of 2, 3, ... m-3 in the top row (while satisfying certain constraints) to enumerate all possible cases.

def A_(m, n, a=[]): #a is a list of numbers that have already been added to the top row
    count = 0

    if len(a) == m - 3: #if the positions of m-2-1 numbers (excluding 1 and m) are known, the position of the remaining number can be uniquely determined
        return 1

    #The lower bound in the for loop below is to avoid situations where the same number occurs at the same position in both the top and bottom rows.
    lower_bound =  max(0, 2*len(a)*n-2*sum(a))

    #The upper bound allows atmost 2*n entries of a particular number in the first row, and reduces this bound further when there are fewer slots available in the first row to insert the number.
    upper_bound = min(2*n, (m-2)*n-sum(a))
    
    for x in range(lower_bound ,  upper_bound+1):
        count = count + A_(m, n, a+[x])

    return count


##def poly(m):
##    row = lambda n: numpy.array([Fraction(n**i) for i in range(m-2)])
##
##    M = numpy.array([row(n) for n in range(1, m-1)])
##    a = numpy.array([A(m, n) for n in range(1, m-1)])[:, None]
##
##    c = multiply(inverse(M), a)
##
##    return [str(f) for row in c for f in row]
    
def polynom(m):
    row = lambda n: [n**i for i in range(m-2)]

    M = numpy.array([row(n) for n in range(1, m-1)])
    a = numpy.array([A(m, n) for n in range(1, m-1)])

    c = numpy.linalg.solve(M, a)
    
    return c

def polynomial(ys):
    if ys == []:
        return []
    return ys[0] + polynomial( [(ys[i+1]-ys[i]) for i in range(len(ys)-1)] )

def choose(n, k):
    return [n-i for i in range(k)]//[i+1 for i in range(k)]

def compute(m):
    pm = polynomial([A(m, n) for n in range(m-2)])
    return lambda n: sum([pm[i]*choose(n, i) for i in range(m-2)])

def A(m, n, pd = (0, 0)):
    count = 0
    
    lb, ub = max(0, pd[1] - pd[0] + 2*n), min(2*n, m*n-pd[0])

    print((pd[0]+pd[1])//(2*n), (lb, ub+1), pd)

    for x in range(lb, ub+1):
        count = count + A(m, n, (pd[0] + x, pd[1] + 2*n - x))

    if pd == (m*n, m*n):
        count += 1
        
    return count
