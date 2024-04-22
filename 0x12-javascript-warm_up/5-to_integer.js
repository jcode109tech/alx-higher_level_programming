#!/usr/bin/node

const value = process.argv[2];
const intValue = parseInt(value);

if (!isNaN(intValue)) {
  console.log('My number: ' + intValue);
} else {
  console.log('Not a number');
}
