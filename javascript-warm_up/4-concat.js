#!/usr/bin/node

const [args1 = 'undefined', args2 = 'undefined'] = process.argv.slice(2);

console.log(`${args1} is ${args2}`);
