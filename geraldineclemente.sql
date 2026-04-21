--EJERCICIO 1
SELECT FirstName, LastName FROM employees
ORDER BY LastName ASC, FirstName ASC;

--EJERCICIO 2
SELECT t.Name, t.Milliseconds FROM tracks t
JOIN albums a ON t.AlbumId = a.AlbumId
WHERE a.Title = 'Big Ones'
ORDER BY t.Milliseconds DESC;


