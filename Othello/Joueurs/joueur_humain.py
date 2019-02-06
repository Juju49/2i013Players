#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    
    game.affiche(jeu)
    print("coups valides:", game.getCoupsValides(jeu))
    coup_valide = False
    while(not coup_valide):
        print("Saisir coup:")
        x = input("ligne  =")
        y = input("colonne=")
        coup = (x,y)
        coup_valide = game.coupValide(jeu,coup)
        if not coup_valide:
            print("coup invalide! rejouez...")
            
    return coup