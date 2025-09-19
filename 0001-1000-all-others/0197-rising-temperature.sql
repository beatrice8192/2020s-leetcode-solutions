-- https://leetcode.com/problems/rising-temperature
-- Write your PostgreSQL query statement below
select today.id from Weather today
left join Weather yesterday on today.recordDate::date - 1 = yesterday.recordDate
where today.temperature > yesterday.temperature;

