"""
FILENAME: testPaatSecurity
AUTHOR: Majid Jafar
PURPOSE: Testfile for paatSecurity.py
DATE CREATED: 22/09/2021
LAST EDITED DATE: 22/09/2021
"""

import bcrypt

#To Access the file in src directory
import sys
sys.path.insert(0, 'src')
from paatSecurity import comparePass, passHash, validateEthAddr, validateIPAddr, validateIntOnly, validateStringOnly, validateUsername

#Testing passHash
print("----------- TESTING passHash -----------\n")
print("Input: ThisIsMyPassword123\nExpected Output: ~RandomHashValue~\n")
print("Actual Output: ", passHash("ThisIsMyPassword123"))


#Testing comparePass
print("\n----------- TESTING comparePass -----------\n")

hashedPassword = bcrypt.hashpw("ThisIsMyPassword123".encode("utf-8") , bcrypt.gensalt())

#Expected output True
print("Input: ThisIsMyPassword123 , Hash of (ThisIsMyPassword123)\nExpected Output: True")
print("Actual Output: ", comparePass("ThisIsMyPassword123", hashedPassword))

#Expected output False
print("\nInput: ThisIsNotMyPassword123 , Hash of (ThisIsMyPassword123)\nExpected output: False")
print("Actual Output: ", comparePass("ThisIsNotMyPassword123", hashedPassword))

#Testing validateUsername
print("\n----------- TESTING validateUsername -----------\n")

#Expected output 0
print("\nInput: Yeeticus\nExpected Output: 0")
print("Actual Output: ", validateUsername("Yeeticus"))

#Expected output 1
print("\nInput: hi\nExpected Output: 1")
print("Actual Output: ", validateUsername("Hi"))

#Expected output 1
print("\nInput: abcdefghijklmnopqrstuvwxyz\nExpected Output: 1")
print("Actual Output: ", validateUsername("abcdefghijklmnopqrstuvwxyz"))

#Expected output 2
print("\nInput: @username\nExpected Output: 2")
print("Actual Output: ", validateUsername("@username"))

#Expected output 2
print("\nInput: user name\nExpected Output: 2")
print("Actual Output: ", validateUsername("user name"))

#Expected output 3
#TODO 



#Testing validateEthAddr
print("\n----------- TESTING validateEthAddr -----------\n")

#Expected output True
print("\nInput: f4:d1:08:0f:84:12\nExpected Output: True")
print("Actual Output: ", validateEthAddr("f4:d1:08:0f:84:12"))
#Expected output False
print("\nInput: Th:is:ma:ac:ad:re:ss\nExpected Output: False")
print("Actual Output: ", validateEthAddr("Th:is:ma:ac:ad:re:ss"))
#Expected output False
print("\nInput: \nExpected Output: False")
print("Actual Output: ", validateEthAddr(""))

#Testing validateIPAddr
print("\n----------- TESTING validateIPAddr -----------\n")

#Expected output True
print("\nInput: 192.168.0.130\nExpected Output: True")
print("Actual Output: ", validateIPAddr("192.168.0.130"))
#Expected output False
print("\nInput: no.t.Ip\nExpected Output: False")
print("Actual Output: ", validateIPAddr("no.t.Ip"))
#Expected output False
print("\nInput: \nExpected Output: False")
print("Actual Output: ", validateIPAddr(""))

#Testing validateStringOnly
print("\n----------- TESTING validateStringOnly -----------\n")

#Expected output True
print("\nInput: ThisisaTest\nExpected Output: True")
print("Actual Output: ", validateStringOnly("ThisisaTest"))
#Expected output False
print("\nInput: thi'swon'twork'\nExpected Output: False")
print("Actual Output: ", validateStringOnly("thi'swon'twork'"))
#Expected output False
print("\nInput: \nExpected Output: False")
print("Actual Output: ", validateStringOnly(""))

#Testing validateIntOnly
print("\n----------- TESTING validateStringOnly -----------\n")

#Expected output True
print("\nInput: 23\nExpected Output: True")
print("Actual Output: ", validateIntOnly(23))
#Expected output False
print("\nInput: 23(as a string)\nExpected Output: False")
print("Actual Output: ", validateIntOnly("23"))
#Expected output False
print("\nInput: 9223372036854775807\nExpected Output: False")
print("Actual Output: ", validateIntOnly(9223372036854775807))
#Expected output False
print("\nInput: \nExpected Output: False")
print("Actual Output: ", validateIntOnly(""))