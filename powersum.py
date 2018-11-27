import numpy

choose = lambda n, k: not k if not k else (n+1-k)/k*choose(n, k-1)

def powersum_(p):
    s = numpy.append(numpy.zeros(p), [1, 1])
    for j in range(1, p):
        s = numpy.append(s[:j+2] + powersum(j)*((-1)**(p+1-j))*choose(p, j-1), s[j+2:])
    return s

def powersum(p):
    return powersum_(p)/(p+1)

def listtotext(s):
    p = '' + str(s[0])
    for i in range(1, len(s)):
        p += ' + %.2f n^%d'%(round(s[i], 3), i)
    print(p)

#print(listtotext(powersum(int(input('n: ')))))
    
def printsums(n):
    l = numpy.array([numpy.append(numpy.round(powersum_(i), 3), numpy.zeros(n-i)) for i in range(n)])
    for i in range(1, len(l)):
        s = 'Row %d: ' %(i)
        for j in range(1, len(l[0])):
            if l[i, j] != 0:
                s += format(l[i][j], '<10.3f')
            else:
                s += '          '
        print(s+'\n')
        numpy.savetxt('sumdata.dat', l, fmt = '%10.3f')

