#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const wedgeAntillesCharacterId = 18;

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
    const data = JSON.parse(body);

    const moviesWithWedgeAntilles = data.results.filter((movie) =>
      movie.characters.includes(wedgeAntillesCharacterId)
    );

    console.log(`Number of movies with Wedge Antilles: ${moviesWithWedgeAntilles.length}`);
  } catch (parseError) {
    console.error(`Error parsing API response: ${parseError}`);
    process.exit(1);
  }
});
