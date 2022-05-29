# Jeu de la vie  

## Description succinte du projet / Informations clés 

**Noms et prénoms des membres du projet :** Lucas Guillen, Quentin Henri 

**Nom du projet :** Jeu de la vie 

**Modules tiers utilisés :**
- Pygame 
- PyQt5 
- Os 
- Random 
- Json 
- Time 
- Threading
- Sys

**Objectif du projet :** 

    1. Comprendre le fonctionnement des règles du jeu de la vie et s'approprier les fonctions conçu à l'avance. 

    2. Créer une animation à l'aide de fonction pré-établi et des règles du jeu de la vie. 

##

**Mission des membres impliqués dans le projet :**

*Quentin :* En charge de la recherche des images à coder / Codage des figures / Implémentation de la musique dans les différentes fonctions.

*Lucas :* En charge du codage des figures / Résolution des différents bugs / Réalisation du rendu final (en accord avec le rythme de la musique). 

***

## Description précise du programme / Difficultés rencontrées 

*Les fichiers présents sur GitHub représente l'ensemble de notre travail. Pour une meilleur compréhension, nous avons décidé de ranger les fichiers en deux catgéorie : *

    1- Figures codés : Fichiers avec le codage des figures présentés. 
    2- Fonctions nécessaires : Fichiers avec le codage des fonctions principales et complémentaires. 

### Détail précis des modifications des différents fichiers 

    1. jdlv_model.py : Aucun ajout. 
##
    2. jdlv_qrc.py : Aucun ajout.
##
    3. jdlv.qrc : Aucun ajout.
##
    4. jdlv_ui : Aucun ajout.
## 
    5. jdlv_rc.py : Aucun ajout.
##
    6. jdlv_other_functions.py : Aucun ajout. 
##
    7. jdlv_main.py : Aucun ajout. 
##
    8. jdlv_vue_fromUi.py : Aucun ajout.
##
    9. jdlv_my_tools.py : 
- Import des différents fichiers comprenant les images codés. 
- Ajout de 5 fonctions permenttant d'animer le projet sur la grille PyQt5. 

##
    10. jdlv_vue.py : Aucun ajout. 
##
    11. jdlv_data.py :
- Ajout des différentes couleurs necessaires à la reproduction des figures présentées

##
    12. jdlv_outil.py : 

- Remplacement de la couleur "red" dans la fonction revive_case (case) par "grey"
    
- Ajout de la fonction play_music () ainsi que du module Pygame. Cette fonction permet d'initiliser la musique qui sera ensuite traité dans le fichier jdlv_controleur.py 

##

    13. jdlv_controleur.py : 

- Ajout de la fonction play_music () dans la fonction action_pb_play_pause_clicked aisni que du module pygame (pygame.mixer.music.play) qui permet de jouer la musique quand on clique sur le bouton play. 

- Changement de la variable apply_game_or_life_rules par scene_1 dans la fonction action_pb_play_pause_clicked. 

##
    14. plan_planisphere_individuel.py : Fichier avec les 14 fonctions correspondant aux 14 parties du monde. 
##
    15. plan_planisphere_global : Fichier avec la fonction permettant d'afficher le planisphere global. 
##
    16. plan_france_individuel : Fichier avec les 7 fonctions correspondant aux 7 parties de la France. 
##
    17. plan_france_global : Fichier avec la fonction permettant d'afficher la France en entier 
##
    18. plan_moto_position1 : Fichier avec la focntion correspondant à la moto avec la fumée collé au pot d'échappement 
##
    19. plan_moto_position2 : Fichier avec la focntion correspondant à la moto avec la fumée détachée du pot d'échappement
##
    20. plan_moto_position3 : Fichier avec la focntion correspondant à la moto sans fumée derrière le pot d'échappement
##
    21. plan_arc_de_triomphe : Fichier avec la fonction permettant d'afficher l'arc de triomphe 

### Détail précis des fonctions 

## Fonctions permettant de coder les images
grid = clean_grid (grid)
--> Permet d'effacer la figure précédente et de commencer sur une grille vierge sans passer par la fonction clean_grid (grid) 

cases [i + 4] [j + 39] ['s'] = life_status
cases [i + 4] [j + 39] ['c'] = color
--> Les deux lignes permettent de coder le pixel en fonction de ses coordonnées sur l'axe horizontal et vertical. Elles permettent également d'indiquer la couleur de la case. 


### Difficultés rencontrées lors du projet : 

Le codage des différentes figures s'est avéré très chronophage. Nosu avons du redimensionner nos ambition au corus de notre projet. Notre idée initiale étant trop complexe à réaliser, nous avons choisi de présenter nos différents monuments puis de mettre en place le jeu de la vie. 

*Auteurs :* Lucas Guillen et Quentin Henri 1-01 

    



