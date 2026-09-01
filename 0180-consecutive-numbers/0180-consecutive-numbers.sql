# Write your MySQL query statement below

SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT num,
    LEAD(num, 1) OVER(ORDER BY ID) AS nextone,
    LEAD(num, 2) OVER(ORDER BY ID) AS nextnextone 
    FROM Logs
) t
WHERE num = nextone AND num = nextnextone;