var assert = require('assert');
var fs = require('fs');

describe('Genres', function() {
    describe('#total genres', function() {
	it('should detect all 55', function() {
	    var genres = fs.readFileSync('genres.txt').toString().split('\n').slice(0, -1);
	    assert.equal(55, genres.length);
	});
    });
});

describe('Messages', function() {
    describe('#total messages', function() {
	it('should detect all 22', function() {
	    var messages = fs.readFileSync('messages.txt').toString().split('\n').slice(0, -1);
	    assert.equal(22, messages.length);
	});
    });
    describe('#parsing', function() {
	it('should replace all %s in each message template', function() {
	    var passing = true;
	    var failed = [];

	    var messages = fs.readFileSync('messages.txt').toString().split('\n').slice(0, -1);
	    var bandName = "foo";
	    var genre = "bar";

	    messages.forEach(function(item) {
		if(item.replace('%GENRE', genre).replace('%BAND', bandName).toString().indexOf('%') != -1) {
		    passing = false;
		    failed.push(item);
		}
	    });

	    assert(passing, "Failed on " + failed);
	});

    });
});
