#!/usr/bin/node

const [, , ...args] = process.argv.map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  args.sort((a, b) => b - a);
  console.log(args[1]);
}
