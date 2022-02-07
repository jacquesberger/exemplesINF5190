// Copyright 2017 Jacques Berger
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Lancée lorsque le champ de pays change. Met à jour la liste des provinces.
// Exemple avec xhr.
function onPaysChange() {
  var champProvince = document.getElementById("champ-province");

  var pays = document.getElementById("champ-pays").value;
  if (pays === "") {
    champProvince.value = "";
    champProvince.disabled = true;
  } else {
    champProvince.disabled = false;

    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
      if (xhr.readyState === XMLHttpRequest.DONE) {
        if (xhr.status === 200) {
          champProvince.innerHTML = xhr.responseText;
          champProvince.value = "";
        } else {
          console.log('Erreur avec le serveur');
        }
      }
    };

    xhr.open("GET", "/provinces/"+pays, true);
    xhr.send();
  }
  var champVille = document.getElementById("champ-ville");
  champVille.value = "";
  champVille.disabled = true;
}

// Lancée lorsque la province change. Met la liste des villes à jour.
// Exemple avec fetch.
function onProvinceChange() {
  let champVille = document.getElementById("champ-ville");

  const province = document.getElementById("champ-province").value;
  if (province === "") {
    champVille.value = "";
    champVille.disabled = true;
  } else {
    champVille.disabled = false;

    fetch("/villes/"+province)
      .then(response => response.text())
      .then(response => {
        champVille.innerHTML = response;
        champVille.value = "";
      })
      .catch(err => {
        console.log("Erreur avec le serveur :", err);
      });
  }
}

document.getElementById("champ-pays").addEventListener("change", onPaysChange);
document.getElementById("champ-province").addEventListener("change", onProvinceChange);
