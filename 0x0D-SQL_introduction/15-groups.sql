-- Retrieve the count of records with the same score, sorted by count in descending order
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
