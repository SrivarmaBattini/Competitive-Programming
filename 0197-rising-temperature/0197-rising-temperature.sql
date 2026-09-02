# Write your MySQL query statement below

SELECT DISTINCT id FROM (
    SELECT id, temperature, recordDate,
        LAG(temperature) OVER(ORDER BY recordDate) AS prevTemp,
        LAG(recordDate) OVER(ORDER BY recordDate) AS prevDate 
    FROM Weather
) t 
WHERE DATEDIFF(recordDate, prevDate) = 1
AND temperature > prevTemp;