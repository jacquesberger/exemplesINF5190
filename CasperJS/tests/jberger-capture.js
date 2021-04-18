casper.test.begin("Vérification du click d'un site de cours avec capture", 1, function(test) {
  // Chargement de la page
  casper.start('http://jberger.org/');

  // Cliquer sur un lien d'un cours
  casper.then(function(){
    this.click("a[href='/inf4150']");
  });

  // Attendre le temps que le widget Twitter soit complètement chargé
  casper.then(function(){
    this.wait(2000);
  });

  // Prendre un screenshot du site
  casper.then(function(){
    this.capture("inf4150.png");
  });

  // Vérifier l'URL
  casper.run(function(){
    test.assertEquals(this.getCurrentUrl(), 'http://jberger.org/inf4150/');
    test.done();
  });
});
