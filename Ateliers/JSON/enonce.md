JSON
====

Le format de sérialisation JSON sera largement utilisé au cours de la session.
Il est important de bien le maîtriser. Cet atelier vise à former l'étudiant à
l'utilisation du JSON.

Objectifs
---------

* Manipuler le format JSON.
* Valider un document JSON.

Exercices
---------

1. À l'aide de [http://jsonlint.com/](http://jsonlint.com/), identifiez et
   corrigez les erreurs dans ce [document](json_avec_erreurs.json).

2. Transformez ce [document](json_sans_erreurs.json) pour que les jours de la
   semaine soient dans un tableau plutôt que des propriétés.

3. Modélisez un document JSON contenant un dossier médical, avec les champs
   suivants :
   * nom;
   * prénom;
   * numéro d'assurance maladie;
   * date de naissance;
   * médecin de famille (nom, prénom, identifiant au collègue des médecins,
     ville de pratique);
   * une liste de visites (pour chaque visite, on conserve la date, le sujet de
     la visite et une description du médecin).

4. Modélisez un document JSON contenant la liste de cours que vous avez suivi.
   Pour chaque cours, on indique :
   * le sigle,
   * le groupe,
   * le trimestre (1 pour hiver, 2 pour été, 3 pour automne),
   * l'année,
   * le nom de l'enseignant,
   * la note lettrée obtenue.

Solutions
---------

* [Exercice #2](Exercice2.json)
* [Exercice #3](Exercice3.json)
* [Exercice #4](Exercice4.json)
