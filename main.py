import mysql.connector
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Azqsxwde240507",
        database="paulie_db"
    )

def registrar_establecimiento(nombre, tipo, ubicacion, telefono):
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        sql = "INSERT INTO establecimientos (nombre, tipo, ubicacion, telefono) VALUES (%s, %s, %s, %s)"
        valores = (nombre, tipo, ubicacion, telefono)
        cursor.execute(sql, valores)
        conexion.commit()
        print(f" {tipo.capitalize()} '{nombre}' registrado con éxito.")

    except Exception as e:
        print(f"Error al registrar: {e}")
    
    finally:
        cursor.close()
        conexion.close()

def añadir_servicio(establecimiento_id, nombre, descripcion, precio, capacidad, idiomas):
    conexion = conectar()
    cursor = conexion.cursor()
    
    try:
        sql = """
            INSERT INTO servicios (establecimiento_id, nombre, descripcion, precio_base, capacidad_max, idiomas_disponibles, activo)
            VALUES (%s, %s, %s, %s, %s, %s, 1)
        """
        valores = (establecimiento_id, nombre, descripcion, precio, capacidad, idiomas)
        
        cursor.execute(sql, valores)
        conexion.commit()
        print(f"Servicio '{nombre}' añadido con éxito.")
        
    except Exception as e:
        print(f"Error al añadir servicio: {e}")
    finally:
        cursor.close()
        conexion.close()

def consultar_tours_disponibles():
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)
    
    try:
        sql = """
            SELECT 
                s.nombre AS nombre_servicio, 
                s.precio_base, 
                s.capacidad_max, 
                s.idiomas_disponibles,
                e.nombre AS nombre_empresa,
                e.tipo AS tipo_empresa
            FROM servicios s
            JOIN establecimientos e ON s.establecimiento_id = e.id
            WHERE e.tipo = 'tour_operadora' AND s.activo = 1
        """
        cursor.execute(sql)
        tours = cursor.fetchall()
        
        print("\nTOURS DISPONIBLES EN LA FORTUNA")
        if not tours:
            print("No hay tours registrados por ahora.")
        else:
            for tour in tours:
                print(f"Tour: {tour['nombre_servicio']}") 
                print(f"   Operado por: {tour['nombre_empresa']}") 
                print(f"   Precio: ${tour['precio_base']} | Capacidad: {tour['capacidad_max']} personas")
                print("-" * 40)
                
    except Exception as e:
        print(f"Error al consultar tours: {e}")
    finally:
        cursor.close()
        conexion.close()

def crear_reserva(servicio_id, cliente, nacionalidad, idioma, personas):
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)
    
    try:
        #Se consulta el servicio, su disponibilidad y precio
        cursor.execute("SELECT nombre, capacidad_max, precio_base FROM servicios WHERE id = %s", (servicio_id,))
        servicio = cursor.fetchone()
        
        if not servicio:
            print("El servicio no existe.")
            return

        if servicio['capacidad_max'] < personas:
            print(f"No hay espacio suficiente. Solo quedan {servicio['capacidad_max']} cupos.")
            return

        #Se calcula el monto total
        total = servicio['precio_base'] * personas
        
        #Se inserta la reserva en la DB con el estado pendiente
        sql_reserva = """
            INSERT INTO reservas (servicio_id, cliente_nombre, nacionalidad, idioma, cantidad_personas, total_monto, estado)
            VALUES (%s, %s, %s, %s, %s, %s, 'pendiente')
        """
        cursor.execute(sql_reserva, (servicio_id, cliente, nacionalidad, idioma, personas, total))
        
        #Se actualiza la capacidad del servicio en la DB
        nueva_capacidad = servicio['capacidad_max'] - personas
        cursor.execute("UPDATE servicios SET capacidad_max = %s WHERE id = %s", (nueva_capacidad, servicio_id))
        
        conexion.commit()
        print(f"Reserva creada para {cliente}. Total a pagar: ${total}. Estado: PENDIENTE.")

    except Exception as e:
        conexion.rollback() #Si algo falla, deshace los cambios para no corromper la DB
        print(f"Error al crear reserva: {e}")
    finally:
        cursor.close()
        conexion.close()

if __name__ == "__main__":
    print("=== PAULIE SYSTEM v1.0 - San Carlos, Costa Rica ===")
    print("1. Consultar Tours")
    print("2. Salir")
    consultar_tours_disponibles()