#!/usr/bin/node

const request = require('request');

const movieID = parseInt(process.argv[2]);
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;


request(url, (error, response, body) => {
    if (error) {
	console.error(error);
	return;
    }
    // convert the data to json
    try {
	const movieJson = JSON.parse(body);
	if (movieJson.title) {
	    console.log(movieJson.title);
	} else {
	    console.error(' NO title found in reponse: ', movieJson);
	}
    } catch (parseError) {
	console.error(parseError);
    }
});
