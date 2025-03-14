import sqlite3
from contextlib import closing

try:
    with closing(sqlite3.connect('test.db')) as db_conn:
        db_conn.row_factory = sqlite3.Row
        with closing(db_conn.cursor()) as cursor:
            try:
                query_1 = "Select * from demo where id > 14"
                cursor.execute(query_1)
                rows = cursor.fetchall()
                print("Name of rows with id > 14")
                for row in rows:
                    print(row['name'])
            except Exception as e:
                print(f"Error Executing Query_1")
            #delete row based on user input
            try:
                del_row = int(input(" Enter the row ID threshold for deletion: "))
                query_2 = "Delete from demo where id < ?"
                cursor.execute(query_2, (del_row,))
                rows = cursor.fetchall()
                num_rows = cursor.rowcount
                print(f"{num_rows} rows deleted")
                db_conn.commit()
            except Exception as e:
                print(f"Error Executing Query_2")

except sqlite3.Error as e:
    print(f"Database Connection error: {e}")
