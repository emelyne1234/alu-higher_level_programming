#!/usr/bin/node
exports.execute = function(x, theFunction) {
for (let i = 0; i < x; i++) {
theFunction();
 }
};
