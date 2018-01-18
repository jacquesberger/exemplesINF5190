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

objet = {"nom": "Berger", "prenom": "Jacques", "age": 87}

print(objet)

# Accéder à un élément
print(objet["nom"])

# Boucler sur les valeurs
for cle, valeur in objet.items():
    print(cle, valeur)

# Supprimer l'âge
del objet["age"]
print(objet)

# Ajouter un élément
objet["vivant"] = False
print(objet)
