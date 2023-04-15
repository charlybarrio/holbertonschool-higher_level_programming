#!/usr/bin/node

function fact (a) {
  if (Number.isNaN(a)) {
    return 1;
  } else if (a <= 1) {
    return 1;
  } else {
    return a * fact(a - 1);
  }
}
const args = process.argv.slice(2);
const a = parseInt(args[0]);
console.log(fact(a));
