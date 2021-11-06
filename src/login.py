import mysql.connector as sql
import paatSecurity
import login_su


class connections:
    __HOST = '127.0.0.1'
    __USERNAME = 'ahmed'
    __PASSWORD = '1234'
    __DATABASE = 'paat'
    
    def __init__(self):
        self.con = sql.connect(host=connections.__HOST,user=connections.__USERNAME,password=connections.__PASSWORD,database=connections.__DATABASE)


    def connect_database(self,username,password):
        queue = []

        sql_query = "SELECT *FROM users WHERE Username ='%s' AND UserPassword ='%s'" % (username, password)
        mycursor = self.con.cursor()

        try:
            mycursor.execute(sql_query)
            results = mycursor.fetchall()
            for row in results:
                for i in row:
                    queue.append(i)
        except:
            print('error occured')

        if (username and password) in queue:
            return True
        else:
            print(username)
            print(password)

        self.con.close()







