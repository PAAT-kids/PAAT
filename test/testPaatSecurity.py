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
from paatSecurity import compPass, passHash

#Testing passHash
print("----------- TESTING passHash -----------\n")
print("Input: ThisIsMyPassword123\nExpected Output: ~RandomHashValue~\n")
print("Actual Output: ", passHash("ThisIsMyPassword123"))


#Testing compPass
print("\n----------- TESTING compPass -----------\n")

hashedPassword = bcrypt.hashpw("ThisIsMyPassword123".encode("utf-8") , bcrypt.gensalt())

#Expected output True
print("Input: ThisIsMyPassword123 , Hash of (ThisIsMyPassword123)\nExpected Output: True")
print("Actual Output: ", compPass("ThisIsMyPassword123", hashedPassword))

#Expected output False
print("\nInput: ThisIsNotMyPassword123 , Hash of (ThisIsMyPassword123)\nExpected output: False")
print("Actual Output: ", compPass("ThisIsNotMyPassword123", hashedPassword))