casper.test.begin("Vérification du click d'un site de cours", 1, function(test) {
  // Chargement de la page
  casper.start('http://jberger.org/');

  // Cliquer sur un lien d'un cours
  casper.then(function(){
    this.click("a[href='/inf4150']");
  });

  // Vérifier l'URL
  casper.run(function(){
    test.assertEquals(this.getCurrentUrl(), 'http://jberger.org/inf4150/');
    test.done();
  });
});
