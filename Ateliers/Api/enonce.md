API
===

Cet atelier couvre la mise en place d'un API RESTful pour manipuler un catalogue
de livres. Lorsqu'un service retourne des données, c'est toujours en format
JSON. Lorsqu'un service reçoit des données, c'est toujours en format JSON
également.

Testez vos services à l'aide d'un client REST.

Objectifs
---------

* Manipuler du JSON
* Créer des services web REST/JSON
* Manipuler un client REST

Exercices
---------

1. Créez une base de données contenant une table modélisant des livres. Les
   données d'un livre sont :
   * l'id du livre;
   * le titre;
   * l'auteur (un seul auteur par livre);
   * l'année de publication
   * le nombre de pages;
   * le nombre de chapitres.

2. Créez une application Flask avec une route `GET` à l'URL `/api/livres/` qui
   retourne la liste de tous les livres (l'id et le titre seulement).

3. Créez une route `GET` à l'URL `/api/livre/<id>` qui retourne toutes les
   données d'un livre.

4. Créez une route `POST` à l'URL `/api/livre` qui sert à créer un nouveau
   livre. La route doit recevoir un objet JSON contenant toutes les données du
   livre, sauf l'id.

5. Créez une route `DELETE` à l'URL `/api/livre/<id>` qui sert à supprimer un
   livre.
