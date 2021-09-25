"""
FILENAME: paatSecurity
AUTHOR: Majid Jafar
PURPOSE: Contains all the important security aspect of the program
DATE CREATED: 22/09/2021
LAST EDITED DATE: 22/09/2021
"""
import bcrypt
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


