import sqlite3

class Sql:

    conn = sqlite3.connect('StudentDB.db')
    c = conn.cursor()
    # creating table
    c.execute("CREATE TABLE IF NOT EXISTS Student("
              "StudentId INTEGER PRIMARY KEY AUTOINCREMENT, "
              "FirstName varchar(25) NOT NULL, "
              "LastName varchar(25) NOT NULL, "
              "GPA REAL NOT NULL, "
              "Major varchar(10) NOT NULL, "
              "FacultyAdviser varchar(25) NOT NULL);")

    conn.commit()