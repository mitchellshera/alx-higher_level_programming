#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Make an HTTP GET request to the specified Star Wars API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error making API request: ${error}`);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Received HTTP status code ${response.statusCode}`);
    process.exit(1);
  }

  try {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    // Iterate through the character URLs and fetch each character's name
    characterUrls.forEach((characterUrl) => {
      request(characterUrl, (error, res, characterBody) => {
        if (error) {
          console.error(`Error fetching character data: ${error}`);
        } else {
          const characterData = JSON.parse(characterBody);
          console.log(characterData.name);
        }
      });
    });
  } catch (parseError) {
    console.error(`Error parsing API response: ${parseError}`);
    process.exit(1);
  }
});
