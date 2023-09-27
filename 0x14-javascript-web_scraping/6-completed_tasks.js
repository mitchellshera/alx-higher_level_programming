#!/usr/bin/node

const request = require('request');

// Check if the correct number of command-line arguments are provided
if (process.argv.length !== 3) {
  console.error('Usage: ./6-completed_tasks.js <API_URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

// Make an HTTP GET request to the specified API URL
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
    const tasks = JSON.parse(body);

    // Create an object to store the counts of completed tasks by user ID
    const completedTasksByUser = {};

    // Iterate through the tasks and count completed tasks by user ID
    tasks.forEach((task) => {
      if (task.completed) {
        if (completedTasksByUser[task.userId]) {
          completedTasksByUser[task.userId]++;
        } else {
          completedTasksByUser[task.userId] = 1;
        }
      }
    });

    // Print the completed tasks by user ID as a JSON object
    console.log(completedTasksByUser);
  } catch (parseError) {
    console.error(`Error parsing API response: ${parseError}`);
    process.exit(1);
  }
});
