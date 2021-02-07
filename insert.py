import psycopg2

def insert_TEMPERATURE(hora, temperatura):
    sql = """ INSERT INTO TEMPERATURE(hora, temperatura) VALUES (%s, %s);"""
    
    conn = None
    
    try:
        conn = psycopg2.connect(
        host="localhost",
        port="5432",
        user="postgres",
        database="ExamenII",
        password="123456")
        
        cur = conn.cursor()
        
        cur.execute(sql, (hora, temperatura))
        
        conn.commit()
        cur.close()

        if conn is not None:
            conn.close()
               
    except (Exception, psycopg2.DatabaseError) as e:
        print(e)
    
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    pass