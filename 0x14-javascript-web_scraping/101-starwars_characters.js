#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

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

    fetchAndPrintCharacters(characterUrls, 0);
  } catch (parseError) {
    console.error(`Error parsing API response: ${parseError}`);
    process.exit(1);
  }
});

function fetchAndPrintCharacters(characterUrls, index) {
  if (index >= characterUrls.length) {
    return;
  }

  const characterUrl = characterUrls[index];

  request(characterUrl, (error, response, characterBody) => {
    if (error) {
      console.error(`Error fetching character data: ${error}`);
      process.exit(1);
    }

    if (response.statusCode !== 200) {
      console.error(`Error: Received HTTP status code ${response.statusCode}`);
      process.exit(1);
    }

    const characterData = JSON.parse(characterBody);
    console.log(characterData.name);

    fetchAndPrintCharacters(characterUrls, index + 1);
  });
}
