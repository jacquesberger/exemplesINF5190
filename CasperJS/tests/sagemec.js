casper.test.begin("Création d'un membre stagiaire, vérification du dossier et de la présence dans la recherche", 7, function(test) {

  // Charger la page initiale
  casper.start('http://localhost:3003/', function() {
    // Vérifier que nous avons bien été redirigé vers la page de login
    test.assertEquals(this.getCurrentUrl(), "http://localhost:3003/login");

    // Remplir et soumettre le formulaire de login
    this.fill("form[action='/login']", {username:"code3", password:"1337"}, true);
  });

  // Vérifier que nous avons été redirigé à la page d'accueil après
  // l'authentification
  casper.then(function() {
    test.assertEquals(this.getCurrentUrl(), "http://localhost:3003/");
  });

  // Charger un formulaire de création de dossier, remplir le formulaire et
  // cliquer sur le bouton de soumission
  casper.thenOpen('http://localhost:3003/membre/nouveau', function() {
    this.fill("form", {nom: "Berger", prenom: "Jacques", sexe: "1", date_naissance: "1982-03-05"}, false);
    this.click("button");
  });

  // Attendre le temps de recevoir la réponse du backend
  casper.then(function() {
    this.wait(1000);
  });

  // Vérifier qu'on a été redirigé vers le profil du nouveau dossier et qu'il
  // est bien visible
  casper.then(function() {
    test.assertVisible("#profile");
    test.assertUrlMatch(/^http:\/\/localhost:3003\/membre\/#\/[0-9a-f]{24}\/fiche\/parcours/);
    test.assertMatch(this.getElementAttribute("#tab-parcours", "class"), /active/);
  });

  // Lancer une recherche sur le dossier nouvellement créé
  casper.then(function() {
    this.fillSelectors("form.form-search", {"#search-field": "Jacques Berger"}, false);
    this.click("form.form-search button");
  });

  // Vérifier que le nouveau dossier est présent dans les résultats de recherche
  casper.then(function() {
    test.assertEquals(this.getCurrentUrl(), "http://localhost:3003/recherche?q=Jacques Berger");

    var getTrCount = function() {
      return __utils__.findAll("tr").length;
    };
    var trCount = this.evaluate(getTrCount);
    test.assert(trCount > 0);
  });

  casper.run(function(){
    test.done();
  });
});
