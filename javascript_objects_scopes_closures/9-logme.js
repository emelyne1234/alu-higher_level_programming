#!/usr/bin/node
let counter = 0;
exports.logMe = function (item) {
  const a = counter;
  console.log(a + ': ' + item);
  counter++
}
