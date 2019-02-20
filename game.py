#!/usr/bin/env python
# -*- coding: utf-8 -*-

# plateau: List[List[nat]]
# liste de listes (lignes du plateau) d'entiers correspondant aux contenus des cases du plateau de jeu

# coup:[nat nat]
# Numero de ligne et numero de colonne de la case correspondante a un coup d'un joueur

# Jeu
# jeu:[plateau nat List[coup] List[coup] List[nat nat]]
# Structure de jeu comportant :
#           - le plateau de jeu
#           - Le joueur a qui c'est le tour de jouer (1 ou 2)
#           - La liste des coups possibles pour le joueur a qui c'est le tour de jouer
#           - La liste des coups joues jusqu'a present dans le jeu
#           - Une paire de scores correspondant au score du joueur 1 et du score du joueur 2

game=None #Contient le module du jeu specifique: awele ou othello
joueur1=None #Contient le module du joueur 1
joueur2=None #Contient le module du joueur 2


#Fonctions minimales 

def getCopieJeu(jeu):
    """ jeu->jeu
        Retourne une copie du jeu passe en parametre
        Quand on copie un jeu on en calcule forcement les coups valides avant
    """
    #import copy
    
    _ = getCoupsValides(jeu)
    #cpy_jeu = copy.deepcopy(jeu)
    cpy_jeu = [ [[e for e in l] for l in jeu[0]], jeu[1], [cv for cv in jeu[2]], [cj for cj in jeu[3]], (jeu[4][0], jeu[4][1])]
    return cpy_jeu

def finJeu(jeu):
    """ jeu -> bool
        Retourne vrai si c'est la fin du jeu
    """
    return game.finJeu(jeu)


def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
        On suppose que la fonction n'est appelee que si il y a au moins un coup valide possible
        et qu'elle retourne obligatoirement un coup valide
    """
    if getJoueur(jeu) == 2:
        cp = joueur2.saisieCoup(getCopieJeu(jeu))
    else:
        cp = joueur1.saisieCoup(getCopieJeu(jeu))

    assert (cp in getCoupsValides(jeu)), "saisieCoup: COUP INVALIDE"
        
    return cp

def getCoupsValides(jeu):
    """ jeu  -> List[coup]
        Retourne la liste des coups valides dans le jeu passe en parametre
        Si None, alors on met à jour la liste des coups valides
    """
    if jeu[2] is not None:
        return jeu[2]

    #on confie la tâche au jeu
    cv = game.coupValides(jeu)  
    jeu[2] = cv
    return cv

def coupValide(jeu,coup):
    """jeu*coup->bool
        Retourne vrai si le coup appartient a la liste de coups valides du jeu
    """
    return coup in getCoupsValides(jeu)

def joueCoup(jeu,coup):
    """jeu*coup->void
        Joue un coup a l'aide de la fonction joueCoup defini dans le module game
        Hypothese:le coup est valide
        Met tous les champs de jeu à jour (sauf coups valides qui est fixée à None)
    """
    game.joueCoup(jeu,coup)

def initialiseJeu():
    """ void -> jeu
        Initialise le jeu List(nouveau plateau, liste des coups joues vide, liste des coups valides None, scores a 0 et joueur = 1)
    """
    return [game.nouveauPlateau(), 1, None, [], (0,0)]

def getGagnant(jeu):
    """jeu->nat
    Retourne le numero du joueur gagnant apres avoir finalise la partie. Retourne 0 si match nul
    """
    return game.getGagnant(jeu)

def affiche(jeu):
    """ jeu->void
        Affiche l'etat du jeu de la maniere suivante :
                 Coup joue = <dernier coup>
                 Scores = <score 1>, <score 2>
                 Plateau :

                         |       0     |     1       |      2     |      ...
                    ------------------------------------------------
                      0  | <Case 0,0>  | <Case 0,1>  | <Case 0,2> |      ...
                    ------------------------------------------------
                      1  | <Case 1,0>  | <Case 1,1>  | <Case 1,2> |      ...
                    ------------------------------------------------
                    ...       ...          ...            ...
                 Joueur <joueur>, a vous de jouer
                    
         Hypothese : le contenu de chaque case ne depasse pas 5 caracteres
    """ 
    def lineBuilder(iterator):
        """ iterator -> str
        retourne une ligne de tableau formatée
        """
        s = ""
        for e in iterator:
            s = "|".join((s, "{:^5}".format(e)))
        s += "\n" + "-" * len(s)
        return s

    plateau = getPlateau(jeu)
    lignes = []
    
    #infos du début
    lignes.append( "\n\nCoup joue = {}\nScores = {}\nPlateau :\n".format(
            getCoupsJoues(jeu)[-1] if getCoupsJoues(jeu) else None, getScores(jeu)) )
    #première ligne
    lignes.append( lineBuilder([" "] + list(range(len(plateau[0]))) ) )
    #toutes les lignes du tableau
    for i in range(len(plateau)):
        lignes.append( lineBuilder([i]+plateau[i]) )

    #on affiche le tout
    print("\n".join(lignes))


# Fonctions utiles

def getPlateau(jeu):
    """ jeu  -> plateau
        Retourne le plateau du jeu passe en parametre
    """
    return jeu[0]

def getCoupsJoues(jeu):
    """ jeu  -> List[coup]
        Retourne la liste des coups joues dans le jeu passe en parametre
    """
    return jeu[3]


def getScores(jeu):
    """ jeu  -> Pair[nat nat]
        Retourne les scores du jeu passe en parametre
    """
    return jeu[4]

def getJoueur(jeu):
    """ jeu  -> nat
        Retourne le joueur a qui c'est le tour de jouer dans le jeu passe en parametre
    """
    return jeu[1]



def changeJoueur(jeu):
    """ jeu  -> void
        Change le joueur a qui c'est le tour de jouer dans le jeu passe en parametre (1 ou 2)
    """
    jeu[1] = 1+jeu[1]%2


def getScore(jeu,joueur):
    """ jeu*nat->int
        Retourne le score du joueur
        Hypothese: le joueur est 1 ou 2
    """
    return jeu[4][joueur-1]

def getCaseVal(jeu, ligne, colonne):
    """ jeu*nat*nat -> nat
        Retourne le contenu de la case ligne,colonne du jeu
        Hypothese: les numeros de ligne et colonne appartiennent bien au plateau  : ligne<=getNbLignes(jeu) and colonne<=getNbColonnes(jeu)
    """
    return getPlateau(jeu)[ligne][colonne]
    
    




