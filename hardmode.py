from random import randint as r
def bot(sticks):
    take = sticks%3
    if take == 2:
        return 1
    elif take == 1:
        return r(1, 2)
    elif take == 0:
        return 2
