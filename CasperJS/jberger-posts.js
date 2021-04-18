var casper = require('casper').create();
var articles = [];

function getPosts() {
  var list = document.querySelectorAll(".post-title");
  var result = [];
  for (i = 0; i < list.length; i++) {
    result.push(list[i].textContent);
  }
  return result;
}

casper.start('http://jberger.org/', function() {
  articles = this.evaluate(getPosts);
});

casper.then(function() {
  for (i = 0; i < articles.length; i++) {
    this.echo(articles[i]);
  }
});

casper.run();
