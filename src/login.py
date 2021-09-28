import mysql.connector as sql


class connections:
    __HOST = 'localh`o`st'
    __USERNAME = 'root'
    __PASSWORD = ''
    __DATABASE = 'testing'
    
    def __init__(self):
        self.con = sql.connect(host=connections.__HOST,user=connections.__USERNAME,password=connections.__PASSWORD,database=connections.__DATABASE)


    def connect_database(self,username,password):
        queue = []
        #if check(email) == True:

        sql_query = "SELECT *FROM users WHERE username ='%s' AND password ='%s'" % (username, password)
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
            print('User name exists')

        self.con.close()


#root = connections()
#root.connect_database('Anas','1234')


