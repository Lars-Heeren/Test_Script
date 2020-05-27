import mysql.connector

HOSTNAME = "127.0.0.1"
USERNAME = "root"
PASSWORD = ""
DB = "agile"


class DataBase:
    @staticmethod
    def connect_to_database():
        return mysql.connector.connect(
            host=HOSTNAME,
            user=USERNAME,
            passwd=PASSWORD,
            database=DB
        )

    @staticmethod
    def run_select_query(query):
        db = DataBase.connect_to_database()
        c = db.cursor()
        c.execute(query)
        result = c.fetchall()
        db.close()
        return result

    @staticmethod
    def run_other_query(query):
        db = DataBase.connect_to_database()
        c = db.cursor()
        c.execute(query)
        db.commit()
        db.close()
