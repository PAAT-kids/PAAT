import bcrypt
#run "pip install bcrypt" in terminal

def passHash (password):
    passwordBits = password.encode("utf-8")
    hashedPassword = bcrypt.hashpw(passwordBits, bcrypt.gensalt())
    return hashedPassword

def compPass (password,dbPassword):
    passwordBits = password.encode("utf-8")
    
    if bcrypt.checkpw(passwordBits, dbPassword):
        return True
    else:
        return False


