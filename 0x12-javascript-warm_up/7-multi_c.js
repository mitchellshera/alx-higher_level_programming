#!/usr/bin/node

const [,, arg1] = process.argv;
const occur = parseInt(arg1);

if (!isNaN(occur)) {
  for (let i = 0; i < occur; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
