/*

    +-------------+---------+
    | Column Name | Type    |
    +-------------+---------+
    | id          | int     |
    | email       | varchar |
    +-------------+---------+
    id is the primary key column for this table.
    Each row of this table contains an email. The emails will not contain uppercase letters.
    
    Write an SQL query to report all the duplicate emails.

    Return the result table in any order.

    The query result format is in the following example.

    Example 1:

    Input: 
    Person table:
    +----+---------+
    | id | email   |
    +----+---------+
    | 1  | a@b.com |
    | 2  | c@d.com |
    | 3  | a@b.com |
    +----+---------+
    Output: 
    +---------+
    | Email   |
    +---------+
    | a@b.com |
    +---------+

Explanation: a@b.com is repeated two times.

*/

-- subquery

select Email, count(Email) as num
from Person 
group by Email;

-- temp table

select email from (
    select Email, count(Email) as num
    from Person 
    group by Email
) as temp_table
where num > 1;

-- another solution

select Email 
from Person 
group by Email 
having count(Email)>1;
