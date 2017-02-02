var spawn = require('child_process').spawn;

var express = require('express');
var app = express();

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
	    bandName: dataString
	});
    });
});

var server = app.listen(process.env.PORT || 8080, function() {
    var host = server.address().address;
    var port = server.address().port;

    console.log('API open on port ' + port);
});
