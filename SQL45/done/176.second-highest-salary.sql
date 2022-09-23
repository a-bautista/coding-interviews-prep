-- [176] Second Highest Salary

-- https://leetcode.com/problems/second-highest-salary/description/

-- database
-- Easy (28.20%)
-- Likes:    643
-- Dislikes: 356
-- Total Accepted:    185.1K
-- Total Submissions: 620.6K
-- Testcase Example:  '{"headers": {"Employee": ["Id", "Salary"]}, "rows": {"Employee": [[1, 100], [2, 200], [3, 300]]}}'

-- Write a SQL query to get the second highest salary from the Employee
-- table.


-- +----+--------+
-- | Id | Salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+


-- For example, given the above Employee table, the query should return 200 as
-- the second highest salary. If there is no second highest salary, then the
-- query should return null.


-- +---------------------+
-- | SecondHighestSalary |
-- +---------------------+
-- | 200                 |
-- +---------------------+


-- Table schema:

-- Create table Employee (id int, salary int);

-- insert into Employee (id, salary) values (1, 100);
-- insert into Employee (id, salary) values (2, 200);
-- insert into Employee (id, salary) values (3, 300);
-- insert into Employee (id, salary) values (4, 400);
-- insert into Employee (id, salary) values (5, 500);


-- https://leetcode.com/problems/second-highest-salary/discuss/1168444/Summary-Five-ways-to-solve-the-top-n-nth-problems
-- This problem is similar to problems:
-- 177, 185, 184, 1194, 1341, 586, 1549, 1532, 1369, 1097, 1077, 1070, 602, 1082, 1112, 619, 574 (most voted)

-- Also, this question is similar to 619 on how to deal with null value. IFNULL(val, null) will not return 'null' if 
-- the value is empty (IFNULL will assume empty is the value we want). To avoid this problem, use either MAX() or 
-- subquery (IFNULL((subquery), null).

-- Versatile solutions
-- Subquery

select distinct salary from Employee order by salary desc limit 1 offset 2

-- offset indicates to get the current row - n value

-- Final query

select (
	select distinct salary from Employee order by salary desc limit 1 offset 2)
as SecondHighestSalary;


-- Specific solution

select distinct max(salary) as SecondHighestSalary
from Employee a
where Salary < (select distinct max(Salary) from Employee b where b.salary > a.salary );

-- Rank over density

With CTE as (
	SELECT salary, RANK () OVER (ORDER BY salary desc) AS RANK_desc
	FROM Employee)
select max(salary) from CTE
where RANK_desc = 2;


select salary, RANK () OVER (ORDER BY salary desc) as RANK_desc
from Employee
