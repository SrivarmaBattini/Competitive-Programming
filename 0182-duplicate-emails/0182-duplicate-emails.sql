# Write your MySQL query statement below

SELECT DISTINCT email AS Email 
FROM Person P
WHERE 1 < (
    SELECT COUNT(M.email) FROM Person M 
    WHERE M.email = P.email 
);