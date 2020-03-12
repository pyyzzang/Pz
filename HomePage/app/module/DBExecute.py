import pyodbc;

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Integer;
from sqlalchemy.orm import sessionmaker

class DBExecute():
    PYODBC = 0
    SQLALCHEMY = 1

    dbConnection="";
    dbMode = SQLALCHEMY;

    def InsertQueryExecute(self, query):
        pass
    def QueryExecute(self, query):
        pass

    @staticmethod 
    def ConvetHangul(encodeStr):
        if(DBExecute.SQLALCHEMY == DBExecute.dbMode):
            return encodeStr;

        encodeStr = encodeStr;
        encodeStr = encodeStr.encode('ISO-8859-1')
        return encodeStr.decode('euc-kr');

    @staticmethod
    def GetDBConnection(db = SQLALCHEMY):
        if("" != DBExecute.dbConnection):
            return DBExecute.dbConnection;

        dbMode = db;
        if( DBExecute.PYODBC == db):
            DBExecute.dbConnection = PyODBC();
        elif(DBExecute.SQLALCHEMY == db):
            DBExecute.dbConnection = SQLalchemy();
        return DBExecute.dbConnection;

class SQLalchemy(DBExecute):
    def __init__(self):
        self.engine = create_engine('mssql+pyodbc:///?odbc_connect=' + 'DRIVER%3D%7BFreeTDS%7D%3BSERVER%3Dpyyzzang.database.windows.net%3BPORT%3D1433%3BDATABASE%3DRaspberryPi%3BUID%3Dpyyzzang%3BPWD%3Dcndwn5069%28%29%3BTDS_Version%3D7.4%3B', pool_size=20, pool_recycle=500, max_overflow=5);

    def InsertQueryExecute(self, query):
        Session = sessionmaker(bind=self.engine)
        session = Session();
        session.execute(query);
        
    def QueryExecute(self, query):
        Session = sessionmaker(bind=self.engine)
        session = Session();
        return session.execute(query);

class PyODBC(DBExecute):
    def InsertQueryExecute(self, query):
        server ="pyyzzang.database.windows.net";
        database = "RaspberryPi";
        username = "pyyzzang";
        password = "cndwn5069()";
        driver = "{FreeTDS}";
        connectString = "DRIVER="+driver+";SERVER="+server+";PORT=1433;DATABASE="+database + ";UID="+username+";PWD="+ password + ";Encrypt=yes;Connection Timeout=30;TDS_Version=7.0";
        cnxn = pyodbc.connect(connectString);
        cursor = cnxn.cursor();
        cursor.execute(query);
        cnxn.commit();
        cnxn.close();

    def QueryExecute(self, query):
        server ="pyyzzang.database.windows.net";
        database = "RaspberryPi";
        username = "pyyzzang";
        password = "cndwn5069()";
        driver = "{FreeTDS}";
        connectString = "DRIVER="+driver+";SERVER="+server+";PORT=1433;DATABASE="+database + ";UID="+username+";PWD="+ password + ";Encrypt=yes;Connection Timeout=30;TDS_Version=7.0";
        cnxn = pyodbc.connect(connectString);
        cursor = cnxn.cursor();
        cursor.execute(query);
        rows = cursor.fetchall();
        return rows; 
    