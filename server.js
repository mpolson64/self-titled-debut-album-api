var express = require('express');
var app = express();

var port = process.env.PORT || 8080;

var router = express.Router();

app.listen(port);
console.log('API open on port ' + port);
