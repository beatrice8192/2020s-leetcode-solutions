-- https://leetcode.com/problems/employees-earning-more-than-their-managers
-- Write your PostgreSQL query statement below
select e.name as "Employee"
from Employee e
left join Employee m on e.managerId = m.id
where e.salary > m.salary;

