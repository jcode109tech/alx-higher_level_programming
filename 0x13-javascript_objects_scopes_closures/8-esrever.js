#!/usr/bin/node

exports.esrever = function (list) {
    const revlist = [];
    let leng = list.length - 1;
    for (let i = leng; i >= 0; i--) {
        revlist.push(list[i]);
    }
    return revlist;
}