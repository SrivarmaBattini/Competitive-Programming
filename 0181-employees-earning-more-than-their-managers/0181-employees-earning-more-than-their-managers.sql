# Write your MySQL query statement below


-- SELECT E.name AS Employee 
-- FROM Employee E 
-- WHERE E.salary > (
--     SELECT M.salary FROM Employee M 
--     WHERE M.id = E.managerId
-- );

SELECT E.name AS Employee
FROM Employee E
JOIN Employee M
    ON E.managerId = M.id
WHERE E.salary > M.salary;