# Write your MySQL query statement below

-- SELECT DISTINCT id FROM (
--     SELECT id, temperature, recordDate,
--         LAG(temperature) OVER(ORDER BY recordDate) AS prevTemp,
--         LAG(recordDate) OVER(ORDER BY recordDate) AS prevDate 
--     FROM Weather
-- ) t 
-- WHERE DATEDIFF(recordDate, prevDate) = 1
-- AND temperature > prevTemp;


WITH CTE AS (
    SELECT id, recordDate, temperature, 
        LAG(temperature) OVER(ORDER BY recordDate) AS prevTemp, 
        LAG(recordDate) OVER(ORDER BY recordDate) AS prevDate
    FROM Weather
)

SELECT id 
FROM CTE WHERE temperature > prevTemp 
AND DATEDIFF(recordDate, prevDate) = 1;