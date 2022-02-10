# Write your MySQL query statement below

select 
    a.name as 'Employee'
From Employee AS a JOIN Employee as b
    ON a.ManagerId = b.Id
    AND a.Salary > b.Salary;