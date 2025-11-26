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
SELECT CONCAT(e.nombrePila, ' ', e.apdPaterno, ' ', e.apdMaterno) as Nombre,
te.descripcion as "Tipo de empleado", -- "
l.numero as "Numero de licencia", -- "
tl.codigo as "Clase de licencia", -- "
l.fechaExpedicion as "Fecha de expedicion", -- "
l.fechaVencimiento as "Fecha de vencimiento" -- "
from empleado as e
inner join tipo_empleado as te on e.tipo_empleado = te.codigo
inner join licencia as l on e.numero = l.empleado
inner join tipo_licencia as tl on l.tipo_licencia = tl.numero
where te.descripcion = 'Chofer'


#Contactos de Empleados
SELECT e.numero as Numero,
CONCAT(e.nombrePila, ' ', e.apdPaterno, ' ', e.apdMaterno) as Nombre,
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
SELECT 
            e.numero,
            CONCAT(e.nombrePila, ' ', e.apdPaterno, ' ', e.apdMaterno) AS nombre,
            l.numero AS licencia,
            l.tipo_licencia AS tipo,
            l.fechaVencimiento
        FROM empleado AS e
        INNER JOIN licencia AS l ON e.numero = l.empleado
        WHERE e.tipo_empleado = 2   

<<<<<<< HEAD
-- 1) 
-- 2) Observaciones realizada en la `bitacora`
-- num bitacora, num observacion, descripcion
SELECT b.numero AS 'No Bitacora',o.numero AS 'No Observacion',o.descripcion AS 'Descripcion'
FROM bitacora AS b
INNER JOIN observacion AS o ON o.bitacora = b.numero
ORDER BY b.numero

-- 3) consultar tipo de licencia requerida para cada `vehiculo`
-- matricla, marca, modelo, proposito, tipo de `licencia`
SELECT matricula, marca, modelo, proposito
FROM `vehiculo` as v
INNER Join `tipo_licencia` as tl on tl.codigo = v.licencia_requerida
=======

-- CONSULTAS PROFE CLEO --
-- 1. Información completa de una bitácora de salida
/*
- Información completa de una bitácora de salida
a. Nombre completo del empleado, en una columna, que levantó la
solicitud.
b. Nombre completo del empleado, en una columna, que autorizó la
solicitud.
c. Nombre del destino
d. Descripción del asunto
e. Fecha de salida
f. Hora de salida
g. Kilometraje de salida
h. Cantidad de gasolina en la salida
i. Fecha de entrada
j. Hora de entrada
k. Kilometraje de entrada
l. Cantidad de gasolina en la entrada
m. Lista de empleados registrados para una bitácora.
n. Matrícula del vehículo asignado.
o. Nombre de la marca del vehículo.
p. Nombre del modelo del vehículo.
*/
SELECT 
    CONCAT(soli.nombrePila, ' ', soli.apdPaterno, ' ', soli.apdMaterno) AS Solicitante,
    CONCAT(aut.nombrePila, ' ', aut.apdPaterno, ' ', aut.apdMaterno) AS Autorizador,
    bit.destino AS Destino,
    bit.asunto AS Asunto,
    DATE_FORMAT(bit.fechaSalida, "%d-%m-%Y") AS FechaSalida,
    DATE_FORMAT(bit.horaSalida, "%H:%M:%S") AS HoraSalida,
    bit.kmSalida AS KilometrajeSalida,
    bit.gasSalida AS GasolinaSalida,
    DATE_FORMAT(bit.fechaEntrada, "%d-%m-%Y") AS FechaEntrada,
    DATE_FORMAT(bit.horaEntrada, "%H:%M:%S") AS HoraEntrada,
    bit.kmEntrada AS KilometrajeEntrada,
    bit.gasEntrada AS GasolinaEntrada,
    CONCAT(em.nombrePila, ' ', em.apdPaterno, ' ', em.apdMaterno) AS Empleado,
    vehi.matricula AS Matricula,
    mar.nombre AS Marca,
    mol.nombre AS Modelo
FROM bitacora AS bit
INNER JOIN solicitud AS sol ON bit.solicitud = sol.numero
INNER JOIN empleado AS aut ON sol.autorizador = aut.numero
INNER JOIN empleado AS soli ON sol.solicitante = soli.numero
INNER JOIN vehiculo AS vehi ON bit.vehiculo = vehi.numSerie
LEFT JOIN marca AS mar ON vehi.marca = mar.codigo
LEFT JOIN modelo AS mol ON vehi.modelo = mol.codigo
LEFT JOIN empleado_bitacora AS eb ON eb.bitacora = bit.numero
LEFT JOIN empleado AS em ON eb.empleado = em.numero
WHERE bit.numero = 5

-- 2. Observaciones realizadas en una bitácora.
/*
a. Número de la bitácora.
b. Número de la observación.
c. Descripción 
*/

SELECT 
    bi.numero AS Bitacora,
    ob.numero AS Observacion,
    ob.descripcion AS Descripcion
FROM bitacora AS bi
INNER JOIN observacion AS ob ON ob.bitacora = bi.numero
WHERE bi.numero = 1

/* 3. Tipo de licencia que requiere cada vehículo
a. Matrícula del vehículo
b. Nombre de la marca del vehículo
c. Nombre del modelo del vehículo
d. Propósito del vehículo
e. Clase del tipo de licencia
*/
SELECT 
    vehi.matricula AS Matricula,
    mar.nombre AS Marca,
    mol.nombre AS Modelo,
    vehi.proposito AS Proposito,
    CONCAT("Clase", " ", tl.codigo) AS Licencia
FROM vehiculo AS vehi
INNER JOIN tipo_licencia AS tl ON vehi.licencia_requerida = tl.codigo
INNER JOIN marca AS mar ON vehi.marca = mar.codigo
INNER JOIN modelo AS mol ON vehi.modelo = mol.codigo

/*
4. Reporte de mantenimiento de un vehículo.
a. Matrícula del vehículo
b. Nombre de la marca del vehículo
c. Nombre del modelo del vehículo
d. Fecha
e. Razón
f. Comentarios
g. Descripción del tipo de mantenimiento
h. Descripción del tipo de observación
i. Descripción del estado de mantenimiento
*/

SELECT 
>>>>>>> 5412c0423be30d91f0919d98d553d77c36f9200d
