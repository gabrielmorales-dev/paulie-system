CREATE DATABASE paulie_db;
USE paulie_db;

CREATE TABLE establecimientos (
  id int PRIMARY KEY AUTO_INCREMENT,
  nombre varchar(255),
  tipo varchar(255),
  ubicacion varchar(255),
  telefono varchar(255),
  creado_at timestamp
);

CREATE TABLE usuarios (
  id int PRIMARY KEY AUTO_INCREMENT,
  establecimiento_id int,
  nombre varchar(255),
  email varchar(255) UNIQUE,
  password_hash varchar(255),
  rol varchar(255)
);

CREATE TABLE servicios (
  id int PRIMARY KEY AUTO_INCREMENT,
  establecimiento_id int,
  nombre varchar(255),
  descripcion text,
  precio_base decimal,
  capacidad_max int,
  idiomas_disponibles varchar(255),
  activo boolean DEFAULT true
);

CREATE TABLE reservas (
  id int PRIMARY KEY AUTO_INCREMENT,
  servicio_id int,
  usuario_id int,
  cliente_nombre varchar(255),
  nacionalidad varchar(255),
  idioma varchar(255),
  cantidad_personas int,
  comentarios_especiales text,
  fecha_inicio datetime,
  estado varchar(255) COMMENT 'pendiente, pagado, cancelado',
  total_monto decimal
);

CREATE TABLE conexiones_comerciales (
  id int PRIMARY KEY AUTO_INCREMENT,
  hotel_id int,
  tour_operadora_id int,
  estado_conexion varchar(255),
  comision_porcentaje decimal
);

ALTER TABLE usuarios ADD FOREIGN KEY (establecimiento_id) REFERENCES establecimientos (id);

ALTER TABLE servicios ADD FOREIGN KEY (establecimiento_id) REFERENCES establecimientos (id);

ALTER TABLE reservas ADD FOREIGN KEY (servicio_id) REFERENCES servicios (id);

ALTER TABLE reservas ADD FOREIGN KEY (usuario_id) REFERENCES usuarios (id);

ALTER TABLE conexiones_comerciales ADD FOREIGN KEY (hotel_id) REFERENCES establecimientos (id);

ALTER TABLE conexiones_comerciales ADD FOREIGN KEY (tour_operadora_id) REFERENCES establecimientos (id);

INSERT INTO establecimientos (nombre, tipo, ubicacion, telefono) 
VALUES ('Hotel Arenal Paradise', 'hotel', 'La Fortuna, San Carlos', '2479-0000');
INSERT INTO establecimientos (nombre, tipo, ubicacion, telefono) 
VALUES ('Arenal Rafting Co.', 'tour_operadora', 'Centro de La Fortuna', '2479-1111');
