#!/usr/bin/node
const args = argv;
if (args.length == 3) {
console.log('Argument found');
} else if (args.length > 3) {
console.log('Argumentsfound');
} else {
console.log('No argument');
}
