#!/usr/bin/node

const Initsquare_rec = require('./5-square');

class Square extends Initsquare_rec {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;