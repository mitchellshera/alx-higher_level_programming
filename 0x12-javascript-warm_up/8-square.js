#!/usr/bin/node

const [,, arg1] = process.argv;
const size = parseInt(arg1);

if (!isNaN(size)) {
  for (let i = 0; i < size; i++) {
    console.log("X".repeat(size));
  }
} else {
  console.log("Missing size");
}
