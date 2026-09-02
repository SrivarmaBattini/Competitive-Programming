# Write your MySQL query statement below


SELECT E.name AS Employee 
FROM Employee E 
WHERE E.salary > (
    SELECT M.salary FROM Employee M 
    WHERE M.id = E.managerId
);