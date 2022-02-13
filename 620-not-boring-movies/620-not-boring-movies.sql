# Write your MySQL query statement below

SELECT * from Cinema
WHERE Cinema.id % 2 != 0 AND Cinema.description != 'boring'
ORDER BY Cinema.rating DESC;
