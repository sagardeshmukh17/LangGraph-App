import sqlite3
from config.settings import DB_NAME

def find_student(student_id):
    conn = sqlite3.connect(DB_NAME)

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    data = cursor.execute(
        "select * from students where student_id = ?",
        (student_id,)
    )
    return data.fetchone()
