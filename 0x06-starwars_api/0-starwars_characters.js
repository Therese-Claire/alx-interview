#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, { json: true }, (err, res, body) => {
  if (!err) {
    const characterPromises = body.characters.map(character => {
      return new Promise((resolve, reject) => {
        request(character, { json: true }, (err2, res2, body2) => {
          if (!err2) {
            resolve(body2.name);
          } else { reject(err2); }
        });
      });
    });

    Promise.all(characterPromises)
      .then(names => {
        names.forEach(name => console.log(name));
      })
      .catch(error => {
        console.log(error);
      });
  }
});
