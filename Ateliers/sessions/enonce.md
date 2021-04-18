Sessions
========

Les sessions sont un concept commun et très utile en développement web. Une
session est un espace de stockage sur le serveur propre à chaque utilisateur
authentifié.

Objectifs
---------

* Mettre en place une autre forme d'authentification.
* Utiliser des sessions.

Exercices
---------

1. Vous devez mettre en place une authentification [Google Sign-In](https://developers.google.com/identity/sign-in/web/sign-in)
   sur votre logiciel. L'authentification doit permettre de créer une session au
   niveau du serveur.

2. Mettez en place un mécanisme de déconnexion pour un utilisateur connecté. Ce
   ménanisme doit également supprimer la session.

3. Vous devez mettre en place une fonctionnalité permettant à une personne
   connecté de s'enregistrer dans une liste d'attente pour adopter un animal de
   compagnie.

   Voici les exigences :

   * Le formulaire doit avoir 3 pages.
   * Sur la page 1, l'utilisateur doit saisir son nom, son prénom et sa ville.
   * Sur la page 2, l'utilisateur doit confirmer son adresse courriel. On lui
     affiche l'adresse que Google nous a donné lors de l'authentification et
     l'utilisateur doit cocher une case de confirmation avant de pouvoir
     continuer à l'étape suivante.
   * Sur la page 3, l'utilisateur doit indiquer le type d'animal qu'il désire
     adopter (provenant d'une liste déroulante) et le nombre d'enfants qui
     vivent dans le foyer de la personne (encore une liste déroulante).
   * L'application offre un menu pour naviguer dans le processus. Au début,
     l'utilisateur ne peut aller qu'à la première étape. Les autres étapes ne
     sont pas accessibles. Une fois la première étape complétée, la deuxième
     étape est débloquée et ainsi de suite.
   * Il est toujours possible de cliquer sur une étape précédente afin de
     modifier ses réponses.
   * Les données du formulaire doivent être stockées dans la session jusqu'à la
     soumission finale du formulaire à la page 3. Donc, lorsqu'on affiche les
     étapes 1 et 2, on doit d'abord vérifier s'il existe des données dans la
     session. Si oui, on affiche ces données.
   * Quand l'utilisateur termine l'étape 3, l'enregistrement est écrit dans la
     base de données.
   * Si une personne ferme sa session sans soumettre la troisième étape, elle
     perd ses données.
