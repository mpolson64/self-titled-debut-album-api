Self-Titled-Debut-Album-API 🎤🖥️🔀
========================
[![Heroku](https://heroku-badge.herokuapp.com/?app=self-titled-debut-album-api&style=flat)](https://self-titled-debut-album-api.herokuapp.com/)
[![Travis-CI](https://api.travis-ci.org/mpolson64/Self-Titled-Debut-Album-API.svg?branch=master)](https://travis-ci.org/mpolson64/Self-Titled-Debut-Album-API)

##About
An API used to generate random band names as well as genres and Twitter-style messages. This project is the spirtitual successor to [Self-Titled-Debut-Album](https://github.com/mpolson64/Self-Titled-Debut-Album), a previous project that became increasingly annoying. Names are generated by asking [Wordnik's API](http://developer.wordnik.com/) for random words of specific parts of speech and combining them in preset patterns (ex. The Plural Nouns → The Beatles). Feel free to use for whatever projects you would like!

##Usage
The API has 4 paths:

###[`/full`](https://self-titled-debut-album-api.herokuapp.com/full):

Returns a filled in `message` as well as the component `bandName` and `genre`

###[`/bandname`](https://self-titled-debut-album-api.herokuapp.com/bandname):

Returns a random `bandName` from [Wordnik's API](http://developer.wordnik.com/) and the preset algorithm

###[`/genre`](https://self-titled-debut-album-api.herokuapp.com/genre):

Returns a random `genre` from a list

###[`/message`](https://self-titled-debut-album-api.herokuapp.com/message):

Returns a random Twitter-style `message` from a list with %BAND and %GENRE placeholders where the respective components are to be filled
