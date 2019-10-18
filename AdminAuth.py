from core import *
import getpass, hashlib

#TODO: Request user data: (login, password)         +
#TODO: Check user data in database (file)           + save carConst
#TODO: Decrypt user password                        + sha256 sum password
#TODO: If user does exist then open the editor


def adminAuth():
    print(loginAdminPanelEng)

    while True:
        username = input(enterUsernameEng)
        password = getpass.getpass(enterPasswordEng)
        password = hashlib.sha256(password.encode())

        if username == 'root' and encryptedPassword == password.hexdigest():
            # srart editor
            print('NOT WORK | добовляй сам')
            break

        else:
            # !!! elif there were more than five data entry attempts, close the program + delit game
            print(dataIncorrectEng)
