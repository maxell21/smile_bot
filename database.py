import sqlite3

create_session_db = """
CREATE TABLE IF NOT EXISTS sessions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  start_time integer,
  end_time INTEGER);
"""

create_message_db = """
CREATE TABLE IF NOT EXISTS messages(
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  msg_time TEXT NOT NULL, 
  session_id TEXT NOT NULL, 
  message text NOT NULL,
  client_id integer,
  FOREIGN KEY (session_id) REFERENCES sessions (id)
);
"""

def init_database():
    connection = sqlite3.connect("sessions.db")
    cursor = connection.cursor()
    execute_query(connection, create_session_db)
    execute_query(connection, create_message_db)
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except:
        print("can't process query")