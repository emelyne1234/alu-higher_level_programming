#!/usr/bin/node
const args = process.argv;
const conv = number(args[0]);
if (conv) {
	console.log('My number: args[0]');
else {
	console.log('Not a number');
}
