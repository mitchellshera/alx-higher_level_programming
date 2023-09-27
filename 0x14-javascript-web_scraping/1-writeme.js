#!/usr/bin/node

const fs = require('fs');
const path = require('path');

// Check if the correct number of command-line arguments are provided
if (process.argv.length !== 4) {
  console.error('Usage: ./1-writeme.js <file_path> <string_to_write>');
  process.exit(1);
}

const filePath = process.argv[2];
const stringToWrite = process.argv[3];

fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(`Error: ${err}`);
  } else {
    console.log(`Successfully wrote "${stringToWrite}" to ${filePath}`);
  }
});
