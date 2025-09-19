-- https://leetcode.com/problems/combine-two-tables
-- compatible with MySQL, MS SQL, PostgreSQL.
select firstName, lastName, city, state
from Person
left join Address on Person.personId = Address.personId;

