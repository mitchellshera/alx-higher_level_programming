#!/usr/bin/node

function add (a, b) {
  return (a + b);
}

const [,, arg1, arg2] = process.argv;
const num1 = parseInt(arg1);
const num2 = parseInt(arg2);

console.log(add(num1, num2));
