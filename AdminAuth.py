import getpass, hashlib

from core import *

#TODO: Request user data: (login, password)
#TODO: Check user data in database (file)
#TODO: Decrypt user password
#TODO: If user does exist then open the editor

def authentication():
    print(loginAdminPanelEng)

    while True:
        username = input(enterUsernameEng)
        password = getpass.getpass(enterPasswordEng)

        if username == 'root' and encryptedPassword == encrypt(password).hexdigest():
            editor = Editor()
            editor.mainMenu()
            break
        else:
            print('This user does not exist!')
            continue


def encrypt(pswd):
    return hashlib.sha256(pswd.encode())
