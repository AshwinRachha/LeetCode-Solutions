# Write your MySQL query statement below
DELETE FROM Person
    WHERE ID NOT IN
    (
        SELECT * FROM(
        SELECT MIN(Id) FROM Person GROUP BY Email) as p
    )
