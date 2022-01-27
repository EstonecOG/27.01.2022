from keyboard import *
from random import *
from data import data_game
from time import sleep

def botvsbot(v1:list,v2:list, access):
    """Robootite mäng
    Näitame ekraanile võitja nime
    Tagastame m muutuja int formaadis
    :param list v1: järjend esimese roboti jaoks
    :param list v2: järjend teise roboti jaoks
    """
    access.insert(0, "Kas mängime? ESC + Välja, Enter - mängime")
    while True:
        if read_key()=="esc":
            break
        elif read_key()=="enter":
            p1= choice(v1)
            access.insert(0, "Esimene bot:",p1)
            p2= choice(v2)
            access.insert(0, "Teine bot:",p2)
            if p1==p2:
                access.insert(0, "Viik")
            elif p1==v1[0] and p2==v2[1] or p1==v1[2] and p2==v2[0] or p1==v1[1] and p2==v2[2]:
                access.insert(0, "Võitis 1")
            else:
                access.insert(0, "Võitis 2")




def robotvs(access):
    print('все гуд')
    a=0
    while a!="x" not in [1,2,3]:
            try:
                h = data_game['kas']['user']
                sleep(.5)
                if h:
                    print('3', h)
                    access.insert(0, "1 - Камень, 2 - Ножницы, 3 - Бумага")
                    select = h.pop()
                    player = select
                    print('4', h)
                    if (player==1 or player==2 or player==3):
                        a=1
                    if player==1:
                        access.insert(0, "Вы выбрали камень.")
                    elif player==2:
                        access.insert(0, "Вы выбрали ножницы.")
                    elif player==3:
                        access.insert(0, "Вы выбрали бумагу.")
                    bot=randint(1,3)
                    if bot==1:
                        access.insert(0, "Компьютер выбрали камень.")
                    elif bot==2:
                        access.insert(0, "Компьютер ножницы.")
                    elif bot==3:
                        access.insert(0, "Компьютер бумагу.")
                    if player==1 and bot==2 or player==2 and bot==3 or player==3 and bot==1:
                        win=1
                    if player==1 and bot==3 or player==2 and bot==1 or player==3 and bot==2:
                        win=2
                    if player==3 and bot==3 or player==2 and bot==2 or player==1 and bot==1:
                        win=0
                    if win==0:
                        access.insert(0, "Ничья.")
                    elif win==1:
                        access.insert(0, "Вы победили!")
                    elif win==2:
                        access.insert(0, "Победил компьютер.")
            except:
                ValueError