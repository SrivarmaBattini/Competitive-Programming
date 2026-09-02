# Write your MySQL query statement below

-- SELECT DISTINCT email AS Email 
-- FROM Person P
-- WHERE 1 < (
--     SELECT COUNT(M.email) FROM Person M 
--     WHERE M.email = P.email 
-- );

-- SELECT email AS Email 
-- FROM Person
-- GROUP BY email 
-- HAVING COUNT(email) > 1;

SELECT DISTINCT email AS Email 
FROM (
    SELECT email, COUNT(email) OVER(PARTITION BY email) AS OCCUR
    FROM Person
) t
WHERE OCCUR > 1;