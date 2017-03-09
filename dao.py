import MySQLdb  
  
class Singleton(object):  
    _instance = None  
    def __new__(cls, *args, **kwargs):  
        if not cls._instance:  
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)  
        return cls._instance  

  
class DAO(Singleton):  
    def __init__(self):  
        self._connect()  
        return  
  
  
    def _connect(self):   
        self.connection = MySQLdb.connect(host="infoweb", \
            user="E155530E", \
            passwd="E155530E", \
            db="E155530E")  
        return  
  
  
    def _get_cursor(self):  
        try:  
            self.connection.ping()  
        except:  
            self._connect()  
        return self.connection.cursor()  
  
  
    def get_row(self, query): 
        cursor = self._get_cursor()  
        cursor.execute(query)  
        row = cursor.fetchone()  
        cursor.close()  
        return row  
  
  
    def get_rows(self, query):   
        cursor = self._get_cursor()  
        cursor.execute(query)  
        rows = cursor.fetchall()  
        cursor.close()  
        return rows  
  
  
    def execute(self, query):   
        cursor = self._get_cursor()  
        cursor.execute(query) 
        self.connection.commit() 
        cursor.close()  
        return  