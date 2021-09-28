import mysql.connector
from mysql.connector import Error
from paatSecurity import passHash, validatePassword, validateUsername, check

"""
FUNCTION NAME: signup
PURPOSE: signing up user
INPUT: String pass
OUTPUT: none
AUTHOR: Samrah Tahir
"""

def signup(email, username, password):

	if validateUsername(username) == 0:
		print('username valid')
		if validatePassword(password):
			print('password valid')
			hashedPassword = passHash(password)
			#email validation
			if check(email):
				print('Email: ',email,'\nUsername: ',username,'\nPassword: ',password)
				#addNewUser(username, hashedPassword.decode('utf-8'), email)
			#else:
				#print('email not valid')
		#else:
			#print('password not valid')
	#else:
		#print('username not valid')


"""
FUNCTION NAME: addNewUser
PURPOSE: Adding user to database
INPUT: String userN, passw, email
OUTPUT: None
AUTHOR: Samrah Tahir
"""

def addNewUser(userN, passw, email):

	#print(userN)
	#print(passw)
	#print(email)
	conn = connectToDatabase()
	cursor = conn.cursor()
	add_user = """insert into User(username,password,email) values(%s,%s,%s)"""
	cursor.execute(add_user, (userN, passw, email))
	conn.commit()
	#record = cursor.fetchone()
	#print(record)
	print('done')

"""
FUNCTION NAME: connectToDatabase
PURPOSE: connecting to database
INPUT: None
OUTPUT: connection (mysql object)
AUTHOR: Samrah Tahir
"""

def connectToDatabase():
	try:
		connection = mysql.connector.connect(host='192.168.231.173',database='paat',user='me',password='myUserpassword')

		print('connection complete')
	except Error as e:
		print('Error while connecting')

	return connection		

#main()