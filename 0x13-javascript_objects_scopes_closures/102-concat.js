#!/usr/bin/node

const process = require('process');
const fs = require('fs');
const path = require('path');

const arg1 = process.argv[2];
const arg2 = process.argv[3];
const arg3 = process.argv[4];

fs.readFile(path.join(__dirname, arg1), 'utf8', function (err, data) {
  if (err) throw err;

  fs.readFile(path.join(__dirname, arg2), 'utf8', function (err, data2) {
    if (err) throw err;

    fs.writeFile(path.join(__dirname, arg3), data + data2, 'utf8', function (err) {
      if (err) throw err;
    });
  });
});