#!/usr/bin/node

// Import the 'request' library
const request = require('request');

// Get the Movie ID from the first positional argument
const movieId = process.argv[2];

// Star Wars API endpoint for films
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Make a request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movie = JSON.parse(body);

    // Print each character name from the "characters" list
    movie.characters.forEach((characterUrl) => {
      request(characterUrl, (err, res, charBody) => {
        if (!err && res.statusCode === 200) {
          const character = JSON.parse(charBody);
          console.log(character.name);
        }
      });
    });
  } else {
    console.error('Error fetching movie data:', error);
  }
});
