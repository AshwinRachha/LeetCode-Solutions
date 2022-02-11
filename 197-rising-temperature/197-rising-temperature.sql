# Write your MySQL query statement below
SELECT w1.id 
FROM Weather w1, Weather w2
WHERE
    w1.temperature > w2.temperature AND DATE_ADD(w2.recordDate, interval 1 day) = w1.recordDate;