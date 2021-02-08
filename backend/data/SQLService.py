#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad
import os
import psycopg2
from backend.util import config

"""
SQLService :

This is the class handling all the database operations.
The database informations are found in environment variables.
"""


class SQLService:

    """
    Constructor :

    Attributes : username, password, address, port, dbname, sql, cursor
    """
    def __init__(self):
        self.username = os.getenv("DB_USERNAME")
        self.password = os.getenv("DB_PW")
        self.address = os.getenv("DB_URL")
        self.port = os.getenv("DB_PORT")
        self.dbname = os.getenv("DB_NAME")
        print(self.username)

        try:
            self.sql = psycopg2.connect(database=self.dbname,
                                        user=self.username,
                                        host=self.address,
                                        password=self.password,
                                        port=self.port)
        except:
            print("Database connection problem")
        else:
            self.cursor = self.sql.cursor()

    """
    Destructor :
    
    Closes the connection
    """
    def __del__(self):
        self.sql.close()

    """This method returns the rows found by the query"""
    def issueQueryWithResult(self, query: str):
        cursor = self.sql.execute(query)
        return cursor.fetchall()

    """
    This method only issue a query to the db, without returning anything. 
    It will be used for update/delete opoerations
    """
    def issueQueryUpdate(self, query: str):
        cursor = self.sql.execute(query)
        try:
            cursor.commit()
        except:
            print("sql exception (commit cursor)")
