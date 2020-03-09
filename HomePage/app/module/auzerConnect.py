import pyodbc;

class Auzer:
    @staticmethod
    def QueryExecute(query):
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