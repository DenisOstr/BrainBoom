import getpass, hashlib

from core import *

#TODO: Request user data: (login, password)
#TODO: Check user data in database (file)
#TODO: Decrypt user password
#TODO: If user does exist then open the editor

def authentication():
    setLanguage('loginAdminPanel')

    while True:
        setLanguage('enterUsername')
        username = input('> ')

        setLanguage('enterPassword')
        password = getpass.getpass('> ')

        if username == a_username and a_password == encrypt(password).hexdigest():
            editor = Editor()
            editor.mainMenu(username)
            break
        else:
            if username != a_username:
                print('User with such username is not found')
                continue
            elif a_password != encrypt(password).hexdigest():
                print('User with such password is not found')
                continue


def encrypt(pswd):
    return hashlib.sha256(pswd.encode())
