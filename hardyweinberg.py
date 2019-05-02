import random

#p = float(input("p: "))
p = 0.98
q = 1 - p

#n = int(input("n: "))
n = 10000

pn = round(2*p*n)
people = ['00']*n
for i in range(n):
    c = random.choice(['01', '10', '11', '11'])
    people[i] = c
    pn -= int(c) % 9
    if pn <= 0:
        break

print(pn)

if pn > 0:
    for i in range(1, n+1):
        person = people[-i]
        if int(person) != '11':
            person == '11'
            pn -= 2 - int(person) % 9
        if pn <= 0:
            break
print(pn)

def cross(a, b):
    return [a[i]+b[j] for i in range(2) for j in range(2)]

def gen():
    return [random.choice(cross(random.choice(people), random.choice(people))) for i in range(n)]

def count(people, details=False):
    pn = 0
    D, H, r = 0, 0, 0
    for person in people:
        pn += int(person) % 9
        if details:
            if person == '11':
                D += 1
            elif person in ['01', '10']:
                H += 1
            else:
                r += 1
    return pn/(2*len(people)), D, H, r if details else pn/(2*len(people))

#for i in range(10):
#    print(count(people, True))
#    people = gen()

        


    
        
