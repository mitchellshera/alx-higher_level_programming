#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, (error, response) => {
  if (error) {
    console.error(`Error making request: ${error}`);
  } else {
    console.log(`HTTP status code: ${response.statusCode}`);
  }
});