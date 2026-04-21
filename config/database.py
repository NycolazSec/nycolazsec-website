import pymysql

class Database(object):
    def __init__(self):
        self.host = 'localhost',
        self.user = 'root',
        self.password = '',
        self.db = 'flask',


class Connection:
    def __init__(self):
        self.db = Database()
        self.connection = pymysql.connect(
            host=self.db.host,
            user=self.db.user,
            password=self.db.password,
            db=self.db.db,
            cursorclass=pymysql.cursors.DictCursor
        )

    def cursor(self):
        return self.connection.cursor()

    def commit(self):
        return self.connection.commit()

    def close(self):
        return self.connection.close()
    

class Query:
    def __init__(self):
        self.connection = Connection()
        self.cursor = self.connection.cursor()

    def execute(self, query, args=None):
        self.cursor.execute(query, args)
        self.connection.commit()
        return self.cursor

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.connection.close()

