# Write your MySQL query statement below

SELECT Department, Employee, Salary 
FROM (
    SELECT D.name AS Department,
           E.name AS Employee,
           E.salary AS Salary,
           DENSE_RANK() OVER(PARTITION BY D.id ORDER BY E.salary DESC) AS sr 
    FROM Employee E 
    LEFT JOIN Department D 
    ON E.departmentId = D.id
) t
WHERE t.sr <= 3;