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

from os.path import exists

# Afficher le contenu d'un fichier à la console
text_file = open("input/input1")
print(text_file.read())
text_file.close()

# Lire une seule ligne d'un fichier
fichiers_prenoms_masculins = open("input/input2")
une_ligne = fichiers_prenoms_masculins.readline()
print(une_ligne)
fichiers_prenoms_masculins.close()

# Créer un fichier et y écrire des données
output = open("result.txt", "w")
resto_prefere = "Chez Chose"
phrase = "J'adore le restaurant %s." % resto_prefere
output.write(phrase)
output.close()

# Vérifier si un fichier existe
print(exists("input/input1"))
print(exists("input/input1000"))
