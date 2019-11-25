import random

def choice(C, choice_function=()): #C is a family of non-empty sets indexed by n=len(C)={0, 1, 2, ..., n-1}
    return choice(C[1:], choice_function + (random.choice(C[0]), )) if C else choice_function
