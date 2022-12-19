import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def select_all_descuentos(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM descuentos")
    rows = cur.fetchall()
    # print(rows)
    return rows

def select_userid(conn,email):
    cur = conn.cursor()
    cur.execute("SELECT usuarioId FROM usuarios WHERE email= ?",email)
    row = cur.fetchone()
    return row

def select_tipoid(conn,tipo):
    cur = conn.cursor()
    cur.execute("SELECT tipoId FROM tipos WHERE descripcion= ?",tipo)
    row = cur.fetchone()
    return row

def select_descuento_porcentaje(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM descuento WHERE porcentaje = 25")
    rows = cur.fetchone()
    # print(rows)
    return rows


def update_descuento(conn, descuento):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' UPDATE descuentos
              SET porcentaje = ?
              WHERE descuentoId = ?'''
    cur = conn.cursor()
    cur.execute(sql, descuento)
    conn.commit()
    print("Valor actualizado correctamente")

def select_all_productos(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT productoId, codigo, nombre, precio, stock, tipos.descripcion, marca FROM productos INNER JOIN tipos ON tipos.tipoId = productos.tipoId WHERE stock > 0")
    rows = cur.fetchall()
    # print(rows)
    return rows

def select_all_tarjetas(conn,usrId):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT numero, banco, titular, fechaCaducidad FROM tarjetas WHERE usuarioId = ?", usrId)
    rows = cur.fetchall()
    # print(rows)
    return rows

def select_comprobanteId(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT MAX(comprobanteId) FROM comprobantes")
    rows = cur.fetchall()
    # print(rows)
    return rows

def select_all_comprobantes(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT 'F'||CO.tipo||' - '||CO.comprobanteId, CO.fecha, US.email, PR.codigo || ' - ' ||PR.nombre, DE.cantidad, DE.precio, CO.total FROM comprobantes AS CO INNER JOIN usuarios AS US ON US.usuarioId =co.usuarioId INNER JOIN detalles AS DE ON de.comprobanteId = co.comprobanteId INNER JOIN productos AS PR ON DE.productoId = PR.productoId ")

    rows = cur.fetchall()
    # print(rows)
    return rows    

def consulta_stock(conn,id):
    cur = conn.cursor()
    cur.execute("SELECT stock FROM productos WHERE productoId= ?",id)
    row = cur.fetchone()
    return row


def main():
    database = r"Supermark.db"
    # create a database connection
    conn = create_connection(database) 
    with conn:
        #print("Mostrar descuentos")
        #print(select_all_descuentos(conn))
        #print(select_all_tarjetas(conn,"5"))
        #print("Mostrar id de usuario según email")
        #print(select_userid(conn,("abelu89@gmail.com",)))
        #print(select_comprobanteId(conn))       
        #print(select_all_comprobantes(conn))
        print(consulta_stock(conn,"1"))

if __name__ == '__main__':
    main()
