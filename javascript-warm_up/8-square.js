#!/usr/bin/node

const args = process.argv.slice(2);
const num = parseInt(args);

let x;

if (Number.isNaN(num)) {
  console.log('Missing size');
} else {
  for (x = 0; x < num; x++) { console.log('x'.repeat(num)); }
}
