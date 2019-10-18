#!/usr/bin/env python3
import sys, random
from core import *

#TODO: set language
#TODO: loop
#TODO: update
#TODO: render


def languageSelection():
    print('Set language | Выберите язык')

    while True:
        lang = input('EN / RU: ')

        if lang == 'RU':
            global menuScreen
            menuScreen = '''\nВыберите:
    1) Нажмите клавишу S, чтобы начать игру
    2) Нажмите клавишу Q, чтобы выйти'''

            global menuSelectNotExists
            menuSelectNotExists = 'Данной функции не существует'


            break


        elif lang == 'EN':
            menuScreen = '''\nSelect:
    1) Press S key for Start the game
    2) Press Q key for Quit from the game'''

            menuSelectNotExists = 'This function does not exists'


            break

        else:
            print('xxxx')

def gameLoop():
    while True:
        print(menuScreen)
        userSelect = input('> ')

        if userSelect in menuSelect:
            if userSelect == menuSelect[0] or userSelect == menuSelect[1] or userSelect == menuSelect[2]:
                print('Start Game')
            elif userSelect == menuSelect[3] or userSelect == menuSelect[4] or userSelect == menuSelect[5]:
                sys.exit()

            # настройка языка в нутри игры

        elif userSelect in menuSelectForEditor:
            if userSelect == menuSelectForEditor[0]:
                adminAuth()



        else:
            print(menuSelectNotExists)
            continue


def update():
    pass


def render():
    languageSelection()
    gameLoop()

# def gameWin():
#     attempts += 1

#     print('\nТы справился, тебе добовляется 1 попытка, у тебя:', attempts)

#     return attempts


# def gameLose():
#     attempts -= 1
#     print('\nОтвет не верный, минуc 1 попытка, у тебя осталось:', attempts)

#     if attempts <= 0:
#         print('\nТы проиграл. :(')
#         # выход или предложение поиграть с точки сохранения
#         sys.exit()

#     return attempts


# def gameLevel_1():
#     print('\nЗадача 1')
#     print('''
#     8631 = 3
#     3625 = 1
#     9612 = 2
#     7831 = x''')

#     while True:
#         x = input('\nВведите значение x (int)\n> ')

#         if x == '2':
#             gameWin()
#             global listLevel
#             listLevel.append(1)
#             break

#         # подсчет сколько попыток понадобилось для прохождения
#         # выводить значение в главном меню -> пройденые уровни

#         else:
#             gameLose()


if __name__ == "__main__":
    render()
