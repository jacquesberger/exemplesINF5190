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

une_liste = ["Pascal", "SQL", "PHP", "Python",
             "Ruby", "Groovy", "Java", "Javascript"]

# Boucler sur une liste
for each in une_liste:
    print(each)

print("Taille de la liste :", len(une_liste))

# Générer une liste de valeurs et boucler dessus
for i in range(0, 10):
    print(i)

# Opérateur []
print(une_liste[2])

# Version longue de la boucle
for i in range(0, len(une_liste)):
    print("Élément no. %d : %s" % (i + 1, une_liste[i]))
