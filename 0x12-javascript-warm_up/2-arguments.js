#!/usr/bin/node

const array = process.argv.length - 2;

if (array === 0) {
  console.log('No arguement');
} else if (array === 1) {
  console.log('Arguement found');
} else {
  console.log('Arguments found');
}
