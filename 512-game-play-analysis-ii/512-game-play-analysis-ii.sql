# Write your MySQL query statement below

SELECT player_id, device_id 
from Activity
WHERE (player_id, event_date) in (SELECT player_id, MIN(event_date) from Activity
GROUP BY player_id);