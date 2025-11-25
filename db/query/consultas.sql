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
e.nombre AS Nombre,
tp.descripcion AS Rol,
tp.codigo AS Codigo,
tl.codigo as "Tipo de licencia", -- "
tl.descripcion AS "Descripcion de Licencia", -- "
lc.numero AS "Numero de licencia" -- "
FROM empleado AS e
INNER JOIN tipo_empleado AS tp ON e.tipo_empleado = tp.codigo
INNER JOIN licencia AS lc ON lc.empleado = e.numero
INNER JOIN tipo_licencia AS tl ON lc.tipo_licencia = tl.numero
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


'''
6. Licencias de cada empleado
    a. Número de empleado
    b. Nombre completo del empleado en una columna
    c. Descripción del tipo de empleado
    d. Número de licencia
    e. Clase del tipo de licencia
    f. Fecha de expedición
    g. Fecha de vencimiento
'''
SELECT e.nombre as Nombre,
te.descripcion as "Tipo de empleado", -- "
l.numero as "Numero de licencia", -- "
tl.codigo as "Clase de licencia", -- "
l.fechaExpedicion as "Fecha de expedicion", -- "
l.fechaVencimiento as "Fecha de vencimiento" -- "
from empleado as e
inner join tipo_empleado as te on e.tipo_empleado = te.codigo
inner join licencia as l on e.numero = l.empleado
inner join tipo_licencia as tl on l.tipo_licencia = tl.numero


#Contactos de Empleados
SELECT e.numero as Numero,
e.nombre as Nombre, 
e.email as "Correo Electronico", -- "
t.numTelefono as "Numero Telefonico" -- "
from empleado as e
inner join telefono as t on t.empleado = e.numero


--Observaciones realizadas en una bitacora
SELECT 
    o.bitacora AS bitacora_num,
    o.numero AS observacion_num,
    o.descripcion AS observacion_desc
FROM observacion o
WHERE o.bitacora = 12; -- reemplaza con la bitácora que quieras

--Reporte de mantenimiento de un vehiculo
SELECT 
    v.matricula,
    m.nombre AS marca,
    mo.nombre AS modelo,
    mt.fechaProgramada AS fecha,
    mt.razon,
    mt.comentarios,
    tm.comentario AS tipo_mantenimiento,
    tobs.descripcion AS tipo_observacion,
    em.descripcion AS estado_mantenimiento
FROM mantenimiento mt
JOIN vehiculo v ON mt.vehiculo = v.numSerie
JOIN marca m ON v.marca = m.codigo
JOIN modelo mo ON v.modelo = mo.codigo
JOIN tipoMantenimiento tm ON mt.tipoMantenimiento = tm.numero
JOIN estadoMantenimiento em ON mt.estadoMantenimiento = em.numero
LEFT JOIN mantenimiento_bitacora mb ON mt.folio = mb.mantenimiento
LEFT JOIN observacion o ON mb.bitacora = o.bitacora
LEFT JOIN tipoObservacion tobs ON o.tipoObservacion = tobs.numero
WHERE v.matricula = 'XYZ123'; -- vehículo específico

--Estados de los vehiculos en mantenimiento
SELECT 
    mt.folio,
    v.matricula,
    ma.nombre AS marca,
    mo.nombre AS modelo,
    mt.fechaProgramada AS fecha,
    mt.razon,
    tm.comentario AS tipo_mantenimiento,
    em.descripcion AS estado_mantenimiento
FROM mantenimiento mt
JOIN vehiculo v ON mt.vehiculo = v.numSerie
JOIN marca ma ON v.marca = ma.codigo
JOIN modelo mo ON v.modelo = mo.codigo
JOIN tipoMantenimiento tm ON mt.tipoMantenimiento = tm.numero
JOIN estadoMantenimiento em ON mt.estadoMantenimiento = em.numero
ORDER BY mt.fechaProgramada DESC;

--JOINS MANTENIMIENTO CON TIPO MANTENIMIENTO, ESTADO MANTENIMIENTO Y VEHICULO
select m.folio as Folio, m.razon as Razon, m.estatus as Estatus, m.importancia as Importancia,
m.fechaProgramada as Fecha, m.comentarios as Comentarios, tm.comentario as TipoMantenimiento,
v.numSerie as Vehiculo, em.descripcion as EstadoMantenimiento
from mantenimiento as m
inner join tipomantenimiento as tm on m.tipomantenimiento = tm.numero
inner join estadomantenimiento as em on m.estadomantenimiento = em.numero
inner join vehiculo as v on m.vehiculo = v.numSerie

--JOINS OBSERVACION CON TIPO OBSERVACION Y BITACORA
select o.numero as Folio, o.descripcion as Descripcion, tob.descripcion as Tipo,
b.numero as Bitacora
from observacion as o
inner join bitacora as b on o.bitacora = b.numero
inner join tipoObservacion as tob on o.tipoObservacion = tob.numero