import MySQLdb

def conectar ():
    return MySQLdb.connect(host="localhost", user="pythonuser", passwd="Pruba123!", db="db_chelis")

def crear_tabla():
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("""CREATE TABLE IF NOT EXISTS inventario (id INT AUTO_INCREMENT PRIMARY KEY,
                                                                    nombre VARCHAR(100) NOT NULL,
                                                                    pz INT NOT NULL,
                                                                    precio DECIMAL (10, 2) NOT NULL)""")
        conn.commit()
    except MySQLdb.Error as e:
        conn.rollback()
        print("Error al crear la tabla:", e)
    finally:
        cursor.close()
        conn.close()

#CRUD + MySQL + PYTHON for server
#CREATE
def create_item (nombre, pz, precio):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO inventario (nombre, pz, precio) VALUES (%s, %s, %s)', (nombre, pz, precio))
    conn.commit()
    conn.close()
    print("item creado")

#READ
def read_iteam():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM inventario')
    resultados = cursor.fetchall()
    conn.close()
    for fila in resultados:
        print(fila)

#UPDATE
def update_item(id_elemento, nuevo_nombre, nueva_pz, nuevo_precio):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('UPDATE inventario SET Nombre = %s, pz = %s, precio = %s WHERE id = %s', (nuevo_nombre, nueva_pz, nuevo_precio, id_elemento))
    conn.commit()
    conn.close()
    print("Item actualizado.")

#DELETE
def delete_item(id_elemento):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM inventario WHERE id = %s', (id_elemento,))
    conn.commit()
    conn.close()
    print("Item eliminado.")

#MENU DE OPCIONES PARA CRUD SEGUN server_2
def menu():
    while True:
        print("\n1. CREATE ITEM \n2. READ ITEM \n3. UPDATE ITEM \n4. DELETE ITEM \n5. EXIT")
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            nombre = input("Nombre: ")
            pz = input("No. Piezas: ")
            precio = input("Precio : S  ")
            create_item (nombre, pz, precio)
        
        elif opcion == '2':
            read_iteam()
        
        elif opcion == '3':
            id_elemento = int(input("ID del producto a actualizar: "))
            nuevo_nombre  = input("Nuevo Nombre: ")
            nueva_pz  = input("Nueva pz: ")
            nuevo_precio  = input("Nuevo precio $: ")
            update_item(id_elemento, nuevo_nombre, nueva_pz, nuevo_precio)
        
        elif opcion == '4':
                    id_elemento = int(input("ID del producto a eliminar: "))
                    delete_item(id_elemento)

        elif opcion == '5':
            print("Bye")
            break
        

if __name__ == "__main__":
 #create_table()
    menu()
