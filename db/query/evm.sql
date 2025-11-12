-- query base para la creacion de la base de datos

CREATE DATABASE evm_db;
USE sys_evm_db;

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
    descripcion VARCHAR(20) NOT NULL
);

CREATE TABLE edo_solicitud (
    numero INT PRIMARY KEY AUTO_INCREMENT,
    descripcion VARCHAR(20) NOT NULL
);

CREATE TABLE tipo_empleado (
    codigo VARCHAR(5) PRIMARY KEY,
    descripcion VARCHAR(15) NOT NULL
);

CREATE TABLE tipo_licencia (
    codigo CHAR(1) PRIMARY KEY,
    descripcion VARCHAR(30) NOT NULL
);

CREATE TABLE tipo_mantenimiento (
    codigo VARCHAR(6) PRIMARY KEY,
    descripcion VARCHAR(20) NOT NULL
);

CREATE TABLE nvl_cobertura (
    numero INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(30)
);

CREATE TABLE aseguradora (
    codigo VARCHAR(6) PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL,
    nombreFiscal VARCHAR(60) NOT NULL UNIQUE
);

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

CREATE TABLE tipo_observacion (
    codigo VARCHAR(8) PRIMARY KEY,
    descripcion VARCHAR(20) NOT NULL,
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

CREATE TABLE telefono (
    numero INT AUTO_INCREMENT PRIMARY KEY,
    numTelefono VARCHAR(16) UNIQUE NOT NULL,
    empleado INT NOT NULL,
    FOREIGN KEY (empleado) REFERENCES empleado(numero)
);

CREATE TABLE licencia (
    numero VARCHAR(14),
    fechaExpedicion DATE NOT NULL,
    fechaVencimiento DATE NOT NULL,
    empleado INT NOT NULL,
    tipo_licencia CHAR(1) NOT NULL,
    FOREIGN KEY (empleado) REFERENCES empleado(numero),
    FOREIGN KEY (tipo_licencia) REFERENCES tipo_licencia(codigo)
);

CREATE TABLE vehiculo (
    numSerie VARCHAR(17) PRIMARY KEY,
    matricula VARCHAR(10) NOT NULL,
    proposito VARCHAR(20) NOT NULL,
    fechaAdquisicion DATE NOT NULL,
    marca VARCHAR(4) NOT NULL,
    modelo VARCHAR(4) NOT NULL,
    licenciaRequerida CHAR(1) NOT NULL,
    FOREIGN KEY (marca) REFERENCES marca(codigo), 
    FOREIGN KEY (modelo) REFERENCES modelo(codigo),
    FOREIGN KEY (licenciaRequerida) REFERENCES tipo_licencia(codigo)
);

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
    edoSolicitud INT NOT NULL, 
    solicitante INT NOT NULL,
    FOREIGN KEY (edoSolicitud) REFERENCES edo_solicitud(numero),
    FOREIGN KEY (vehiculo) REFERENCES vehiculo(numSerie),
    FOREIGN KEY (solicitante) REFERENCES empleado(numero)
);

CREATE TABLE bitacora (
    numControl INT PRIMARY KEY AUTO_INCREMENT,
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

CREATE TABLE empleado_bitacora (
    bitacora INT NOT NULL, 
    empleado INT NOT NULL,
    PRIMARY KEY(bitacora, empleado),
    FOREIGN KEY (empleado) REFERENCES empleado(numero),
    FOREIGN KEY (bitacora) REFERENCES bitacora(numControl)
);

CREATE TABLE observaciones (
    numero INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(60) NOT NULL,
    tipoObservacion VARCHAR(6) NOT NULL,
    bitacora INT NOT NULL,
    FOREIGN KEY (tipoObservacion) REFERENCES tipo_observacion(codigo),
    FOREIGN KEY (bitacora) REFERENCES bitacora(numControl)
);

CREATE TABLE nvl_importancia(
    numero INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(15)
);

CREATE TABLE mantenimiento(
    folio VARCHAR(20) PRIMARY KEY,
    razon VARCHAR(50) NOT NULL,
    fechaProgramada DATE NOT NULL,
    comentarios TEXT, 
    tipoMantenimiento VARCHAR(6) NOT NULL,
    importancia INT NOT NULL,
    vehiculo VARCHAR(17) NOT NULL,
    edoMantenimiento INT NOT NULL,
    FOREIGN KEY (tipoMantenimiento) REFERENCES tipo_mantenimiento(codigo),
    FOREIGN KEY (importancia) REFERENCES nvl_importancia(numero),
    FOREIGN KEY (vehiculo) REFERENCES vehiculo(numSerie),
    FOREIGN KEY (edoMantenimiento) REFERENCES edo_mantenimiento(numero)
);

