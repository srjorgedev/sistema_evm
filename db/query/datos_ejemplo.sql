INSERT INTO tipo_licencia (codigo, descripcion) VALUES
('A', 'Automovilista'),
('B', 'Chofer de Servicio Particular'),
('C', 'Licencia de Motociclista');

INSERT INTO marca (codigo, nombre) VALUES
('TOY', 'Toyota'),
('NIS', 'Nissan'),
('FOR', 'Ford'),
('CHE', 'Chevrolet'),
('VW', 'Volkswagen');

INSERT INTO modelo (codigo, nombre, periodo, marca) VALUES
('CORA', 'Corolla', 2023, 'TOY'),
('VERS', 'Versa', 2024, 'NIS'),
('FOCA', 'Focus', 2022, 'FOR'),
('BEAT', 'Beat', 2023, 'CHE'),
('VIRT', 'Virtus', 2024, 'VW'),
('HILU', 'Hilux', 2023, 'TOY'),
('FRON', 'Frontier', 2024, 'NIS');

INSERT INTO edo_mantenimiento (descripcion) VALUES
('Pendiente'),
('En Proceso'),
('Finalizado'),
('Cancelado');

INSERT INTO edo_solicitud (descripcion) VALUES
('Pendiente'),
('Aprobada'),
('Rechazada'),
('En Curso'),
('Finalizada');

INSERT INTO tipo_mantenimiento (codigo, descripcion) VALUES
('PREV', 'Preventivo'),
('CORR', 'Correctivo'),
('LAVA', 'Lavado y Limpieza');

INSERT INTO nvl_importancia (descripcion) VALUES
('Baja'),
('Media'),
('Alta'),
('Urgente');

INSERT INTO nvl_cobertura (descripcion) VALUES
('Limitada'),
('Amplia'),
('Premium/Total');

INSERT INTO tipo_empleado (codigo, descripcion) VALUES
('DRV', 'Conductor'),
('MEC', 'Mecánico'),
('ADM', 'Administrativo'),
('SUP', 'Supervisor');

INSERT INTO aseguradora (codigo, nombre, nombreFiscal) VALUES
('AXA', 'AXA Seguros', 'AXA Seguros, S.A. de C.V.'),
('GNP', 'GNP Seguros', 'Grupo Nacional Provincial, S.A.B.'),
('CHUBB', 'Chubb', 'Chubb Seguros México, S.A.');

INSERT INTO empleado (nombrePila, apdPaterno, apdMaterno, tipo_empleado) VALUES
('Juan', 'Pérez', 'Gómez', 'DRV'),
('María', 'López', 'Hernández', 'MEC'),
('Carlos', 'Ramírez', 'Ortiz', 'ADM'),
('Sofía', 'Torres', 'Mendoza', 'SUP'),
('Ricardo', 'Flores', 'Silva', 'DRV'),
('Ana', 'Castro', 'Rojas', 'ADM');

INSERT INTO telefono (numTelefono, empleado) VALUES
('+52 664-123-5678', 1),
('+52 664-234-6789', 2),
('+52 664-345-7890', 3),
('+52 664-456-8901', 4),
('+52 664-567-9012', 5);

INSERT INTO licencia (numero, fechaExpedicion, fechaVencimiento, empleado, tipo_licencia) VALUES
('MX123456789012', '2022-03-10', '2027-03-10', 1, 'B'),
('MX987654321098', '2023-01-20', '2028-01-20', 5, 'B'),
('MX112233445566', '2024-05-01', '2029-05-01', 4, 'A');

INSERT INTO seguro (numPoliza, fechaInicio, fechaVigencia, aseguradora, nvl_cobertura) VALUES
('POL-AXA-VEH-001234', '2024-01-01', '2025-01-01', 'AXA', 2),
('POL-GNP-VEH-005678', '2023-10-15', '2024-10-15', 'GNP', 3),
('POL-CHB-VEH-009012', '2024-06-20', '2025-06-20', 'CHUBB', 1);

INSERT INTO vehiculo (numSerie, matricula, proposito, fechaAdquisicion, marca, modelo, licenciaRequerida) VALUES
('JTDKARFP3J3084521', 'ABC-1234', 'Transporte interno', '2023-02-15', 'TOY', 'CORA', 'A'),
('3N1CN7AD0FL123456', 'XYZ-5678', 'Mensajería', '2024-05-10', 'NIS', 'VERS', 'A'),
('1FAPD4F58N5010999', 'DEF-9012', 'Uso Gerencial', '2022-11-20', 'FOR', 'FOCA', 'B'),
('9FADB4F58N5010111', 'GHI-3456', 'Carga Ligera', '2023-08-01', 'NIS', 'FRON', 'B'),
('3VWCN7AD0FL123111', 'JKL-7890', 'Inspección', '2024-01-05', 'VW', 'VIRT', 'A');

INSERT INTO vehiculo_seguro (vehiculo, seguro) VALUES
('JTDKARFP3J3084521', 1),
('3N1CN7AD0FL123456', 2),
('1FAPD4F58N5010999', 3),
('9FADB4F58N5010111', 2),
('3VWCN7AD0FL123111', 1);

INSERT INTO tipo_observacion (codigo, descripcion, tipo_mantenimiento) VALUES
('LI_EXT', 'Limpieza Exterior', 'LAVA'),
('RE_ACE', 'Revisión de Aceite', 'PREV'),
('RE_FRE', 'Revisión de Frenos', 'PREV'),
('FA_MOT', 'Falla de Motor', 'CORR'),
('PI_CRIS', 'Piel o Cristal Roto', 'CORR');

INSERT INTO solicitud (asunto, horaSolicitada, fechaSolicitada, vehiculo, edoSolicitud, solicitante) VALUES
('Traslado de documentos', '09:00:00', '2024-10-25', 'JTDKARFP3J3084521', 5, 3),
('Visita a almacén principal', '14:30:00', '2024-10-25', '3N1CN7AD0FL123456', 5, 4),
('Reunión de dirección', '08:00:00', '2024-10-28', '1FAPD4F58N5010999', 4, 6),
('Entrega de material', '10:00:00', '2024-10-29', '9FADB4F58N5010111', 2, 3),
('Calibración de equipo', '11:30:00', '2024-10-30', '3VWCN7AD0FL123111', 1, 6);

INSERT INTO bitacora (destino, asunto, horaSalida, horaEntrada, fechaSalida, fechaEntrada, gasSalida, gasEntrada, kmSalida, kmEntrada, kmTotal, kmPorLitro, salida, entrada, solicitud, vehiculo) VALUES
('Centro de Distribución', 'Traslado de documentos', '09:15:00', '11:45:00', '2024-10-25', '2024-10-25', 75.0, 68.5, 15200.5, 15290.5, 90.0, 13.85, TRUE, TRUE, 1, 'JTDKARFP3J3084521'),
('Almacén Central', 'Visita a almacén principal', '14:45:00', '17:00:00', '2024-10-25', '2024-10-25', 50.0, 45.0, 2890.0, 2965.0, 75.0, 15.0, TRUE, TRUE, 2, '3N1CN7AD0FL123456'),
('Oficinas Corporativas', 'Reunión de dirección', '08:15:00', NULL, '2024-10-28', NULL, 90.0, NULL, 4580.0, NULL, NULL, NULL, TRUE, FALSE, 3, '1FAPD4F58N5010999');

INSERT INTO empleado_bitacora (bitacora, empleado) VALUES
(1, 1),
(2, 5), 
(3, 4); 

INSERT INTO observaciones (descripcion, tipoObservacion, bitacora) VALUES
('Nivel bajo de líquido de frenos', 'RE_FRE', 1),
('Limpieza interior necesaria', 'LI_EXT', 2),
('Foco delantero izquierdo fundido', 'FA_MOT', 3);

INSERT INTO mantenimiento (folio, razon, fechaProgramada, comentarios, tipoMantenimiento, importancia, vehiculo, edoMantenimiento) VALUES
('MANT-PREV-001', 'Mantenimiento preventivo por kilometraje', '2024-11-15', 'Checar pastillas de freno y cambio de aceite.', 'PREV', 2, 'JTDKARFP3J3084521', 1),
('MANT-CORR-002', 'Falla reportada en la bitácora 3', '2024-11-05', 'Reemplazar foco delantero. Revisar cableado asociado.', 'CORR', 3, '1FAPD4F58N5010999', 2),
('MANT-LAVA-003', 'Limpieza y estética general', '2024-11-12', 'Limpieza profunda de tapicería.', 'LAVA', 1, '3N1CN7AD0FL123456', 3);

