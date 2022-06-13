from random import randint as r
from game import game 
from configparser import RawConfigParser

# Game settings constants

config = RawConfigParser()
config.read('game.ini')
max_sticks = int(config.get('settings', 'matches.amount'))
max_take_sticks = 2

greetings = '''
|Приветствую тебя в игре "Спички"                        |
|Напиши "play" (p) - чтобы начать игру                   |
|Напиши "playh" (ph) - чтобы начать игру в сложном режиме|
|Напиши "quit" (q) - чтобы выйти из игры                 |
|Напиши "info" (i) - чтобы узнать правила                |'''

def info():
    print("""
    Код написал - Danek_Gaffet
    Твоя задача - оставить противнику 1 и меньше спичек
    """)

def menu(max_sticks, max_take_sticks):
    command = ""
    while not (command == "q" or command == "quit"):
        print(greetings)
        command = input()
        if command == "p" or command == "play":
            game(max_sticks, max_take_sticks, False)
        elif command == "ph" or command == "playh":
            game(max_sticks, max_take_sticks, True)
        elif command == "i" or command == "info":
            info()
        else:
            print("Неизвестная команда")

if __name__ == '__main__':
    menu(max_sticks, max_take_sticks)