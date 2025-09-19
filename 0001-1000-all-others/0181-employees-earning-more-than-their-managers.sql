-- https://leetcode.com/problems/employees-earning-more-than-their-managers
-- compatible with MySQL, MS SQL, PostgreSQL.
select e.name as "Employee"
from Employee e
left join Employee m on e.managerId = m.id
where e.salary > m.salary;

