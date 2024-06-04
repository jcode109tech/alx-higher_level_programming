#!/usr/bin/node
const process = require('process');
const request = require('request');

const url = process.argv[2];
const data;

request(url, function (error, response, body) {
  if (error != null) {
    console.log(error);
  } else {
    let movies = 0;
    data = JSON.parse(body);
    data['results'].forEach(function (result) {
      result['characters'].forEach(function (character) {
        const urlSplit = character.split('/');
        if (urlSplit[urlSplit.length - 2] === '18') {
          movies++;
        }
      });
    });
    console.log(movies);
  }
});
