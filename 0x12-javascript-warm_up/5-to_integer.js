#!/usr/bin/node

const [,, arg1] = process.argv;

const myArg = parseInt(arg1);

if (!isNaN(myArg)) {
  console.log(`My number: ${myArg}`);
} else {
  console.log('Not a number');
}
