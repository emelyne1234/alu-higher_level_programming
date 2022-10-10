#!/usr/bin/node
const args = argv
if (args.length == 2) {
console.log('Argument found');
} else if (args.length > 2) {
console.log('Argumentsfound');
} else {
console.log('No argument');
}
