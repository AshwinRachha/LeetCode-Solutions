# Write your MySQL query statement below

select name, bonus
FROM Employee LEFT JOIN Bonus
ON Employee.empId = Bonus.empId
WHERE
Bonus.bonus < 1000 or bonus is null;
