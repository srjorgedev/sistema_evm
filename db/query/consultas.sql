-- USAR SOLO SI ES NECESARIO
-- BORRA TODA LA BD
DROP DATABASE evm_db;

SELECT * FROM `vehiculo`

-- Si en las consultas tenemos una lista de datos, deben ser de minimo 3 tuplas.

-- 1. Recuperar la informacion de todos los vehiculos
SELECT v.numSerie AS "Numero de serie", -- "
v.matricula as Matricula, v.proposito as Proposito, 
DATE_FORMAT(fechaAdquisicion, "%d-%m-%Y") as "Fecha de adquisicion", -- "
m.nombre as Marca, mo.nombre as Modelo, tl.codigo as "Licencia requerida" -- "
FROM vehiculo AS v
INNER JOIN marca AS m ON v.marca = m.codigo
INNER JOIN modelo AS mo ON v.modelo = mo.codigo
INNER JOIN tipo_licencia AS tl ON v.licencia_requerida = tl.codigo;

-- 2. Recuperar la informacion de un vehiculo
SELECT v.numSerie AS "Numero de serie", -- "
v.matricula as Matricula, v.proposito as Proposito, 
DATE_FORMAT(fechaAdquisicion, "%d-%m-%Y") as "Fecha de adquisicion", -- "
m.nombre as Marca, mo.nombre as Modelo, tl.codigo as "Licencia requerida" -- "
FROM vehiculo AS v
INNER JOIN marca AS m ON v.marca = m.codigo
INNER JOIN modelo AS mo ON v.modelo = mo.codigo
INNER JOIN tipo_licencia AS tl ON v.licencia_requerida = tl.codigo
WHERE v.numSerie = '70DKB7RK6CYPBKUTY'

-- 3. Recuperar la informacion de todos los usuarios
SELECT e.numero AS "Numero de empleado", -- "
CONCAT(nombrePila, ' ', apdPaterno, ' ', apdMaterno) AS Nombre,
tp.descripcion AS Rol,
tp.codigo AS Codigo,
lc.tipo_licencia AS "Tipo de licencia", -- "
lc.numero AS "Numero de licencia" -- "
FROM empleado AS e
INNER JOIN tipo_empleado AS tp ON e.tipo_empleado = tp.codigo
INNER JOIN licencia AS lc ON lc.empleado = e.numero
ORDER BY e.numero

-- 4. Recuperar la informacion de un empleado
SELECT e.numero AS "Numero de empleado", -- "
CONCAT(nombrePila, ' ', apdPaterno, ' ', apdMaterno) AS Nombre,
tp.descripcion AS Rol,
tp.codigo AS Codigo,
lc.tipo_licencia AS "Tipo de licencia", -- "
lc.numero AS "Numero de licencia" -- "
FROM empleado AS e
INNER JOIN tipo_empleado AS tp ON e.tipo_empleado = tp.codigo
INNER JOIN licencia AS lc ON lc.empleado = e.numero
WHERE e.numero = ?

-- 5. Recuperar la informacion de empleados con un tipo de licencia
SELECT e.numero AS "Numero de empleado", -- "
CONCAT(nombrePila, ' ', apdPaterno, ' ', apdMaterno) AS Nombre,
tp.descripcion AS Rol,
tp.codigo AS Codigo,
lc.tipo_licencia AS "Tipo de licencia", -- "
lc.numero AS "Numero de licencia" -- "
FROM empleado AS e
INNER JOIN tipo_empleado AS tp ON e.tipo_empleado = tp.codigo
INNER JOIN licencia AS lc ON lc.empleado = e.numero
INNER JOIN tipo_licencia AS tl ON lc.tipo_licencia = tl.codigo
WHERE tl.codigo = 'A'

-- BITACORAS

-- 0. Recuperar el total de bitacoras
SELECT COUNT(*) as TotalBitacoras FROM bitacora;

-- 1. Recuperar todas las bitacoras
SELECT * FROM bitacora;

-- 2. Recuperar lista general de bitacoras (No toda la informacion)
SELECT 
numero as id,
asunto,
destino, 
entrada, 
salida
FROM bitacora

-- VEHICULOS
SELECT 
    v.numSerie, 
    ma.nombre as marca,
    mo.nombre as modelo,
    v.disponibilidad 
FROM vehiculo AS v
INNER JOIN marca AS ma ON v.marca = ma.codigo
INNER JOIN modelo AS mo ON v.modelo = mo.codigo
WHERE v.disponibilidad = TRUE