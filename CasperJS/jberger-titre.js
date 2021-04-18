var casper = require('casper').create();

casper.start('http://jberger.org/', function() {
  this.echo(this.getTitle());
});

casper.run();
