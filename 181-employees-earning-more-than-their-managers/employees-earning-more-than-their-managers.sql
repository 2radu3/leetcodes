/* Write your PL/SQL query statement below */
select e.name as employee from employee e, employee em
where e.managerId=em.id and e.salary > em.salary