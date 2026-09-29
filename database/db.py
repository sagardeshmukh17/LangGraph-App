import sqlite3
from config.settings import DB_NAME

# ==== initialize database

def initialize_database():
    connection = sqlite3.connect(DB_NAME)
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS students(
            student_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            course TEXT NOT NULL,
            fee_paid REAL NOT NULL,
            fee_due REAL NOT NULL,
            batch_time TEXT NOT NULL
        )
        """
    )
    connection.execute(
        """
        INSERT OR IGNORE INTO students
        (student_id, name, course, fee_paid, fee_due, batch_time)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            101,
            "Ravi Kumar",
            "GEN AI and Agentic AI with Python",
            9000,
            2500,
            "7:00 PM IST",
        )
    )
    connection.commit()
    connection.close()
    print("Database initialized successfully")

    # ==== call function
if __name__ == "__main__":
   initialize_database()