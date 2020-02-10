Enregistrement de mot de passe
==============================

La gestion des mots de passe est une tâche délicate et complexe. La technique
recommandée dans cet atelier est la technique avec le salt et la fonction de
hachage, comme présenté dans cet <a href="https://github.com/jacquesberger/exemplesINF5190/blob/master/auth/insert.py">exemple</a>.

Objectifs
---------

* Enregistrer des mots de passe
* Intégrer cet enregistrement de mot de passe à une application Flask

Exercices
---------

1. Créez une base de données servant à stocker les données d'un compte
   utilisateur :
   * nom;
   * prénom;
   * courriel;
   * date d'inscription;
   * salt;
   * haché du mot de passe.

2. Écrivez une application Flask où la page d'accueil est un formulaire
   d'inscription contenant les champs suivants :
   * nom;
   * prénom;
   * courriel;
   * confirmation du courriel (entrer une deuxième fois le courriel);
   * mot de passe (champ texte de type `password`).

   Note : il n'y a pas de nom d'utilisateur car on utiliserait l'adresse courriel
   comme nom d'utilisateur.

   Lors de la soumission du formulaire, vous devez valider que tous les champs ont
   été remplis, sinon vous affichez un message d'erreur et l'utilisateur doit
   recommencer. Si les données sont valides, vous écrivez les données de
   l'utilisateur dans la base de données. La date d'inscription est générée
   automatiquement selon la date du jour.

3. Ajoutez quelques règles de validation au mot de passe :
   * minimum de 8 caractères;
   * au moins une lettre majuscule et une lettre minuscule;
   * au moins un chiffre
   * au moins un caractère de ponctuation.
