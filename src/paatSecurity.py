"""
FILENAME: paatSecurity
AUTHOR: Majid Jafar, Samrah Tahir, Ahmed larbi
PURPOSE: Contains all the important security aspect of the program
DATE CREATED: 22/09/2021
LAST EDITED DATE: 22/09/2021
"""
import bcrypt
import re
#run "pip install bcrypt" in terminal

reg = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

"""
FUNCTION NAME: passHash
PURPOSE: Hashes the imported string value
INPUT: String password
OUTPUT: Bit String hashPassword
AUTHOR: Majid Jafar
"""
def passHash (password):
    passwordBits = password.encode("utf-8")
    hashedPassword = bcrypt.hashpw(passwordBits, bcrypt.gensalt())
    return hashedPassword

"""
FUNCTION NAME: check
PURPOSE: checks the email
INPUT: Email string
OUTPUT: boolean
"""
def check(email):
 
    if(re.fullmatch(reg, email)):
        return True
 
    else:
        return False


"""
FUNCTION NAME: comparePass
PURPOSE: Compares the given input to the hashvalue from the database
INPUT: String password , Bit String dbPassword
OUTPUT: Boolean
AUTHOR: Majid Jafar
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
AUTHOR: Majid Jafar
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

"""
INPUT VALIDATION FOR SENDING PACKET

"""

"""
FUNCTION NAME: validateEthIP
PURPOSE: Checks the given Mac address for the correct format
INPUT: String ethIP
OUTPUT: Boolean ( True: is valid, False: not valid)
AUTHOR: Majid Jafar
"""
def validateEthIP(ethIP):
    regex = ("^([0-9A-Fa-f]{2}[:-])" +
             "{5}([0-9A-Fa-f]{2})|" +
             "([0-9a-fA-F]{4}\\." +
             "[0-9a-fA-F]{4}\\." +
             "[0-9a-fA-F]{4})$")

    compRegex = re.compile(regex)

    if(ethIP == None):
        return False
    
    if(re.search(compRegex,ethIP)):
        return True
    else:
        return False

"""
FUNCTION NAME: validateStringOnly
PURPOSE: Checks the given variables datatype and if it contains symbols
INPUT: unknown inputVar
OUTPUT: Boolean ( True: is valid, False: not valid)
AUTHOR: Majid Jafar
"""
def validateStringOnly(inputVar):

    if(isinstance(inputVar, str)):
        if(inputVar.isalnum()):
            return True
        else:
            return False
    else:
        return False

"""
FUNCTION NAME: validateIntOnly
PURPOSE: Checks the given variables datatype and if it contains symbols
INPUT: unknown inputVar
OUTPUT: Boolean ( True: is valid, False: not valid)
AUTHOR: Majid Jafar
"""
def validateIntOnly(inputVar):

    if(isinstance(inputVar, int)):
        if((inputVar < 9223372036854775807) & (inputVar > -9223372036854775806)):
            return True
        else:
            return False
    else:
        return False


print(type(0x024))
print(validateIntOnly("HI"))
print(validateIntOnly("34"))
print(validateIntOnly(34))
print(validateIntOnly(9223372036854775807))