from random import randint as r
from time import sleep
from hardmode import bot

def win():
    print("Вы победили!")

def lose():
    print("Вы проиграли!")

def results(result):
    if result == False:
        lose()
    elif result == True:
        win()

def turn(sticks, max_take_sticks, difficulty):
    amount = sticks
    if amount <= 1:
        return amount, False

    print(f'Осталось {amount} спичек.')
    print("Сколько спичек ты хочешь взять?")
    choice = int(input("Я возьму: "))
    while not (choice > 0 and choice < max_take_sticks + 1):
        print("Столько спичек взять нельзя!")
        choice = int(input("Я возьму: "))
    amount -= choice

    if amount <= 1:
        return amount, True

    print("Компьютер думает...")
    sleep(r(1, 5))

    cchoice = bot(amount) if difficulty else r(1, max_take_sticks)
    amount -= cchoice
    print(f"Компьютер взял {cchoice}")

    return amount, False

def game(sticks, max_take_sticks, difficulty):
    result = False
    while sticks > 1:
        sticks, result = turn(sticks, max_take_sticks, difficulty)
    results(result)
