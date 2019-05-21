#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
import game  # @UnresolvedImport

T = 3
MV_DIRS = ((1,0),(0,1),(1,1),(-1,1),(-1,0),(0,-1),(-1,-1),(1,-1))

def nouveauPlateau():
    """ int -> plateau
        Retourne un nouveau plateau du jeu
    """ 
    #plateau vide
    p = [[0]*T for _ in range(T)]
    
    return p

def calcScore(jeu):
    sj1 = 0
    sj2 = 0
    for l in jeu[0]:
        for c in l:
            if c == 1:
                sj1 += 1
            elif c == 2:
                sj2 += 1
                
    jeu[4] = (sj1, sj2)
    return sj1, sj2

def coupValides(jeu):
    """jeu -> list[coup]
        Retourne vrai si le coup est valide dans jeu
    """
    cv = set()
    plt = game.getPlateau(jeu)
    
    for i in range(T):
        for j in range(T):
            if plt[i][j] == 0:
                cv.add((i,j))
    
    return list(cv)

def joueCoup(jeu,coup):
    """jeu*coup -> void
        Joue un coup
        Hypothese:le coup est valide
        Met à jour le plateau
    """
    ln, cl = coup
    plt = jeu[0]
    
    joueur = game.getJoueur(jeu)

    plt[ln][cl] = joueur
    
    _ = calcScore(jeu)
    
    game.changeJoueur(jeu)
    jeu[2] = None
    game.getCoupsJoues(jeu).append(coup)


def finJeu(jeu):
    """ jeu -> bool
        Retourne vrai si c'est la fin du jeu
    """
    
    plt = jeu[0]
    return getGagnant(jeu) != 0 and sum(sum(i) for i in plt) > T*T

def getGagnant(jeu):
    """jeu->nat
    Retourne le numero du joueur gagnant apres avoir finalise la partie. Retourne 0 si match nul
    """
    plt = jeu[0]
    winner = 0
    
    def rechercheGagnantPoint(ln, cl):
        gagnant = 0
        nb_alignes = 0
        
        for direction in MV_DIRS:
            #on cherche les directions où retourner les pions
            x = ln + direction[0]
            y = cl + direction[1]
            while(0 <= x < T and 0 <= y < T):
                #on regarde si il y en a 3 de suite du même joueur
                if gagnant == plt[x][y]:
                    nb_alignes += 1
                else:
                    gagnant = plt[x][y]
                    
                x += direction[0]
                y += direction[1]
                if (nb_alignes == 3 and gagnant != 0):
                    #si c'est aps du vide mais bien un joueur, on a fini 
                    return gagnant
    
    
    for ln in range(T):
        for cl in range(T):
            winner = rechercheGagnantPoint(ln, cl)
    
    return winner
