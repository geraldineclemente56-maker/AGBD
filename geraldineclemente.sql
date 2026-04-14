--EJERCICIO 1
SELECT FirstName, LastName FROM employees
ORDER BY LastName ASC, FirstName ASC;

--EJERCICIO 2
SELECT t.Name, t.Milliseconds FROM tracks t
JOIN albums a ON t.AlbumId = a.AlbumId
WHERE a.Title = 'Big Ones'
ORDER BY t.Milliseconds DESC;

--EJERCICIO 3
SELECT a.Title, SUM(t.UnitPrice) AS PrecioTotal 
FROM albums a
JOIN tracks t ON a.AlbumId = t.AlbumId
GROUP BY a.AlbumId
ORDER BY PrecioTotal ASC
LIMIT 10;

--EJERCICIO 4
SELECT t.Name AS Tema, g.Name AS Genero, a.Title AS Disco
FROM tracks t
JOIN genres g ON t.GenreId = g.GenreId
JOIN albums a ON t.AlbumId = a.AlbumId
WHERE t.UnitPrice = 0.99
ORDER BY t.Name ASC;

--EJERCICIO 5
