-- USAR SOLO SI ES NECESARIO
-- BORRA TODA LA BD
DROP DATABASE evm_db;

-- 1. Recuperar la informacion de los vehiculos
SELECT v.numSerie AS "Numero de serie", -- "
v.matricula as Matricula, v.proposito as Proposito, 
DATE_FORMAT(fechaAdquisicion, "%d-%m-%Y") as "Fecha de adquisicion", -- "
m.nombre as Marca, mo.nombre as Modelo, tl.codigo as "Licencia requerida" -- "
FROM vehiculo AS v
INNER JOIN marca AS m ON v.marca = m.codigo
INNER JOIN modelo AS mo ON v.modelo = mo.codigo
INNER JOIN tipo_licencia AS tl ON v.licenciaRequerida = tl.codigo;

-- 2. Recuperar la informacion de los usuarios
SELECT numero AS "Numero de empleado", -- "
CONCAT(nombrePila, ' ', apdPaterno, ' ', apdMaterno) AS Nombre,
tp.descripcion AS Rol,
tp.codigo AS Codigo
FROM empleado AS e
INNER JOIN tipo_empleado AS tp ON e.tipo_empleado = tp.codigo
WHERE numero = 3