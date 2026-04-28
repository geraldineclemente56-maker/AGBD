--EJERCICIO 1
SELECT FirstName, LastName FROM employees
ORDER BY LastName ASC, FirstName ASC;

--EJERCICIO 2
SELECT t.Name, t.Milliseconds FROM tracks t
JOIN albums a ON t.AlbumId = a.AlbumId
WHERE a.Title = 'Big Ones'
ORDER BY t.Milliseconds DESC;


--Nombre y precio total de los 10 discos más baratos

--EJERCICIO 3
SELECT UnitPrice , name 
from tracks 
order by UnitPrice ASC
LIMIT 10;

--Ejercicio 4
SELECT name, GenreId, albumid, UnitPrice
FROM tracks
WHERE UnitPrice = 0.99 

--ejercicio 5
SELECT tracks.name, artists.Name, tracks.Milliseconds,  albums.Title
FROM tracks 
JOIN artists on tracks.AlbumId = albums.AlbumId
JOIN artists ON albums.ArtistId = artists.ArtistId
ORDER BY tracks.Milliseconds ASC
limit 20;


--ejercicio 6
--Apellido, puesto, apellido del jefe y cantidad de 
--clientes que atiende de todos los empleados, ordenado 
--desde los que atienden más clientes a los que atienden 
--menos.
SELECT emp.LastName AS empleado, jefe.LastName AS jefe, COUNT(*)  FROM employees emp
JOIN employees jefe ON emp.ReportsTo = jefe.EmployeeId
JOIN customers cus ON emp.EmployeeId = cus.SupportRepId
GROUP BY emp.EmployeeId
ORDER by jefe ASC


-- ejercicio 7
SELECT emp.LastName, emp.FirstName, c.FirstName, c.LastName
FROM empleados e
JOIN Clientes c on e.id = c.id_empleado;
