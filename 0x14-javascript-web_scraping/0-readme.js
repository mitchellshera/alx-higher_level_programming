#!/usr/bin/node
const fs = require('fs');
const path = require('path');

// Check if the correct number of command-line arguments are provided
if (process.argv.length !== 3) {
  console.error('Usage: ./0-readme.js <file_path>');
  process.exit(1);
}

const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(`Error: ${err}`);
  } else {
    console.log(data);
  }
});