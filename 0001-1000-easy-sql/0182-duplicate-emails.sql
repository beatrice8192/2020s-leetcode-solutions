-- https://leetcode.com/problems/duplicate-emails
-- compatible with MySQL, MS SQL, PostgreSQL.
with email_count as (
    select email, count(email) as count
    from Person
    group by email
)
select email
from email_count
where count > 1;

