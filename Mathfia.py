import random

class Player:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)

    def negate(self):
        pass

class Axiom(Player):
    def __init__(self, axm): #name is a signed integer 
        super(Axiom, self).__init__(axm)        

    def negate(self):
        self.name *= -1

class Mathfia(Player):
    def __init__(self, n_axioms, proof = []):

        if proof == []:
            def shuffled(a):
                b = a.copy(); random.shuffle(b); return b
                
            #Creates a proof of length lim (=3), having atleast one negated axiom so that every Mathfia member survives for atleast one round
            proof = shuffled(list(range(-n_axioms, 0)))[:random.choice([1, 2, 3])]
            proof = proof + shuffled([i for i in range(1, n_axioms+1) if -i not in proof])[:3-len(proof)] #lim=3

        super(Mathfia, self).__init__(proof)
        self.proved = False

    def negate(self):
        for i, step in enumerate(self.name):
            self.name[i] *= -1
            
def initialise(n_axioms, n_mathfia):
    plyrs = []

    for i in range(n_axioms):
        plyrs.append(Axiom(i+1))

    for j in range(n_mathfia):
        plyrs.append(Mathfia(n_axioms, []))

    random.shuffle(plyrs)
    
    return plyrs

def disp(players): #displays the arrangement of players
    print('\nThe arrangement of players is')

    for k, player in enumerate(players):
        print(str(k) + ' - ' + str(player))

def positions(players): #returns the positions of all the Axioms and Mathfia members are two separate arrays
    p_axioms, p_mathfia = [], []

    for pos, player in enumerate(players):
        if type(player) == Axiom:
            p_axioms.append(pos)
        elif type(player) == Mathfia:
            p_mathfia.append(pos)

    return p_axioms, p_mathfia

def check(players, p_axioms, p_mathfia): #checks if the game has ended or if a Mathfia has been proved

    def end_game():
        print('\nGame Over.')
        game_ended = True
        exit(0)

    #Inconsistent axiomatic system
    for p in p_axioms:
        for q in p_axioms:
            if players[p].name + players[q].name == 0:
                print("Inconsistent axiomatic system. The Mathfia wins.\n")
                end_game()

    #Negate Mathfia
    current_axioms = set([players[pos].name for pos in p_axioms])
    for p in p_mathfia:
        if set(players[p].name).issubset(current_axioms):
            players[p].proved = True
            print("Mathfia member at position", p, "has been proved. \n")
    
    #Check if all Mathfia members have been proved atleast once
    if sum([players[i].proved==False for i in p_mathfia]) == 0:
        print("All Mathfia theorems have been proved. The Axioms win.\n")
        end_game()
        
def round(players, p_axioms, p_mathfia): 
    mathfia_choice = int(input('\nMATHFIA ')) #position of the person to be negated
    players[mathfia_choice].negate()
    print('OUTCOME Player %d has been negated by the Mathfia.\n' %mathfia_choice)
    check(players, p_axioms, p_mathfia)

    def choice(a, n=1):
        if n == 0:
            return []
        b = a.copy()
        e = random.choice(b)
        b.remove(e)
        return [e] + choice(b, n-1)

    bt_lim = 1
    
    banach_choice = choice(p_axioms, bt_lim) #bt_lim=2
    tarski_choice = choice(p_axioms, bt_lim) #bt_lim=2
        
    for i in range(bt_lim):
        b, t = banach_choice[i], tarski_choice[i]
        if b == t:
            r = random.choice([i for i in range(1, len(p_axioms)+1) if i != players[b].name])
            print("OUTCOME Banach and Tarski have replaced Axiom %d with Axiom %d.\n" %(abs(players[b].name), r))
            players[b].name = r
        else:
            players[b].name, players[t].name = players[t].name, players[b].name;
            print("OUTCOME Banach and Tarski have chosen to switch Axioms %d and %d.\n" %(abs(players[b].name), abs(players[t].name)))

    check(players, p_axioms, p_mathfia)
    
    community_choice = int(input('COMMUNITY '))
    players[community_choice].negate()
    print('OUTCOME Player %d has been negated by the community.\n' %(community_choice))    

    check(players, p_axioms, p_mathfia)

def play():    
    N = int(input('Number of players: '))

    n_axioms = int(input('Number of Axioms: '))
    n_mathfia = int(input('Number of Mathfia members: '))

    global game_ended
    game_ended = False

    players = initialise(n_axioms, n_mathfia)
    p_axioms, p_mathfia = positions(players)

    i = 1
    
    while not game_ended:
        print('\nRound', i)
        disp(players)
        round(players, p_axioms, p_mathfia)
        i += 1

play()
