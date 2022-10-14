#!/usr/bin/node
const args = process.argv.slice(2);
const conv = number(args[0]);
if (conv) {
	console.log('My number: ' + number(args[0]));
else {
	console.log('Not a number');
}
