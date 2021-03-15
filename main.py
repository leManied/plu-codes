#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 16:22:24 2021

@author: damien
"""
import random

# Liste des noms des produits
liste_produits = ["Ail", "Asperge", "Avocat hass mur", "Avocat sac", "Bleuet", 
                  "Brocoli couronne", "Brocoli GR14", "Celeri", "Chou vert", 
                  "Chou-fleur", "Citron", "Concombre sans pépin", 
                  "Concombre Select", "Fraises", "Framboises", "Gingembre", 
                  "Laitue Iceberg", "Laitue Romaine", "Mangue", "Mures", 
                  "Oignon blanc", "Oignon espagnol", "Oignon rouge", 
                  "Oignon vert", "Patate douce", "Poire Bartlett", 
                  "Poivron jaune", "Poivron rouge", "Poivron vert", "Radis", 
                  "Raisin rouge", "Raisin vert", "Rutabaga", 
                  "Tomate rouge de serre", "Tomate rose"]

# Liste des codes PLU
liste_codes = [4608, 4526, 4225, 4227, 13897, 3082, 4060, 4070, 4069, 4079,
               4053, 4593, 4062, 13894, 13895, 4612, 4061, 4640, 4051, 13896, 
               4663, 4093, 4082, 4068, 4816, 4024, 4689, 4688, 4065, 4089, 4023, 
               3498, 4747, 4799, 4807]
#Fonction permettant d'afficher les produits avec leur code lié
def afficher():
    for x in range(35):
        print(f"{liste_produits[x]}, {liste_codes[x]}")

#Fonction qui génère un nombre aléatoire entre 0 et le nombre de produits
def generer_nombre_aleatoire(nombre_de_produit):    
    return random.randint(0, nombre_de_produit-1)
    
#Fonction qui choisi la chaîne de caractère correspondant au nombre aléatoire
def choisir_produit(nombre_aleatoire):
    return liste_produits[nombre_aleatoire]

#Fonction qui choisi le code PLU correspondant au nombre aléatoire
def choisir_code(nombre_aleatoire):
    return liste_codes[nombre_aleatoire]

## Main, le script quoi
nombre_de_produit = len(liste_produits)
fini = False

##Début de la boucle principale
while not fini:
    bonne_reponse = False
    
    # Générer le nombre aléatoire et stocker en mémoire quels sont le code et le produit
    nombre_aleatoire = generer_nombre_aleatoire(nombre_de_produit)
    produit = choisir_produit(nombre_aleatoire)
    code = choisir_code(nombre_aleatoire)
    
    # Converti le code en string pour permettre la comparaison plus tard
    code = str(code)
    
    # Afficher le produit, demandez le code et dire que pour quitter c'est "quitter"
    print("============================")
    print(f"Produit : {produit} \n Quel est le code ?")
    
    print("Si vous souhaitez quitter, écrivez 'quitter'")

    # Début de la boucle secondaire, qui demande à l'infini la réponse tant qu'on a pas une valeur correcte
    while not bonne_reponse:
        reponse = input()
    
        #Si la reponse n'est pas bonne, recommencez, sinon si elle est égale à quitter, quitter, sinon gg
        if reponse == code:
            print(f"Le code {code} est le bon code pour {produit} ! Bravo !")
            bonne_reponse = True
        elif reponse == "quitter":
            bonne_reponse = True
            fini = True
            print("Au revoir !")
        else:
            print(f"Ce n'est pas le bon code pour le produit {produit}. Réessayez !")