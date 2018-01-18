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

import random

print("Nouvelle partie de HILO")
mystery_number = random.randint(1, 100)

tries = 10
found = False
while tries > 0 and found is False:
    print("Entrez un nombre entre 1 et 100")
    user_number = int(input())
    if user_number < mystery_number:
        print("Plus haut!")
    elif user_number > mystery_number:
        print("Plus bas!")
    else:
        found = True
    tries = tries - 1

if found is True:
    print("Vous avez gagné!")
else:
    print("Vous avez perdu!")
