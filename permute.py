#import listmethods as lm

##def permute(a):
##    b = [[]] if a == [] else []
##    for e in a:
##        b += [[e] + p for p in permute(lm.remelem(a, e))]
##    return sorted(b)

permute = lambda a: [[e] + p for e in a for p in \
                               permute(list(filter(lambda n: n != e, a)))] if a else [a]
