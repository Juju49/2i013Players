#AWELE

import game  # @UnresolvedImport
from builtins import None

def nourrit(jeu, coup):
    j = game.getJoueur(jeu)
    if j == 1 :
        return game.getCaseVal(jeu, *coup) > coup[1]
    return game.getCaseVal(jeu, *coup) > 5 - coup[1]
    
def advAffame(jeu):
    j = game.getJoueur(jeu)
    adv = j % 2+ 1
    return sum(jeu[0][adv-1] == 0)

def coupValides(jeu):
    #règles
    #case dans son camp
    #case non vide
    #devoir de ravitailler l'adversaire si toutes ses cases sont vides
    #(on peut s'affamer soit même)

    j = game.getJoueur(jeu)
    a = advAffame(jeu)
    ret = [(j-1,i) for i in range(6) 
        if game.getCaseVal(jeu, j-1, i) > 0 and ( 
        not a or nourrit(jeu, (j-1, i))
        )]
    return  ret
    

def nextCase(l, c, horraire=False):
    if horraire:
        if c==5 and l==0:
            return (1, c)
        if c==0 and l==1:
            return (0, c)
        if l==0:
            return  (l, c+1)
        return (l, c-1)
    else:
        if c==0 and l==0:
            return (1, c)
        if c==5 and l==1:
            return (0, c)
        if l==0:
            return  (l, c-1)
        return (l, c+1)
    
def distribue(jeu, case):
    v = game.getCaseVal(jeu, *case)
    nc = case
    while v > 0:
        nc = nextCase(*nc)
        if not nc == case:
            jeu[0][nc[0]][nc[1]]+1
            v -= 1
    return nc

def mange():
    pass

def joueCoup(jeu, coup):
    l, c = distribue(jeu, coup)
    j = game.getJoueur(jeu)
    save = game.getCopieJeu(jeu)
    v = game.getCaseVal(jeu, l, c)
    pris = []
    
    while(l == (j % 2 + 1)) and (v == 2 or v == 3):
        jeu[0][j][c] = 0
        pris.append(v)
        jeu[-1][j-1] += v
        l, c = nextCase(l, c, horraire=True)
        v = game.getCaseVal(jeu, l, c)
        
    game.changeJoueur(jeu)
    jeu[2] = None
    jeu[3].append(coup)
    
    for i in range(len(pris)):
        l, c = nextCase(l, c, horraire=True)
        v = pris[-1-i]
        jeu[0][l][c] = v
        jeu[4][j-1] -= v