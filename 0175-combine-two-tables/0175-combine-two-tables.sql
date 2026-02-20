# Write your MySQL query statement below
Select  Person.firstName, Person.LastName, Address.city, Address.state
From Person 
Left Join Address on Person.personId = Address.personId

