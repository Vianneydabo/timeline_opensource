# timeline_opensource
Timeline open source est un jeu de cartes basé sur le jeu "timeline", adapté à l'hisoire du travail informatique collaboratif. Pour jouer, ouvrir le fichier "timeline_opensource.html".

Les règles du jeu sont simples : 
- Mélanger toutes les cartes et les placer au milieu de la table, la face avec la date vers le bas (cachée)
- Chacun son tour, un joueur pioche une carte, toujours sans regarder la date. Il la positionne ensuite sur la timeline (au milieu de la table), en fonction d'où il pense que l'événement se situe par rapport aux autres. Une fois qu'il l'a positionnée, il peut la retourner.
- Un joueur gagne un point lorsqu'il positionne correctement la carte sur la timeline. S'il s'est trompé, il ne gagne pas de point mais il replace la carte correctement sur la timeline, afin d'avoir une frise cohérente qui se construit petit à petit.
- À la fin, on obtient une frise chronologique de l'histoire de l'opensource, avec les dates et les funfacts correspondant à chaque événement.

## Comment jouer

1. Ouvrez le fichier `timeline_opensource.html` dans votre navigateur
2. Choisissez le nombre de joueurs (2 à 4)
3. Chaque joueur pioche une carte à son tour en cliquant sur la pioche
4. Placez la carte sur la frise chronologique en cliquant sur l'emplacement souhaité
5. Le jeu vérifie automatiquement si le placement est correct
6. Le joueur avec le plus de points à la fin gagne !

## Structure du projet

- `timeline_opensource.html` : le jeu jouable dans le navigateur
- `cartes jeu emergence.pdf` : le PDF des cartes créées sur Canva
- `card_images/` : les images extraites des cartes
- `cards-new.csv` : les données des cartes au format CSV

## Un projet open source sur l'open source

Ce projet est lui-même un exemple concret de travail collaboratif 
open source. Nous utilisons GitHub pour développer ensemble un jeu qui retrace justement cette histoire.

Chaque membre de l'équipe peut proposer des améliorations, signaler des bugs, ou ajouter de nouvelles cartes grâce aux mécanismes de collaboration de GitHub. Le jeu est ainsi en constante évolution, exactement comme les grands projets open source qu'il célèbre.
