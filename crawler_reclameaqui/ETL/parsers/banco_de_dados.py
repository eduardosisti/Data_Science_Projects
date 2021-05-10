import psycopg2 as pc2
import os
import pandas as pd

class banco_de_dados(object):
    _db = None
    def __init__(self):
        self.host = os.getenv('DB_SERVICE_NAME')
        self.database = os.getenv('DB_DATABASE')
        self.username = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASS')
        self.port = os.getenv('DB_PORT')
        self._db = pc2.connect(host=self.host, database=self.database, user=self.username,  password=self.password)

    def consultar(self, sql):
        rs = None
        try:
            cur = self._db.cursor()
            cur.execute(sql)
            rs = cur.fetchall()
            rs = pd.DataFrame(rs)
        except:
            return None
        return rs

    def fechar(self):
        self._db.close()