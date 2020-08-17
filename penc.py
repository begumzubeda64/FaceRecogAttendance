import uuid
import hashlib
from model import insertAccount
from model import readAccount

def hash_password(password):
   # uuid is used to generate a random number of the specified password
   salt = uuid.uuid4().hex
   return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

def check_password(hashed_password, user_password):
   password, salt = hashed_password.split(':')
   return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

# username = input('Enter username: ')
# new_pass = input('Please enter a password: ')
# hashed_password = hash_password(new_pass)
# iacc = insertAccount(username, hashed_password)
# print('The string to store in the db is: ' + hashed_password)
# if iacc:
#    print("Inserted...")

# old_user = input("Enter username to check: ")
# old_pass = input('Now please enter the password again to check: ')
#
# racc = readAccount(old_user)
#
# if racc != "":
#    if check_password(racc, old_pass):
#       print('You entered the right password')
#    else:
#       print('Passwords do not match')
# else:
#    print("Invalid username")