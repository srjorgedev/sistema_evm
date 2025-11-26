#nombre de la base de datos: examen
Create database examen

Use examen

#Tabla vehiculos
CREATE TABLE vehiculos (
    id_vehiculo INT PRIMARY KEY AUTO_INCREMENT,
    num_serie VARCHAR(17) NOT NULL UNIQUE,
    matricula VARCHAR(20) NOT NULL UNIQUE,
    marca VARCHAR(20) NOT NULL,
    modelo VARCHAR(30) NOT NULL,
    color VARCHAR(20) NOT NULL,
    tipo VARCHAR(20) NOT NULL,
    tipo_licencia VARCHAR(10) NOT NULL,
    capacidad_pasajeros INT NOT NULL,
    fecha_adquision DATE NOT NULL,
    utilidad VARCHAR(50) NOT NULL,
    comentarios VARCHAR(50) 
);

CREATE TABLE solicitudes (
    id_solicitud INT PRIMARY KEY AUTO_INCREMENT,
    id_vehiculo INT,
    fecha_solicitud DATE NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    destino VARCHAR(100) NOT NULL,
    motivo VARCHAR(100) NOT NULL,
    estado VARCHAR(20) NOT NULL,
    FOREIGN KEY (id_vehiculo) REFERENCES vehiculos(id_vehiculo)
)

INSERT INTO vehiculos (num_serie, matricula, marca, modelo, color, tipo, tipo_licencia, capacidad_pasajeros, fecha_adquision, utilidad, comentarios) VALUES
('1HGCM82633A123456', 'ABC123', 'Honda', 'Accord', 'Negro', 'Sedan', 'B', 5, '2020-01-15', 'Transporte ejecutivo', 'Buen estado')

INSERT INTO solicitudes 
(id_vehiculo, fecha_solicitud, fecha_inicio, fecha_fin, destino, motivo, estado)
VALUES 
(3, '2025-01-10', '2025-01-12', '2025-01-15', 'Madrid', 'Reunión ejecutiva', 'Pendiente');

