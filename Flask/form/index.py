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

from flask import Flask
from flask import render_template
from flask import redirect
from flask import request

app = Flask(__name__)


@app.route('/')
def formulaire():
    return render_template('formulaire.html')


@app.route('/envoyer', methods=['POST'])
def donnees_formulaire():
    print(request.form['name'])
    print(request.form['fname'])
    print(request.form['birthday'])
    print(request.form['birthmonth'])
    print(request.form['birthyear'])
    print(request.form['email'])
    print(request.form['username'])
    print(request.form['password'])
    print(request.form['salary'])
    print(request.form['publicity'])
    print(request.form['rating'])
    # Excellent endroit pour valider les données et les sauvegarder dans une
    # base de données.
    # Prévoir une route pour afficher les erreurs.
    return redirect('/merci')


@app.route('/merci')
def merci():
    return render_template('merci.html')
