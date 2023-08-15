#!/usr/bin/node

let printedCount = 0;

exports.logMe = function (item) {
  console.log(`${printedCount}: ${item}`);
  printedCount++;
};
