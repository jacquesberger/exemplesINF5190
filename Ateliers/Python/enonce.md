Introduction à Python
=====================

Apprendre un nouveau langage de programmation demande de la pratique. Dans cet
atelier, vous allez vous exercer avec les éléments syntaxiques vus en classe.
Vous allez développer un logiciel simple. Il s'agit d'un énoncé de TP d'un cours
d'initiation à la programmation.

Objectifs
---------

* Manipuler le programme `python3`.
* Écrire du code Python.

Exercice
--------

Vous devez faire un logiciel qui lira un ensemble de commandes d'articles dans
un fichier et qui créera des factures pour les clients concernés à l'aide des
éléments de Python vus en classe :
* fichiers;
* conditions;
* boucles;
* classes;
* listes;
* dictionnaires.

Voici un exemple de fichier d'entrée :
```
0001 RTU43245 3 69.99 FP
0001 RCU83364 1 169.99 F
0001 POP64483 12 1.99 P
0001 KOP77442 100 10.99
0067 RTU43245 35 69.99 FP
0088 RTU43245 13 69.99 FP
0088 UYT11233 5 10.75
```

La première colonne est un numéro de client. La deuxième colonne est un numéro
de produit. La troisième colonne est une quantité. La quatrième colonne est un
prix unitaire. La dernière colonne indique les taxes à calculer sur le produit.

Vous devez produire une facture dans un fichier texte pour chaque client qui
commande des produits. Dans le fichier d'entrée, tous les produits d'un même
client seront toujours consécutifs. Les lettres de la dernière colonne indique
quelles taxes sont applicables sur le produit (F = taxe fédérale;
P = taxe provinciale; FP = les deux taxes; rien signifie que le produit n'est
pas taxé).

Le fichier contenant la facture pour le client 0001 doit se nommer 0001.txt. Le
nom du fichier correspond donc au numéro du client avec l'extension .txt.

Lorsqu'un client achète plus de 100 articles dans une même commande, un rabais
de 15% est appliqué sur le total de la facture.

Voici un exemple de facture à produire :
```
Client numéro 0001

              No de produit  Qte      Prix  Total (tx)
Produit #1    RTU43245         3     69.99      241.41
Produit #2    RCU83364         1    169.99      178.49
Produit #3    POP64483        12      1.99       26.26
Produit #4    KOP77442       100     10.99     1099.00

Total avant rabais : 1545.16
Rabais : 231.77
Total : 1313.39
```
