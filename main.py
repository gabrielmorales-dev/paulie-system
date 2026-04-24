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

if __name__ == "__main__":
    print("Bienvenido a Paulie System")
    registrar_establecimiento("Hotel Selina Fortuna", "hotel", "Cerca del centro", "2479-1010")