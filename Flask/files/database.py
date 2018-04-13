# Copyright 2018 Jacques Berger
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


class Database:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db/profiles.db')
        return self.connection

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()

    def create_profile(self, firstname, lastname, pic_id):
        connection = self.get_connection()
        connection.execute(("insert into profiles(fname, lname, pic_id)"
                            " values(?, ?, ?)"), (firstname, lastname, pic_id))
        connection.commit()

    def create_picture(self, pic_id, file_data):
        connection = self.get_connection()
        connection.execute("insert into pictures(id, data) values(?, ?)", [pic_id, sqlite3.Binary(file_data.read())])
        connection.commit()

    def load_picture(self, pic_id):
        cursor = self.get_connection().cursor()
        cursor.execute(("select data from pictures where id=?"), (pic_id,))
        picture = cursor.fetchone()
        if picture is None:
            return None
        else:
            blob_data = picture[0]
            return blob_data
    
    def get_profiles(self):
        cursor = self.get_connection().cursor()
        cursor.execute("select fname, lname, pic_id from profiles")
        profiles = cursor.fetchall()
        return [{"prenom": profile[0], "nom": profile[1], "photo": profile[2]} for profile in profiles]
