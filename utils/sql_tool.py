import sqlite3

def run_sql(query: str):
    try:
        conn = sqlite3.connect("example.db")
        cur = conn.cursor()
        cur.execute(query)
        results = cur.fetchall()
        columns = [description[0] for description in cur.description]
        return columns, results
    except Exception as e:
        return ["Error"], [[str(e)]]
    finally:
        conn.close()
