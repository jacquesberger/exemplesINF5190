# coding: utf8

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

import sqlite3

connection = sqlite3.connect('musique.db')
cursor = connection.cursor()
cursor.execute(("insert into artiste(nom, est_solo, nombre_individus) "
                "values('Brain Surgery', 0, 7)"))

cursor.execute("select last_insert_rowid()")
lastId = cursor.fetchone()[0]
connection.commit()

cursor.execute("update artiste set nom = 'Unstoppable' where id = %d" % lastId)
connection.commit()

cursor.execute("select nom from artiste")
for row in cursor:
    print(row[0])

connection.close()
