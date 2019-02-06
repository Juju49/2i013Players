#!/usr/bin/env python
# -*- coding: utf-8 -*-

#AWELE
import sys
sys.path.append("..")
import game  # @UnresolvedImport

def nouveauPlateau():
    """ void -> plateau
        Retourne un nouveau plateau du jeu
    """
    return [[4, 4, 4, 4, 4, 4],
            [4, 4, 4, 4, 4, 4]]


def getparcoursJoueur(joueur):
    """Int->List[Tuple(Int,Int)]
    Retourne la liste des paires d'indices de cases dans l'ordre du début de la rangée du joueur dont c'est le tour
    """
    IDCJ1 = [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5)]
    IDCJ2 = [(1,5), (1,4), (1,3), (1,2), (1,1), (1,0)]
     
    if joueur == 1:
        return IDCJ1 + IDCJ2
    if joueur == 2:
        return IDCJ2 + IDCJ1
 
def getGrainesJoueur(plateau, joueur):
    """plateau*Int -> Int
        Retourne le nombre de graine du coté du joueur @joueur
    """
    parcours = getparcoursJoueur(joueur)
    nb_graines = 0
    for case in parcours[:6]:
        nb_graines += plateau[case[0]][case[1]]
 
    return nb_graines
         
 
# def startFromCase(parcours, case):
#     """List[Tuple(Int,Int)] * Tuple(Int,Int)->List[Tuple(Int,Int)]
#     Retourne la liste des cases où déposer les graines dans l'ordre de dépose"""
#     idx_case = parcours.index(case)
# 
#     return [ parcours[(12-idx_case+1+i)%11] for i in range(11) ]
# 
# def coupValide(jeu,coup):
#     """jeu*coup -> bool
#         Retourne vrai si le coup est valide dans jeu
#     """
#     val          = False
#     plt          = jeu[0]
#     parcours     = getparcoursJoueur(jeu[1])
#     
#     #déjà, interdiction de s'affamer:
#     if getGrainesJoueur(plt, jeu[1]) == plt[coup[0], coup[1]] and coup == parcours[5]:
#         val = False
# 
#     dispersion   = startFromCase(parcours, coup)
#         
#     #on disperse dans les cases
#     graines_main = plt[coup[0], coup[1]]
#     for i in range(graines_main):
#         case = dispersion[i%11]
#         plt[case[0]][case[1]] += 1
#         graines_main -= 1
# 
#     #on capture les graines adverses
#     for case in parcours[6:].copy().reverse():
#         graine_dans_case = plt[case[0]][case[1]]
#         if ((2 == graine_dans_case or graine_dans_case == 3) and #condition de prise
#         getGrainesJoueur( plt, 1+jeu[1]%2 ) > graine_dans_case): #on vérif que l'opposant ne sera pas affamé
#             
#             jeu[4][jeu[1]-1] += plt[case[0]][case[1]]
#             plt[case[0]][case[1]] = 0 #confiscation!!
#         else:
#             break #on s'arrete si les case de l'adversaire parcourues dans le sens horaire ne sont plus capturable
# 
#     return val
# 
# def joueCoup(jeu,coup):
#     """jeu*coup -> void
#         Joue un coup
#         Hypothese:le coup est valide
#         Met à jour le plateau
#     """
#     plt          = jeu[0]
#     graines_main = plt[coup[0], coup[1]]
#     parcours     = getparcoursJoueur(jeu[1])
# 
#     dispersion   = startFromCase(parcours, coup)
#         
#     #on disperse dans les cases
#     graines_main = plt[coup[0], coup[1]]
#     for i in range(graines_main):
#         case = dispersion[i%11]
#         plt[case[0]][case[1]] += 1
#         graines_main -= 1
# 
#     #on capture les graines adverses
#     for case in parcours[6:].copy().reverse():
#         graine_dans_case = plt[case[0]][case[1]]
#         if ((2 == graine_dans_case or graine_dans_case == 3) and #condition de prise
#         getGrainesJoueur( plt, 1+jeu[1]%2 ) > graine_dans_case): #on vérif que l'opposant ne sera pas affamé
#             
#             jeu[4][jeu[1]-1] += plt[case[0]][case[1]]
#             plt[case[0]][case[1]] = 0 #confiscation!!
#         else:
#             break #on s'arrete si les case de l'adversaire parcourues dans le sens horaire ne sont plus capturable

def finJeu(jeu):
    """ jeu -> bool
        Retourne vrai si c'est la fin du jeu
    """
    return len(game.getCoupsValides(jeu)) == 0

def getGagnant(jeu):
    """jeu->nat
    Retourne le numero du joueur gagnant apres avoir finalise la partie. Retourne 0 si match nul
    """
    plt = jeu[0]
    #on capture ses graines
    jeu[4][0] += getGrainesJoueur( plt, 1 )
    jeu[4][1] += getGrainesJoueur( plt, 2 )
    sj1 = jeu[4][0]
    sj2 = jeu[4][1]

    #on regarde le winner 
    if sj1 > sj2:
        return 1
    if sj2 > sj1:
        return 2
    return 0

def nourrit(jeu, coup):
    j = game.getJoueur(jeu)
    if j == 1 :
        return game.getCaseVal(jeu, *coup) > coup[1]
    return game.getCaseVal(jeu, *coup) > 5 - coup[1]
    
def advAffame(jeu):
    j = game.getJoueur(jeu)
    adv = j % 2+ 1
    return sum(jeu[0][adv-1]) == 0

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

def joueCoup(jeu, coup):
    l, c = distribue(jeu, coup)
    j = game.getJoueur(jeu)
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
