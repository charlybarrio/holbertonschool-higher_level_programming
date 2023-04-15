#!/usr/bin/node

const args = process.argv.slice(2).map(Number).sort((a, b) => b - a);

if ((args.length < 2)) {
  console.log(0);
} else {
  for (let n = 1; n < args.length; n++) {
    if (args[n] < args[0]) {
      console.log(args[n]);
      break;
    }
  }
}
