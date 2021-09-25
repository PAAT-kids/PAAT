"""
FILENAME: paatSecurity
AUTHOR: Majid Jafar
PURPOSE: Contains all the important security aspect of the program
DATE CREATED: 22/09/2021
LAST EDITED DATE: 22/09/2021
"""
import bcrypt
import re
#run "pip install bcrypt" in terminal


"""
FUNCTION NAME: passHash
PURPOSE: Hashes the imported string value
INPUT: String password
OUTPUT: Bit String hashPassword
"""
def passHash (password):
    passwordBits = password.encode("utf-8")
    hashedPassword = bcrypt.hashpw(passwordBits, bcrypt.gensalt())
    return hashedPassword


"""
FUNCTION NAME: comparePass
PURPOSE: Compares the given input to the hashvalue from the database
INPUT: String password , Bit String dbPassword
OUTPUT: Boolean
"""
def comparePass (password,dbPassword):
    passwordBits = password.encode("utf-8")
    
    if bcrypt.checkpw(passwordBits, dbPassword):
        return True
    else:
        return False


"""
FUNCTION NAME: validateUsername
PURPOSE: Checks the given username for validity
INPUT: String userName
OUTPUT: int (1: Length Error , 2: Symbols Error, 3: Not unique)
"""
def validateUsername (username):
    #Checking username length (4-15)
    if len(username) < 4:
        return 1
    elif len(username) > 15:
        return 1

    #Checking for only Alpha Numeric symbols
    if username.isalnum() == False:
        return 2

    #Checking if the username is unique
    #TODO: Wait for database completion

    return 0

"""
FUNCTION NAME: validatePassword
PURPOSE: Checks the given password for validity
INPUT: String pass
OUTPUT: Boolean ( True: is valid, False: not valid)
AUTHOR: Samrah Tahir
"""
def validatePassword(passW):
	
	if(len(passW)<8):
	#check if pass < 8
		return False
	elif not re.search("[A-Z]", passW):
	#check if pass contains atleast 1 Uppercase
		return False
	elif not re.search("[a-z]", passW):
	#check if pass contains lowercase
		return False
	elif not re.search("[0-9]", passW):
	#check if pass contains numbers
		return False
	elif not re.search("[_@$*+-]", passW):
	#check if pass contains special characters
		return False
	elif re.search("\s", passW):
	#check if pass contains space (should not)
		return False
	
	return True
		
		
		
