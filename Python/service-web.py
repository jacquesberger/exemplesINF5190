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

# Ce programme invoque les services web de l'exemple /Flask/api
# Installer le module requests : pip install --user requests

import requests

# Lire la liste des pays
response = requests.get('http://localhost:5000/api/pays/')
if response.status_code == 200:
    collection = response.json()
    for each in collection:
        print(each['nom'])
else:
    print("Erreur lors de la lecture du service")

# Créer un nouveau pays
nouveau = {'nom': 'Russie'}
post_response = requests.post('http://localhost:5000/api/pays/', json=nouveau)
if post_response.status_code == 201:
    print("Pays créé avec succès")
else:
    print("Erreur avec la création du pays")
