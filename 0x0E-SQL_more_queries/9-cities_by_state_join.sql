-- Retrieve cities with their corresponding state names
SELECT DISTINCT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
