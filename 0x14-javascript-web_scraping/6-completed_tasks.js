#!/usr/bin/node

const request = require('request');
const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

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
    const todos = JSON.parse(body);

    const completedTasksByUser = {};
    
    todos.forEach((todo) => {
      if (todo.completed) {
        if (!completedTasksByUser[todo.userId]) {
          completedTasksByUser[todo.userId] = 1;
        } else {
          completedTasksByUser[todo.userId]++;
        }
      }
    });

    for (const userId in completedTasksByUser) {
      console.log(`User ID ${userId}: ${completedTasksByUser[userId]} completed tasks`);
    }
  } catch (parseError) {
    console.error(`Error parsing API response: ${parseError}`);
    process.exit(1);
  }
});
