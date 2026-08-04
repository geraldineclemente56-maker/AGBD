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
SELECT emp.LastName AS empleado, jefe.LastName AS jefe, 
COUNT(*)  FROM employees emp
JOIN employees jefe ON emp.ReportsTo = jefe.EmployeeId
JOIN customers cus ON emp.EmployeeId = cus.SupportRepId
GROUP BY emp.EmployeeId
ORDER by jefe ASC

--ejercicio 7
SELECT e.FirstName AS NombreEmpleado, e.LastName AS ApellidoEmpleado,c.FirstName AS NombreCliente, c.LastName AS ApellidoCliente
FROM employees e
JOIN customers c ON e.EmployeeId = c.SupportRepId;

--ejercicio 8
SELECT customers.FirstName AS NombreCliente, artists.Name AS NombreArtista
from customers
JOIN invoices. on customers.CustomersId = invoices.CustomerId
JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
JOIN tracks ON invoice_items.TrackId = tracks.TrackId
JOIN albums ON tracks.AlbumId = albums.AlbumId
JOIN artists ON albums.ArtistId = artists.ArtistId
order by customers.FirstName;

-- ejercicio 9
SELECT genres.Name, 
COUNT(*) AS Total
FROM genres
JOIN tracks ON genres.GenreId = tracks.GenreId
GROUP BY 1
ORDER BY 2 DESC;

-- ejercicio 10
SELECT customers.FirstName, customers.LastName, artists.Name
from customers
JOIN invoices ON customers.CustomerId = invoices.CustomerId
JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
JOIN tracks ON invoice_items.TrackId = tracks.TrackId
JOIN albums ON tracks.AlbumId = albums.AlbumId
JOIN artists ON albums.ArtistId = artists.ArtistId
ORDER BY customers.FirstName ASC;
-- ejercicio 11
SELECT c.FirstName, c.City, t.Name, g.Name
FROM customers c
JOIN invoices i ON c.CustomerId = i.CustomerId
JOIN invoice_items ii ON i.InvoiceId = ii.InvoiceId
JOIN tracks t ON ii.TrackId = t.TrackId
JOIN genres g ON t.GenreId = g.GenreId;
-- ejercicio 12
SELECT *
FROM employees e
JOIN customers c ON e.EmployeeId = c.SupportRepId
JOIN invoices i ON c.CustomerId = i.CustomerId
JOIN invoice_items ii ON i.InvoiceId = ii.InvoiceId
JOIN tracks t ON ii.TrackId = t.TrackId
JOIN genres g ON t.GenreId = g.GenreId
JOIN media_types mt ON t.MediaTypeId = mt.MediaTypeId
JOIN albums alb ON t.AlbumId = alb.AlbumId
JOIN artists art ON alb.ArtistId = art.ArtistId
JOIN playlist_track pt ON t.TrackId = pt.TrackId
JOIN playlists p ON pt.PlaylistId = p.PlaylistId;
