var spawn = require('child_process').spawn;
var fs = require('fs');
var express = require('express');
var app = express();

var genres = fs.readFileSync('genres.txt').toString().split('\n');
var messages = fs.readFileSync('messages.txt').toString().split('\n');

var router = express.Router();

app.get('/', function(req, res) {
    res.json({
	message: "Welcome to the Self Titled Debut Album API. For more information visit https://github.com/mpolson64/Self-Titled-Debut-Album-API"
    });
});

app.get('/bandname', function(req, res) {
    var script = spawn('python', ['generator.py']);
    var dataString = '';

    script.stdout.on('data', function(data) {
	dataString += data.toString();
    });

    script.stdout.on('end', function() {
	console.log(dataString);
	res.json({
	    bandName: dataString.substring(0, dataString.length - 1)
	});
    });
});

app.get('/genre', function(req, res) {
    res.json({
	genre: genres[Math.floor(Math.random() * genres.length)]
    });
});

app.get('/full', function(req, res) {
    var genre = genres[Math.floor(Math.random() * genres.length)]

    var message = messages[Math.floor(Math.random() * messages.length)]

    var script = spawn('python', ['generator.py']);
    var dataString = '';
    var bandName = '';

    script.stdout.on('data', function(data) {
	dataString += data.toString();
    });

    script.stdout.on('end', function() {
	console.log(dataString);
	bandName = dataString.substring(0, dataString.length - 1);
	res.json({
	    bandName: bandName,
	    genre: genre,
	    message: message
	});
    });
});

var server = app.listen(process.env.PORT || 8080, function() {
    var host = server.address().address;
    var port = server.address().port;

    console.log('API open on port ' + port);
});
