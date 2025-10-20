-- https://leetcode.com/problems/delete-duplicate-emails
-- compatible with MySQL, MS SQL, PostgreSQL.
with email_distinct as (
    select min(id) as id
    from Person
    group by email
)
delete from Person
where id not in (select * from email_distinct);

