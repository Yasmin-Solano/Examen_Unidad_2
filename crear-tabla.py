import psycopg2

def crear_tablas():
    comandos = (
        """CREATE TABLE TEMPERATURE(
            hora TIME WITHOUT TIME ZONE,
            temperatura REAL NOT NULL
            )
        """,
    )
    
    conn = None
    
    try:
        conn = psycopg2.connect(
        host="localhost",
        port="5432",
        user="postgres",
        database="ExamenII",
        password="123456")

        print("iniciando coneccion")
        cur = conn.cursor()
        
        for comando in comandos:
            print("iniciando coneccion")
            cur.execute(comando)

            
        cur.close()
        conn.commit()

        if conn is not None:
            conn.close()
        print("terminando coneccion")          
    except (Exception, psycopg2.DatabaseError) as e:
        print(e)
    
    finally:
        if conn is not None:
            conn.close()
            print("fin")
if __name__ == "__main__":
    crear_tablas()