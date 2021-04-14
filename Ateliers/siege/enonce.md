Tests de charge avec siege
==========================

Les tests de charge sont un élément important de l'exploitation d'une
application web. Ils servent à découvrir les limites de notre logiciel et de
notre architecture de déploiement.

Note : En temps normal, les tests de charge doivent être faits sur une
application déployée sur un serveur. Pour les besoins de l'exercice, les tests
de charge durant l'atelier seront faits sur votre ordinateur.


Objectifs
---------

* Faire des tests de charge.
* Utiliser [siege](https://www.joedog.org/siege-home/).


Exercices
---------

1. Lancez un test de charge sur la page d'accueil de votre TP1 durant une
   minute.

2. Lancez un test de charge sur toutes les pages de votre TP1 durant 5 minutes.

3. À partir de la liste d'URL de l'exercice #2, trouvez la capacité maximale de
   connexions simultanées que votre TP1 arrive à gérer sans perte de service.

4. Une fois la limite trouvée (exercice #3), essayez d'évaluer si votre TP1 peut
   supporter une telle charge pendant 30 minutes sans perte de qualité de
   service.
