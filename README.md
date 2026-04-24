Paulie es un sistema backend desarrollado en Python y MySQL diseñado para centralizar la oferta turística y la gestión de reservas en la zona de La Fortuna, San Carlos. El proyecto permite a hoteles y operadoras gestionar inventarios de servicios en tiempo real, asegurando la integridad de los datos y la disponibilidad de los cupos.

- Características Principales
Gestión de Establecimientos: Registro y clasificación de hoteles y tour-operadoras.

Catálogo de Servicios Dinámico: Manejo de servicios (tours o habitaciones) vinculados a establecimientos específicos mediante llaves foráneas.

Sistema de Reservas: Lógica de negocio que procesa ventas, calcula montos totales y actualiza automáticamente la capacidad (stock) de los servicios.

Base de Datos Relacional: Estructura optimizada en MySQL con integridad referencial.

Consultas Avanzadas: Uso de JOINs para visualización detallada de la oferta comercial.

- Tecnologías Utilizadas
Lenguaje: Python 3.x

Base de Datos: MySQL

Conector: mysql-connector-python

Control de Versiones: Git & GitHub

- Estructura del Proyecto
main.py: Archivo principal con la lógica de conexión y funciones CRUD.

db_schema.sql: (Opcional, si lo creas) Script para recrear la estructura de tablas en MySQL.

.gitignore: Configuración para excluir archivos sensibles y entornos virtuales.

- Configuración e Instalación
Clonar el repositorio:

Bash
git clone https://github.com/TU_USUARIO/paulie-system.git
Instalar dependencias:

Bash
pip install mysql-connector-python
Configurar la Base de Datos:

Crear la base de datos paulie_db en MySQL.

Ejecutar la creación de tablas para establecimientos, servicios y reservas.

- Próximos Pasos (Roadmap)
[ ] Implementar una interfaz web con FastAPI.

[ ] Añadir manejo de fechas y temporadas para los precios.

[ ] Generación automática de comprobantes de reserva en PDF.

- Autor
Gabriel Morales – Estudiante de Ingeniería en Sistemas.
San Carlos, Alajuela, Costa Rica.
