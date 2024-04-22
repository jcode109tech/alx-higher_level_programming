#!/usr/bin/node

const arguement = process.argv[2];

if (arguement === undefined) {
  console.log('No argument');
} else {
  console.log(arguement);
}
