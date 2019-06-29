from hardyweinberg import *

for i in range(100):
    print(count(people, True))
    people = gen()
    people = [person for person in people if person != '00']

    H = count(people, True)[2]
    people = people[int(H/19):]
    
    


