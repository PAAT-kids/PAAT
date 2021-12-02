import mysql.connector as sql
import paatSecurity
import login_su


class connections:
    __HOST = '127.0.0.1'
    __USERNAME = 'PAAT'
    __PASSWORD = '1234'
    __DATABASE = 'paat'
    
    def __init__(self):
        self.con = sql.connect(host=connections.__HOST,user=connections.__USERNAME,password=connections.__PASSWORD,database=connections.__DATABASE)



    def connect_database(self,username,password):

        sql_query = "SELECT UserPassword FROM Users WHERE Username ='%s'" % (username) #retrieve password by matching the entered username to the one in DB

        mycursor = self.con.cursor()

        try:

             mycursor.execute(sql_query)
             hashedPassword = mycursor.fetchone() 
        except:
             print('error occured')
        if paatSecurity.comparePass(password,hashedPassword[0]) == True: #compare entered pass wot hashed pass, hashedPassword[0] because ince a tuple is returned, we only need the first value
            print('match')
            self.con.close()
            return True
        else:
            print('no match')
            self.con.close()
            return False


    def getEmail(self,username):
        email = ""
        sql_query = "SELECT Email FROM Users WHERE Username ='%s'" % (username) #retrieve password by matching the entered username to the one in DB

        mycursor = self.con.cursor()
        print(username)

        try:

             mycursor.execute(sql_query)
             email = mycursor.fetchone() 
             return email[0]
        except:
            print('error occured')
            print('match')
            self.con.close()







