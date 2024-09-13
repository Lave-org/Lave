import mysql.connector

class Database:
    @staticmethod
    def conn():
        config = {
            'user': 'lave',
            'password': '',  # Ensure to fill in your password
            'host': 'localhost',
            'database': 'Lave',
        }
        return mysql.connector.connect(**config)

    @staticmethod
    def query_user(username, password):
        conn = Database.conn()
        if conn:
            try:
                cursor = conn.cursor()
                sql = "SELECT * FROM user WHERE username = %s AND password = %s"
                values = (username, password)  # Tuple of values
                cursor.execute(sql, values)
                user_data = cursor.fetchone()
                return user_data
            finally:
                cursor.close()
                conn.close()
        return None
