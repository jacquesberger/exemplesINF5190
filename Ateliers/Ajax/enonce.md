Ajax
====

Le paradigme Ajax est très répandu en développement web. Il permet, entre autre,
d'améliorer significativement la convivialité des applications web.

Dans cet atelier, il n'est pas permis d'utiliser de librairies simplifiant la
gestion des requêtes Ajax. Il faut donc utiliser la fonction fetch.

Objectif
--------

* Mettre en place le paradigme Ajax

Exercice
--------

1. Créez une application affichant une liste de noms et prénoms de personnes.
   Chaque nom et prénom est un élément ayant toutes les apparences d'un lien
   (curseur, couleur et souligné) mais lorsqu'on clique sur un nom, un appel
   Ajax est fait pour obtenir le reste des informations sur la personne en
   question et ces informations sont affichés sur la page directement.

   Les informations à afficher pour chaque individu sont :
   * le nom complet;
   * le sexe de la personne;
   * l'âge de la personne;
   * le pays et la ville de naissance de la personne.

   Évidemment, vous devez créer une base de données contenant ces informations
   et la route Ajax pour obtenir les données d'une personne.
