-- https://leetcode.com/problems/customers-who-never-order
-- compatible with MySQL, MS SQL, PostgreSQL.
select c.name as "Customers"
from Customers c
left join Orders o on c.id = o.customerId
where o.id is null;

