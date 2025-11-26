Create database solicitudes;
USE solicitudes;

CREATE TABLE vehiculo (
    numSerie VARCHAR(17) PRIMARY KEY,
    marca VARCHAR(20),
    modelo VARCHAR(20)
);

CREATE TABLE empleado (
    numero INT PRIMARY KEY,
    nombre VARCHAR(50)
);

CREATE TABLE edo_solicitud (
    numero INT PRIMARY KEY,
    estado VARCHAR(20)
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
    FOREIGN KEY (vehiculo) REFERENCES vehiculo(numSerie),
    FOREIGN KEY (edo_solicitud) REFERENCES edo_solicitud(numero),
    FOREIGN KEY (solicitante) REFERENCES empleado(numero),
    FOREIGN KEY (autorizador) REFERENCES empleado(numero)
);

INSERT INTO vehiculo (numSerie, marca, modelo)
VALUES
('1HGCM82633A004352', 'Honda', 'Civic'),
('2FACP71W4LX155788', 'Ford', 'Mustang'),
('3VWFE21C04M000001', 'Volkswagen', 'Jetta');

INSERT INTO empleado (numero, nombre)
VALUES
(1, 'Juan Pérez'),
(2, 'María López'),
(3, 'Carlos Hernández');

INSERT INTO edo_solicitud (numero, estado)
VALUES
(1, 'Pendiente'),
(2, 'Aprobada'),
(3, 'Rechazada');

INSERT INTO solicitud (
    asunto,
    horaSolicitada,
    fechaSolicitada,
    vehiculo,
    edo_solicitud,
    solicitante,
    autorizador
)
VALUES
('Salida a reunión', '10:30:00', '2025-01-12', '1HGCM82633A004352', 1, 1, 2),
('Entrega de documentos', '14:00:00', '2025-01-13', '2FACP71W4LX155788', 2, 2, 3),
('Supervisión', '08:00:00', '2025-01-14', '3VWFE21C04M000001', 1, 3, 1);

ALTER TABLE solicitud
MODIFY solicitante VARCHAR(100) NOT NULL;

ALTER TABLE solicitud
MODIFY autorizador VARCHAR(100) NOT NULL;

ALTER TABLE solicitud
DROP FOREIGN KEY solicitud_ibfk_2;  -- FK del solicitante

ALTER TABLE solicitud
DROP FOREIGN KEY solicitud_ibfk_4;  -- FK del autorizador

INSERT INTO solicitud (
    asunto, horaSolicitada, fechaSolicitada,
    vehiculo, edo_solicitud, solicitante, autorizador
)
VALUES
('Salida a reunión', '10:30:00', '2025-01-12', '1HGCM82633A004352', 1, 'Juan Pérez', 'María López'),
('Entrega de documentos', '14:00:00', '2025-01-13', '2FACP71W4LX155788', 2, 'María López', 'Carlos Hernández'),
('Supervisión', '08:00:00', '2025-01-14', '3VWFE21C04M000001', 1, 'Carlos Hernández', 'Juan Pérez');

CREATE TABLE solicitud (
    numero INT AUTO_INCREMENT PRIMARY KEY,
    asunto VARCHAR(50) NOT NULL,
    horaSolicitada TIME NOT NULL,
    fechaSolicitada DATE NOT NULL,
    vehiculo VARCHAR(17) NOT NULL,
    edo_solicitud VARCHAR(50) NOT NULL,    
    solicitante VARCHAR(100) NOT NULL,      
    autorizador VARCHAR(100) NOT NULL,      
    FOREIGN KEY (vehiculo) REFERENCES vehiculo(numSerie)
);

INSERT INTO solicitud (
    asunto,
    horaSolicitada,
    fechaSolicitada,
    vehiculo,
    edo_solicitud,
    solicitante,
    autorizador
)
VALUES (
    'Viaje a reunión',
    '10:30:00',
    '2025-03-01',
    '1HGCM82633A004352',
    'Pendiente',
    'Juan Pérez',
    'María López'
);


DROP table solicitud;
ALTER TABLE vehiculo
ADD id INT AUTO_INCREMENT PRIMARY KEY FIRST;

ALTER TABLE vehiculo DROP PRIMARY KEY;

ALTER TABLE vehiculo 
ADD id INT AUTO_INCREMENT PRIMARY KEY FIRST;
