-- query base para la creacion de la base de datos

CREATE DATABASE evm_db;

USE evm_db;

CREATE TABLE tipo_licencia (
    numero INT(15) PRIMARY KEY AUTO_INCREMENT,
    codigo CHAR(1) NOT NULL,
    descripcion VARCHAR(30) NOT NULL
);
ALTER TABLE tipo_licencia
DROP PRIMARY KEY;

ALTER TABLE tipo_licencia
ADD COLUMN numero INT NOT NULL AUTO_INCREMENT FIRST;

ALTER TABLE tipo_licencia
ADD PRIMARY KEY (numero);

SHOW CREATE TABLE tipo_licencia;

DROP TABLE tipo_licencia;


CREATE TABLE marca (
    codigo VARCHAR(4) PRIMARY KEY,
    nombre VARCHAR(30) NOT NULL
);

CREATE TABLE modelo (
    codigo VARCHAR(4) PRIMARY KEY,
    nombre VARCHAR(30) NOT NULL,
    periodo INT NOT NULL,
    marca VARCHAR(4) NOT NULL,
    FOREIGN KEY (marca) REFERENCES marca(codigo)
);

CREATE TABLE edo_mantenimiento (
    numero INT PRIMARY KEY AUTO_INCREMENT,
    descripcion VARCHAR(25) NOT NULL
);

CREATE TABLE edo_solicitud (
    numero INT PRIMARY KEY AUTO_INCREMENT,
    descripcion VARCHAR(20) NOT NULL
);

CREATE TABLE tipo_mantenimiento (
    codigo VARCHAR(6) PRIMARY KEY,
    descripcion VARCHAR(20) NOT NULL
);

CREATE TABLE nvl_importancia(
    numero INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(15)
);

CREATE TABLE nvl_cobertura (
    numero INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(15)
);

CREATE TABLE tipo_empleado (
    codigo VARCHAR(5) PRIMARY KEY,
    descripcion VARCHAR(15) NOT NULL
);

CREATE TABLE aseguradora (
    codigo VARCHAR(6) PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL,
    nombreFiscal VARCHAR(60) NOT NULL UNIQUE
);

CREATE TABLE tipo_observacion (
    codigo VARCHAR(8) PRIMARY KEY,
    descripcion VARCHAR(30) NOT NULL,
    tipo_mantenimiento VARCHAR(6) NOT NULL,
    FOREIGN KEY (tipo_mantenimiento) REFERENCES tipo_mantenimiento(codigo)
);

CREATE TABLE empleado (
    numero INT AUTO_INCREMENT PRIMARY KEY,
    nombrePila VARCHAR(30) NOT NULL,
    apdPaterno VARCHAR(20) NOT NULL,
    apdMaterno VARCHAR(20),
    tipo_empleado VARCHAR(5) NOT NULL,
    FOREIGN KEY (tipo_empleado) REFERENCES tipo_empleado(codigo)
);

SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE empleado;
SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE empleado(
    numero INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR (90) NOT NULL,
    tipo_empleado VARCHAR(5) NOT NULL,
    FOREIGN KEY (tipo_empleado) REFERENCES tipo_empleado(codigo)
);
ALTER TABLE empleado ADD activo TINYINT(1) NOT NULL DEFAULT 1;
ALTER TABLE empleado ADD COLUMN password_hash VARCHAR(255) NOT NULL;
ALTER TABLE empleado ADD COLUMN email VARCHAR(100) NOT NULL;

CREATE TABLE telefono (
    numero INT AUTO_INCREMENT PRIMARY KEY,
    numTelefono VARCHAR(16) UNIQUE NOT NULL,
    empleado INT NOT NULL,
    FOREIGN KEY (empleado) REFERENCES empleado(numero)
);

CREATE TABLE licencia (
    numero VARCHAR(14), #tendria que ser pk
    fechaExpedicion DATE NOT NULL,
    fechaVencimiento DATE NOT NULL,
    empleado INT NOT NULL,
    tipo_licencia INT NOT NULL,
    FOREIGN KEY (empleado) REFERENCES empleado(numero),
    FOREIGN KEY (tipo_licencia) REFERENCES tipo_licencia(numero)
);
SHOW CREATE TABLE licencia;

ALTER TABLE licencia
DROP FOREIGN KEY licencia_ibfk_2;

ALTER TABLE licencia
MODIFY tipo_licencia INT(15) NOT NULL;

ALTER TABLE licencia
ADD CONSTRAINT fk_tipoLicencia
FOREIGN KEY (tipo_licencia) REFERENCES tipo_licencia(numero);

DROP TABLE licencia;


CREATE TABLE seguro (
    numero INT AUTO_INCREMENT PRIMARY KEY,
    numPoliza VARCHAR(30) UNIQUE NOT NULL,
    fechaInicio DATE NOT NULL,
    fechaVigencia DATE NOT NULL,
    aseguradora VARCHAR(6) NOT NULL,
    nvl_cobertura INT NOT NULL,
    FOREIGN KEY (aseguradora) REFERENCES aseguradora(codigo),
    FOREIGN KEY (nvl_cobertura) REFERENCES nvl_cobertura(numero)
);

CREATE TABLE vehiculo (
    numSerie VARCHAR(17) PRIMARY KEY,
    matricula VARCHAR(12) NOT NULL,
    proposito VARCHAR(30) NOT NULL,
    fechaAdquisicion DATE NOT NULL,
    disponibilidad BOOLEAN DEFAULT TRUE,
    marca VARCHAR(4) NOT NULL,
    modelo VARCHAR(4) NOT NULL,
    licencia_requerida INT NOT NULL,
    FOREIGN KEY (marca) REFERENCES marca(codigo),
    FOREIGN KEY (modelo) REFERENCES modelo(codigo),
    FOREIGN KEY (licencia_requerida) REFERENCES tipo_licencia(numero)
);
SHOW CREATE TABLE vehiculo;
ALTER TABLE vehiculo
DROP FOREIGN KEY vehiculo_ibfk_3;
ALTER TABLE vehiculo
DROP FOREIGN KEY vehiculo_ibfk_2;
ALTER TABLE vehiculo
DROP FOREIGN KEY vehiculo_ibfk_1;

SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE vehiculo;
SET FOREIGN_KEY_CHECKS = 1;


DROP TABLE vehiculo;

CREATE TABLE vehiculo_seguro (
    vehiculo VARCHAR(17) NOT NULL UNIQUE,
    seguro INT NOT NULL,
    PRIMARY KEY(vehiculo, seguro),
    FOREIGN KEY (vehiculo) REFERENCES vehiculo(numSerie),
    FOREIGN KEY (seguro) REFERENCES seguro(numero)
);

CREATE TABLE solicitud (
    numero INT AUTO_INCREMENT PRIMARY KEY,
    asunto VARCHAR(50) NOT NULL,
    horaSolicitada TIME NOT NULL,
    fechaSolicitada DATE NOT NULL,
    vehiculo VARCHAR(17) NOT NULL,
    edo_solicitud INT NOT NULL,
    solicitante INT NOT NULL,
    autorizador INT NOT NULL,
    FOREIGN KEY (edo_solicitud) REFERENCES edo_solicitud(numero),
    FOREIGN KEY (vehiculo) REFERENCES vehiculo(numSerie),
    FOREIGN KEY (solicitante) REFERENCES empleado(numero),
    FOREIGN KEY (autorizador) REFERENCES empleado(numero)
);

CREATE TABLE bitacora (
    numero INT PRIMARY KEY AUTO_INCREMENT,
    destino VARCHAR(50) NOT NULL,
    asunto VARCHAR(50) NOT NULL,
    horaSalida TIME NOT NULL,
    horaEntrada TIME,
    fechaSalida DATE NOT NULL,
    fechaEntrada DATE,
    gasSalida FLOAT NOT NULL,
    gasEntrada FLOAT,
    kmSalida FLOAT NOT NULL,
    kmEntrada FLOAT,
    kmTotal FLOAT,
    kmPorLitro FLOAT,
    salida BOOLEAN NOT NULL DEFAULT TRUE,
    entrada BOOLEAN DEFAULT FALSE,
    solicitud INT NOT NULL,
    vehiculo VARCHAR(17) NOT NULL,
    FOREIGN KEY (solicitud) REFERENCES solicitud(numero),
    FOREIGN KEY (vehiculo) REFERENCES vehiculo(numSerie)
);

ALTER TABLE bitacora
ADD COLUMN visible BOOLEAN;

UPDATE bitacora
SET visible = 1;

CREATE TABLE empleado_bitacora (
    bitacora INT NOT NULL,
    empleado INT NOT NULL,
    PRIMARY KEY(bitacora, empleado),
    FOREIGN KEY (empleado) REFERENCES empleado(numero),
    FOREIGN KEY (bitacora) REFERENCES bitacora(numero)
);

CREATE TABLE observacion (
    numero INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(60) NOT NULL,
    tipo_observacion VARCHAR(6) NOT NULL,
    salida BOOLEAN,
    entrada BOOLEAN,
    bitacora INT NOT NULL,
    FOREIGN KEY (tipo_observacion) REFERENCES tipo_observacion(codigo),
    FOREIGN KEY (bitacora) REFERENCES bitacora(numero)
);

CREATE TABLE mantenimiento(
    folio VARCHAR(10) PRIMARY KEY,
    razon VARCHAR(50) NOT NULL,
    fechaProgramada DATE NOT NULL,
    comentarios TEXT,
    tipo_mantenimiento VARCHAR(6) NOT NULL,
    nvl_importancia INT NOT NULL,
    vehiculo VARCHAR(17) NOT NULL,
    edo_mantenimiento INT NOT NULL,
    FOREIGN KEY (tipo_mantenimiento) REFERENCES tipo_mantenimiento(codigo),
    FOREIGN KEY (nvl_importancia) REFERENCES nvl_importancia(numero),
    FOREIGN KEY (vehiculo) REFERENCES vehiculo(numSerie),
    FOREIGN KEY (edo_mantenimiento) REFERENCES edo_mantenimiento(numero)
);