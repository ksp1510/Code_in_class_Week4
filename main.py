import sqlite3
from sqlite3 import Error


def db_connect(db_file_name):
      # print(sqlite3.version)
      conn = sqlite3.connect(db_file_name)
      # conn = sqlite3.connect(':memory:')
      # print(conn)
      return conn


def create_tables(conn):
      stu_table = """CREATE TABLE IF NOT EXISTS student
                        (sid INT PRIMARY KEY, 
                        sname TEXT NOT NULL);"""

      cursor = conn.cursor()
      cursor.execute(stu_table)


def insert_data(conn, sid, sname):
      sql = "INSERT INTO student VALUES(?, ?)"
      cur = conn.cursor()
      cur.execute(sql, (sid, sname))
      conn.commit()

def select_data(conn):
      sql = "SELECT * FROM student"
      cur = conn.cursor()
      cur.execute(sql)

      dataRows = cur.fetchall()
      for row in dataRows:
            print(row)


if __name__ == '__main__':
      print(sqlite3.version)
      conn = db_connect("student.db")
      print(conn)
      create_tables(conn)
      insert_data(conn, 1, "Kishan")
      select_data(conn)
