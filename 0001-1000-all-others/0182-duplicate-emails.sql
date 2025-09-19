-- https://leetcode.com/problems/duplicate-emails
-- Write your PostgreSQL query statement below
with email_count as (select email, count(email) from Person group by email)
select email from email_count where count > 1;

