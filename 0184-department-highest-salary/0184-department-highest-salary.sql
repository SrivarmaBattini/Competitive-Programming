# Write your MySQL query statement below

SELECT Department, Employee, Salary
FROM (
    SELECT D.name AS Department,
           E.name AS Employee,
           E.salary AS Salary,
           MAX(E.salary) OVER(PARTITION BY D.id) AS HS
    FROM Employee E
    LEFT JOIN Department D
        ON E.departmentId = D.id
) t
WHERE Salary = HS;