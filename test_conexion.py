import mysql.connector

try:
    # 1. Establecer la conexión
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Azqsxwde240507",
        database="paulie_db"
    )

    if conexion.is_connected():
        print("¡Conexión exitosa! Paulie ya tiene acceso a la base de datos.")
        
        # 2. Consultar qué tablas hay
        cursor = conexion.cursor()
        cursor.execute("SHOW TABLES;")
        
        tablas = cursor.fetchall()
        print("Tablas encontradas en la base de datos:")
        for tabla in tablas:
            print(f"- {tabla[0]}")

except Exception as e:
    print(f"Error al conectar: {e}")

finally:
    if 'conexion' in locals() and conexion.is_connected():
        conexion.close()
        print("Conexión cerrada.")