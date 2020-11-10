# https://leetcode-cn.com/problems/swap-salary/
Update salary set sex = if(sex = 'm', 'f', 'm')

UPDATE salary
SET 
    sex = CASE sex
            WHEN 'm' THEN 'f'
            ELSE 'm'
        END;

# https://leetcode-cn.com/problems/employees-earning-more-than-their-managers/
select e.Name as Employee from Employee e left join Employee m on e.ManagerId = m.Id where e.salary > m.salary

# https://leetcode-cn.com/problems/classes-more-than-5-students/
select class from courses group by class having count(distinct student) >= 5 ;

# https://leetcode-cn.com/problems/big-countries/
select name, population, area from World where area > 3000000 or population > 25000000;

# https://leetcode-cn.com/problems/delete-duplicate-emails/
delete p1 from Person p1, Person p2 where p1.Email = p2.Email and p1.Id > p2.Id;


# https://leetcode-cn.com/problems/reformat-department-table/submissions/
# Write your MySQL query statement below
select id,
    sum(case `month` when 'Jan' then revenue else null end) as Jan_Revenue,
    sum(case `month` when 'Feb' then revenue else null end) as Feb_Revenue,
    sum(case `month` when 'Mar' then revenue else null end) as Mar_Revenue,
    sum(case `month` when 'Apr' then revenue else null end) as Apr_Revenue,
    sum(case `month` when 'May' then revenue else null end) as May_Revenue,
    sum(case `month` when 'Jun' then revenue else null end) as Jun_Revenue,
    sum(case `month` when 'Jul' then revenue else null end) as Jul_Revenue,
    sum(case `month` when 'Aug' then revenue else null end) as Aug_Revenue,
    sum(case `month` when 'Sep' then revenue else null end) as Sep_Revenue,
    sum(case `month` when 'Oct' then revenue else null end) as Oct_Revenue,
    sum(case `month` when 'Nov' then revenue else null end) as Nov_Revenue,
    sum(case `month` when 'Dec' then revenue else null end) as Dec_Revenue
from Department
group by id

# https://leetcode-cn.com/problems/department-highest-salary/
select d.Name Department,
       e.Name Employee,
       e.Salary
from Employee e join Department d
on e.DepartmentId = d.Id
where (e.DepartmentId, e.Salary) in (select DepartmentId, max(Salary) from Employee group by DepartmentId);

# https://leetcode-cn.com/problems/second-highest-salary/
select IFNULL((select distinct(Salary) 
from Employee
order by Salary desc
limit 1,1),null) as SecondHighestSalary