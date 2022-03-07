# Le confort en avion 

## Description succinte du projet / Informations clés 

**Nom et prénom des membres du projet :** Lucas Guillen, Quentin Henri et Samuel Nonon 

**Nom du projet :** Le confort en avion 

**Modules tiers utilisées :**
- Pandas 
- Matplotlib 

**Objectif du projet :** 

    1. Etudier à travers un tableau statistique le confort des passagers américain en avion. 

    2. Créer une interface graphique pour faciliter la compréhension 
       de ceux qui souhaite travailler sur ce tableau de donnée.

> Nota : Nous avons réuit l'échatillon initiale pour manipuler les données plus facilement. A l'origine il y avait environ 2000 lignes, nous avons garder 100. Nous avons fait de même pour les colonnes. Nous en avons garder une vingtaine sur les quarante initiale. 

##

**Mission des membres impliqués dans le projet :**

*Quentin :* En charge de la recherche du tableau et de la recherche des différents filtres à appliquer. 

*Lucas :* En charge du developpement sur python des filtres donnée précédement. 
(Cette tâche s'est finalement effectuer avec Quentin). 

*Samuel :* En charge de l'interface graphique. 

***

## Description précise du programme / Difficultés rencontrés 

*Le programme présent sur GitHub est l'épicentre de notre projet. Ce code nous a permis de structurer tous nos filtres en python. Ce sont des lignes de codes assez répétitives. Elle permettent cependant de mieux comprendre les données du tableau.* 

### Détail précis d'une fonction

    1. On appelle le tableau depuis l'endroit où il est enregistré 
    
    2. A partir d'une colonne, on selectionne certains mots clés présents dans celle-ci. 
       Par exemple pour la colonne "Fréquence utilisation avion"on choisi de prendre 
       seulement les personnes qui voyagent une fois ou moins souvent dans l'année 
       "Once a year or less".
       
    3. On renomme notre masque de départ pour pouvoir l'exploiter avec une autre colonne 
    
    4. A partir du nouveau nom donné à notre filtre, 
       on l'ajoute à une autre colonne et on demande à python de faire soit : 
       Un graphique circulaire, une moyenne, un historiogramme, etc...
    5. On renvoie une phrase pour donner le résultat 
       (cette phrase est normalement provisoire, en attente de l'interface graphique)

##


### Présentation des filtres (pramètres d'entrées) : 

> Nota : Nous travaillons sur 5 fréquence différentes : Never / Once a year or less /  Once a month or less / A few times per week 
> / Every day
> 
> Quand la mention (fréquence) apparait, cela signifie que nous avons traité les 5 possibilités qui s'offraient à nous

*Pour chaque filtres effectuer nous cherchons à savoir si il existe des corrélation ou des causalité entre les différentes variables misent en commun*

- Filtre "Age" en fonction de la "fréquence d'utilisation de l'avion"
  - On souhaite connaitre quelle tranche d'age est la plus susceptible de prendre l'avion 

- Filtre "Revenue du menage" en fonction de la "fréquence d'utilisation de l'avion" 
  - On souhaite connaitre quelle est le revenue moyen de ceux qui emprunte (fréquence) l'avion  

- Filtre "Diplôme" en fonction de la "fréquence d'utilisation de l'avion" 
  - On souhaite connaitre quelle est le diplome de ceux qui emprunte (fréquence) l'avion 

- Filtre "Emplacement (region de recensement)" en fonction de la "fréquence d'utilisation de l'avion" 
  - On souhaite connaitre l'emplacement moyen de ceux qui emprunte (fréquence) l'avion

- Filtre "Age" en fonction de "l'utilisation ou non d'un appareil éléctronique lors des phases critiques de vol"
  - On souhaite connaitre la moyenne d'age des personnes qui ne respectent pas les consignes de sécurité lors d'un vol 

- Filtre "Emplacement (region de recensement)" en fonction de "l'utilisation ou non d'un appareil éléctronique lors des phases critiques de vol"
  - On souhaite connaitre l'emplacement moyen des personnes qui ne respectent pas les consignes de sécurité lors d'un vol

- Filtre "Revenue du ménage" en fonction de "l'utilisation ou non d'un appareil éléctronique lors des phases critiques de vol"
  - On souhaite connaitre le revenue moyen des personnes qui ne respectent pas les consignes de sécurité lors d'un vol

- Filtre "Revenue du menage" en fonction de "Qui devrait avoir le contrôle du hublot ?" 
  - On souhaite savoir si l'argent peut avoir un impact sur les décisions des passagers durant un vol.

- Filtre "Revenue du menage" en fonction de "Est-il imprudent de s'installer sur un siège invendus en avion" 
  - On souhaite savoir si l'argent peut avoir un impact sur les décisions des passagers durant un vol.

- Filtre "Quelle taille mesurez-vous ?" en fonction de "Est-il impoli d'incliner son siège en avion" 
  - On souhaite savoir si la taille a un impactla compréhension des passagers par rapport à une personne qui inclinerait fortement son siège 

- Filtre "Emplacement(region de recensement)"  en fonction "Est-il impoli de parler dans une conversation à l"tranger assis à coté de vous" 
  - On souhaite savoir si la région d'origine du passager à un impact sur son humeur et sur son caractère de sociabilité 

- Filtre "Age" en fonction "En general, est-il impoli d'amener un bébé en avion" 
  - On souhaite savoir si l'age des passagers à un impact sur la compréhension d'amener un enfant en avion.

##

### Difficultés rencontrées lors du projet : 

Il y a eu un manque de coordination entre les différents membres du groupe, ce qui a malheuresement mis de côté une partie du travail. Il y a eu quelques difficultés sur le code python au départ mais désormais tout les légers bugs sont corrigés. Il ne reste que l'interface graphique à faire. 

*Auteurs :* Lucas Guillen et Quentin Henri 1-01 

    



