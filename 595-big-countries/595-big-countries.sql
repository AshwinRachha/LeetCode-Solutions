# Write your MySQL query statement below
SELECT name, population, area
FROM WORLD
where WORLD.population >= 25000000 OR WORLD.area >= 3000000;