/*
    Table: Person
    +-------------+---------+
    | Column Name | Type    |
    +-------------+---------+
    | PersonId    | int     |
    | FirstName   | varchar |
    | LastName    | varchar |
    +-------------+---------+
    PersonId is the primary key column for this table.

    Table: Address

    +-------------+---------+
    | Column Name | Type    |
    +-------------+---------+
    | AddressId   | int     |
    | PersonId    | int     |
    | City        | varchar |
    | State       | varchar |
    +-------------+---------+
    AddressId is the primary key column for this table.

    Write an SQL query to report the first name, last name, city, and state of each person in the Person table. 
    If the address of a personId is not present in the Address table, report null instead.
    Return the result table in any order.

    Input

    Person table:
    +----------+----------+-----------+
    | personId | lastName | firstName |
    +----------+----------+-----------+
    | 1        | Wang     | Allen     |
    | 2        | Alice    | Bob       |
    +----------+----------+-----------+
    Address table:
    +-----------+----------+---------------+------------+
    | addressId | personId | city          | state      |
    +-----------+----------+---------------+------------+
    | 1         | 2        | New York City | New York   |
    | 2         | 3        | Leetcode      | California |
    +-----------+----------+---------------+------------+

    Output: 
    +-----------+----------+---------------+----------+
    | firstName | lastName | city          | state    |
    +-----------+----------+---------------+----------+
    | Allen     | Wang     | Null          | Null     |
    | Bob       | Alice    | New York City | New York |
    +-----------+----------+---------------+----------+

    select firstName, lastName, city, state from Person p, Address a
    left join p.personId on a.personId;

    Table schema:

    Create table Person (personId int, firstName varchar(255), lastName varchar(255));
    Create table Address (addressId int, personId int, city varchar(255), state varchar(255));

    insert into Person (personId, lastName, firstName) values ('1', 'Wang', 'Allen');
    insert into Person (personId, lastName, firstName) values ('2', 'Alice', 'Bob');
    insert into Address (addressId, personId, city, state) values ('1', '2', 'New York City', 'New York');
    insert into Address (addressId, personId, city, state) values ('2', '3', 'Leetcode', 'California');

*/

select firstName, lastName, city, state 
from Person as p
left join Address as a
on p.personId = a.personId