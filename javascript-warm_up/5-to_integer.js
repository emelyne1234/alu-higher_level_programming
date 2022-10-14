#!/usr/bin/node
const args = process.argv;
const conv = number(args[2]);
if (conv) {
	console.log('My number: ${args[2]}');
else {
	console.log('Not a number');
}
