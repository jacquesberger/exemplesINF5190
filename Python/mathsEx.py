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

# Opérations arithmétiques de base
print(5 + 3)
print(5 * 3)
print(5 / 3)
print(5 / 3.0)
print(5 < 3)
print(5 > 3)
print(5 <= 3)
print(5 >= 3)
print(5 == 3)
print(5 == 5)
print(5 != 3)
print((5 + 3) * (4 - 1))

# Utilisation de variables
annee_courante = 2017
annee_naissance = 1967
age = annee_courante - annee_naissance
print("L'âge d'une personne née en 1967 :", age)

# Calcul d'une moyenne
note_etudiant1 = 89
note_etudiant2 = 100
note_etudiant3 = 37
note_etudiant4 = 57
somme_notes = note_etudiant1 + note_etudiant2 + note_etudiant3 + note_etudiant4
moyenne_notes = somme_notes / 4.0
print("La moyenne des notes est de", moyenne_notes, "%")
