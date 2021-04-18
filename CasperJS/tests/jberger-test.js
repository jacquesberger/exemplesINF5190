casper.test.begin("Vérification du nombre d'articles", 1, function(test) {
  var articles = [];

  // Cette fonction va chercher la liste des titres d'articles
  function getPosts() {
    var list = document.querySelectorAll(".post-title");
    var result = [];
    for (i = 0; i < list.length; i++) {
      result.push(list[i].textContent);
    }
    return result;
  }

  // Chargement de la page
  casper.start('http://jberger.org/', function() {
    articles = this.evaluate(getPosts);
  });

  // Vérifier le nombre d'articles
  casper.run(function(){
    test.assertEquals(articles.length, 5);
    test.done();
  });
});
