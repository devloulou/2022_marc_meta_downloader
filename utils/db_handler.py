import psycopg2 as sql

class PostgreDB:

    def __init__(self):
        pass

    def get_connection(self):
        return sql.connect(user="postgres",
                            password="postgres",
                            host="localhost",
                            port=5432,
                            database="postgres")

    def insert_data(self, insert_script, data):
        with self.get_connection() as conn:
            with conn.cursor() as cur:
                try:
                    cur.execute(insert_script, data)
                except Exception as e:
                    conn.rollback()
                    return False, str(e)

        return True

    def run_sql(self, sql_script):
        with self.get_connection() as conn:
            with conn.cursor() as cur:
                try:
                    cur.execute(sql_script)                    
                except Exception as e:
                    conn.rollback()
                    return False, str(e)

                if sql_script[0:6].lower() == 'select':
                    return cur.fetchall()
        
        return True

if __name__ == '__main__':
    db = PostgreDB()

    val = db.run_sql("select 12")

    print(val)