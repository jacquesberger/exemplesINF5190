Utiliser une base de données avec Python
========================================

L'utilisation d'une base de données est un élément incontournable en
développement de logiciels. La grande majorité des applications web en
utilisent. Dans cet atelier, nous allons utiliser la base de données SQLite avec
Python.

Objectifs
---------

* Manipuler une BD SQLite.
* Utiliser la librairie _built-in_ `sqlite3`.

Exercices
---------

1. À partir de la console SQLite, créez une base de données (avec `.read`) en
   utilisant ce [script SQL](https://github.com/jacquesberger/exemplesINF3005/blob/master/SQLite/musique.sql).

2. Écrivez un programme qui va afficher à l'écran la liste numérotée des artistes
   dans la BD. Lorsque l'utilisateur choisit un artiste en particulier (en
   saisissant son numéro au clavier), le programme affiche la liste des albums
   de cet artiste (regardez la fonction `input()` et `int()` pour la saisie
   au clavier).

3. Le fichier [input.txt](input.txt) contient des données sur des albums de
   musique. Chaque ligne correspond à un album, avec 3 champs :
   * le premier champ est le nom de l'artiste;
   * le deuxième champ est le nom de l'album;
   * le troisième champ est l'année de publication de l'album.

   Les champs sont séparés par un `|`.

   Écrivez un programme qui va lire le fichier et ajouter ces albums à la base
   de données. Si l'artiste existe déjà, utilisez l'id de l'artiste existant,
   sinon créez un nouvel artiste (inventez les valeurs que vous ne connaissez
   pas - ex. `est_solo` et `nombre_individus`). Prenez n'importe quel maison
   d'édition pour les albums.
