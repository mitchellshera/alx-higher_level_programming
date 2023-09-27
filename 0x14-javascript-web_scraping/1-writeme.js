#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

fs.writeFile(filePath, stringToWrite, error => {
  if (error) {
    console.error(`Error writing file: ${error}`);
  } else {
    console.log(`Successfully wrote "${stringToWrite}" to ${filePath}`);
  }
});;