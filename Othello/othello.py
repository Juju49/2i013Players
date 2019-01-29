#!/usr/bin/env python
# -*- coding: utf-8 -*-

def nouveauPlateau():
    """ void -> plateau
        Retourne un nouveau plateau du jeu
    """
    T = 8

    #plateau vide
    p = [[0]*T]*T
    
    #on pose les 4 premières pièces
    p[T/2-1][T/2-1] = 1
    p[T/2][T/2]     = 1
    p[T/2-1][T/2]   = 0
    p[T/2][T/2-1]   = 0
    
    return p

def coupValide(jeu,coup):
    """jeu*coup -> bool
        Retourne vrai si le coup est valide dans jeu
    """
    val = False
    
    return val

def joueCoup(jeu,coup):
    """jeu*coup -> void
        Joue un coup
        Hypothese:le coup est valide
        Met à jour le plateau
    """
    ln, cl = coup
    plt    = jeu[0]

def finJeu(jeu):
    """ jeu -> bool
        Retourne vrai si c'est la fin du jeu
    """
    plt    = jeu[0]

    for ln in plt:
        for e in ln:
            if e == 0:
                return False
    return True

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
