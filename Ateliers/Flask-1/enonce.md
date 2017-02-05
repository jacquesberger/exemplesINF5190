Introduction à Flask
====================

Flask est le microframework qui sera utilisé durant tout le trimestre. Il y aura
plusieurs ateliers sur ce sujet. Ce premier atelier sert mettre les bases pour
le reste.

Objectifs
---------

* Installer Flask.
* Définir des routes et servir des documents HTML.
* Recevoir les données d'un formulaire.

Exercices
---------

1. Créez une application affichant un formulaire sur sa page d'accueil (route
   `/`). Le formulaire doit permettre des données de différents types :
   * un champ texte (`input type="text"`);
   * un choix entre plusieurs valeurs (`input type="radio"`);
   * une liste déroulante (`select`).

2. Ajoutez une route pour recevoir les données du formulaire. Vous devez valider
   que l'utilisateur a bien remplit la totalité des champs du formulaire. Si les
   données ne sont pas complètes, redirigez l'utilisateur vers une page avec un
   message d'erreur. Si les données sont complètes, redirigez l'utilisateur vers
   une page de remerciement.

3. Lorsque les données du formulaire sont valides, enregistrez-les dans un
   fichier sur le serveur (un log).
