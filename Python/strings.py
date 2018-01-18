# Copyright 2017 Jacques Berger
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Délimiteurs de chaîne
print("Chaîne avec des caractères accentués")
print('Chaîne avec des caractères accentués')
print("J'aime les fruits.")
print('Ces élus sont "compétents", parfois!')

# Plusieurs paramètres au print (affichés avec un espace entre chacun)
nombre_pommes = 5
print("J'ai mangé", nombre_pommes, "pommes pour souper hier.")

# Formattage
print("J'ai mangé %d pommes pour souper hier." % nombre_pommes)

nombre_poires = 2
nombre_oranges = 7
phrase = ("J'ai mangé %d pommes, %d poires "
          "et %d oranges pour déjeuner ce matin.")
print(phrase % (nombre_pommes, nombre_poires, nombre_oranges))

# Multi-lignes
longue_chaine = """
Une petite anecdote que j'ai vécue lorsque j'ai terminé mon cégep et qui me
fait toujours rire, même aujourd'hui.

En 2003, le marché du développement de logiciels n'était pas aussi
intéressant qu'aujourd'hui à Montréal. À l'époque, il y avait plus d'offre
que de demande et les emplois étaient plus rares. Du moins, les bons emplois
étaient plus rares.

Fraîchement sorti du cégep avec mon DEC en informatique de gestion en poche,
je me suis lancé dans la recherche d'un emploi à Montréal. Durant les
premiers mois de ma recherche d'emploi, j'ai passé plusieurs entrevues
dans diverses entreprises. L'une de ces entrevues m'a frappé plus que les
autres.

Il s'agissait d'un poste bien peu intéressant, pour une entreprise qui
développait un logiciel comptable. La tâche principal de ce poste était de
prendre un formulaire papier du gouvernement et d'écrire un document HTML qui
reproduit le plus fidèlement possible le formulaire papier original. En
gros, du HTML et du CSS assez élémentaire. L'entreprise offrait 25,000$ par
année pour ce poste et exigeait à l'employé d'être présent au bureau au
moins 38 heures par semaine.

Le plus étonnant dans tout ça, ce n'est pas le faible salaire ou les tâches
peu intéressantes, c'est définitivement la méthode de recrutement de
l'entreprise. Mon entrevue a durée près de deux heures. J'ai eu droit à une
entrevue complète en français et en anglais, à un test technique sur le HTML
et finalement à un test de personnalité. Finalement, le recruteur m'a confié
qu'il devait rencontrer 25 candidats au total pour ce poste.

Évidemment, je n'ai pas eu l'emploi. Par contre, encore aujourd'hui, je
suis étonné par cette expérience. Une entrevue de 2 heures, bilingue, avec
test technique et test de personnalité, multipliée par 25 candidats, pour
un poste d'HTML élémentaire! Les coûts de recrutement de cette entreprise
doivent être incroyables.
"""
print(longue_chaine)

# Longueur d'une chaîne
print("Longueur de ce texte :", len(longue_chaine))
