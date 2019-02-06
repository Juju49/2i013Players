#!/usr/bin/env python
# -*- coding: utf-8 -*-

T = 8
MV_DIRS = ((1,0),(0,1),(1,1),(-1,1),(-1,0),(0,-1),(-1,-1),(1,-1))

def nouveauPlateau():
    """ void -> plateau
        Retourne un nouveau plateau du jeu
    """
    
    #plateau vide
    p = [[0]*T]*T
    
    #on pose les 4 premières pièces
    p[T/2-1][T/2-1] = 1
    p[T/2][T/2]     = 1
    p[T/2-1][T/2]   = 2
    p[T/2][T/2-1]   = 2
    
    return p

import game  # @UnresolvedImport

def coupValides(jeu):
    """jeu -> list[coup]
        Retourne vrai si le coup est valide dans jeu
    """
    cv = []
    advers = 1+game.getJoueur(jeu)%2
    plt = jeu[0]
    
    for i in range(T):
        for j in range(T):
            if plt[i][j] == advers:
                for direction in MV_DIRS:
                    x = i
                    y = j
                    while((0 <= x < T) and (0 <= y < T) and (plt[x][y] == advers)):
                        x += direction[0]
                        y += direction[1]
                        if plt[x][y] == 0:
                            cv.append((x,y))
    
    return cv

def joueCoup(jeu,coup):
    """jeu*coup -> void
        Joue un coup
        Hypothese:le coup est valide
        Met à jour le plateau
    """
    ln, cl = coup
    plt    = jeu[0]
    
    j = game.getJoueur(jeu)
    advers = 1+j%2
    plt = jeu[0]
    
    plt[ln][cl] = j
    
    for direction in MV_DIRS:
        x = ln + direction[0]
        y = cl + direction[1]
        while((0 <= x < T) and (0 <= y < T) and (plt[x][y] == advers)):
            plt[x][y] = j
            x += direction[0]
            y += direction[1]

def finJeu(jeu):
    """ jeu -> bool
        Retourne vrai si c'est la fin du jeu
    """
    return len(coupValides(jeu)) == 0

def getGagnant(jeu):
    """jeu->nat
    Retourne le numero du joueur gagnant apres avoir finalise la partie. Retourne 0 si match nul
    """
    #on compte...
    sj1 = 0
    sj2 = 0
    for l in jeu[0]:
        for c in l:
            if c == 1:
                sj1 += 1
            elif c == 2:
                sj2 += 1
                
    jeu[4][0] = sj1
    jeu[4][1] = sj2

    #on regarde le winner 
    if sj1 > sj2:
        return 1
    if sj2 > sj1:
        return 2
    return 0
