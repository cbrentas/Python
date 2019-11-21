#Christos Brentas, A.M: 4442

import random
print('Welcome to my Battleship game. Created by Christos Brentas.')
gameMode = int(input("If you want to play alone type 1, otherwise type 2 to play with 2 players: "))

points = {'P1':0 , 'P2': 0}
coords = ['a','b','c','d','e']
p1ships=[]
p2ships=[]
anagnwst = 0
odhgoscoords = ['a','b','c','d','e']

#Creating the boards using 2D lists.
arena1 = []
for i in range(5):
    arena1.append([" "] * 5)

arena2 = []
for y in range(5):
    arena2.append([" "] * 5)

def print_arena(arena1,arena2):
    hello = 0
    print('      P1            P2')
    print('  1 2 3 4 5     1 2 3 4 5')
    for i, z in zip(arena1, arena2):
        print(odhgoscoords[hello], " ".join(i), end='')
        print(' ', odhgoscoords[hello], " ".join(z))
        hello = hello + 1
    return

#A function created to translate the coordinates given by the client to board coordinates(e.g a1 --> 00).
def translate(el):
    if el == 'a' or el == '1':
        el = 0
    elif el == 'b' or el == '2':
        el = 1
    elif el == 'c' or el == '3':
        el = 2
    elif el == 'd' or el == '4':
        el = 3
    elif el == 'e' or el == '5':
        el = 4
    return el

def bot_translate(el):
    if el[0] == 0:
        el[0] = 'a'
    elif el[0] == 1:
        el[0] = 'b'
    elif el[0] == 2:
        el[0] = 'c'
    elif el[0] == 3:
        el[0] = 'd'
    elif el[0] == 4:
        el[0] = 'e'
    if el[1] == 0:
        el[1] = '1'
    elif el[1] == 1:
        el[1] = '2'
    elif el[1] == 2:
        el[1] = '3'
    elif el[1] == 3:
        el[1] = '4'
    elif el[1] == 4:
        el[1] = '5'
    return el

#This is the function for placing the ships taking into consideration all the possible invalid entries.
def place_airships(p):
    p = []
    n = 0
    while n < 5:
        n = n + 1
        temp = str(input("Please give me coordinates for your ship position: "))
        if len(temp) != 2:
            print("\n*WARNING*\nThe position you gave me is not valid!")
            n = n - 1
        elif (temp[0] == 'a' or temp[0] == 'b' or temp[0] == 'c' or temp[0] == 'd' or temp[0] == 'e') and (temp[1] == '1' or temp[1] == '2' or temp[1] == '3' or temp[1] == '4' or temp[1] == '5'):
            a = list(temp)
            a[0] = translate(a[0])
            a[1] = translate(a[1])
            if a in p:
                print("\n*WARNING*\nPosition already occupied please enter another position:")
                n = n - 1
            else:
                p.append(a)
                print("Ship successfully placed!")
        else:
                print("\n*WARNING*\nThe position you gave me is out of range!")
                n = n - 1
    return p

#The following function is used for 'throwing missiles' and marking the map with an 'O' if an enemy ship was hit and an 'X' if not, taking into consideration all invalid entries.
#Variable 'field' stands for the targeted board and 'shiplist' for the ship contained in the targeted board
def missile_launching(field, shiplist):
    n = 0
    while n < 1:
        global anagnwst
        anagnwst = 0
        n = n + 1
        a = str(input("Please enter the position you want to attack: "))
        if len(a) != 2:
            print("\n*WARNING*\nThe position you gave me is not valid!")
            n = n - 1
        elif (a[0] == 'a' or a[0] == 'b' or a[0] == 'c' or a[0] == 'd' or a[0] == 'e') and (a[1] == '1' or a[1] == '2'or a[1] == '3' or a[1] == '4' or a[1] == '5'):
            temp = list(a)
            temp[0] = translate(a[0])
            temp[1] = translate(temp[1])
            if field[temp[0]][temp[1]] == 'X' or field[temp[0]][temp[1]] == 'O':
                print('You already gave this position before, please select another one.')
                n = n - 1
            elif temp in shiplist:
                print("Missile launched at {}".format(a))
                print("Gratz! Your missile hit an enemy ship. You are one step closer to the victory.")
                field[temp[0]][temp[1]] = 'O'
                print_arena(arena1,arena2)
                anagnwst = 1
            else:
                print("Missile launched at {}" .format(a))
                print("No ships here try again some other time..")
                field[temp[0]][temp[1]] = 'X'
                print_arena(arena1,arena2)
        else:
            print("\n*WARNING*\nThe position you gave me is out of range!")
            n = n -1

#This function is made exclusively for the 'missile throwing' part when the bot 'attacks' taking again all invalid entries into consideration.
def bot_missile(field, shiplist):
    n = 0
    while n < 1:
        n = n + 1
        global anagnwst
        anagnwst = 0
        thesi11 = random.randint(0, 4)
        thesi22 = random.randint(0, 4)
        lista = []
        lista.append(thesi11)
        lista.append(thesi22)
        if field[lista[0]][lista[1]] == 'O' or field[lista[0]][lista[1]] == 'X':
            n = n - 1
#The reason behind using the 'bot_translate' function here is to change indexes into characters in order to use it on print.
        elif lista in shiplist:
            metafrlista1 = ''.join(bot_translate(lista))
            print("The bot launched a missile at {}".format(metafrlista1))
#And the reverse here(characters to indexes)
            lista[0] = translate(lista[0])
            lista[1] = translate(lista[1])
            field[lista[0]][lista[1]] = 'O'
            print("The bot is doing better than you, it just hit one of your ship!")
            print_arena(arena1,arena2)
            n = n + 1
            anagnwst = 1
        else:
            metafrlista1 = ''.join(bot_translate(lista))
            print("The bot launched a missile at {}".format(metafrlista1))
            lista[0] = translate(lista[0])
            lista[1] = translate(lista[1])
            field[lista[0]][lista[1]] = 'X'
            print('Apparently python -random- library is not so efficient. Target missed!')
            print_arena(arena1,arena2)
            n = n + 1

#This is the 'main'
if gameMode == 2:
    print('----------Player 1 it is your turn to place the ship!----------')
    p1ships = place_airships(p1ships)
    print('\n\n')
    print('----------Player 2 it is your turn to place the ship!----------')
    p2ships = place_airships(p2ships)

    seira = random.randint(1,2)
#I used a 'for' inside another 'for' to change turns between players.
    for temp in range(25):
        if seira == 1:
#Before every loop I check my dictionary to see if someone has scored 5 points(If someone has sunk 5 enemy ship)
            if points['P1'] == 5 or points['P2'] == 5:
                break
            print('Player 1 it is your turn to attack.')
            missile_launching(arena2, p2ships)
#The 'anagnwst' variable becomes '1' if the hit was successful and it adds one to the score, otherwise it is '0' and it continues the loop.
            if anagnwst ==  1:
                points['P1'] = points['P1'] + 1
        for z in range(25):
            if points['P1'] == 5 or points['P2'] == 5:
                break
            print('Player 2 it is your turn to attack.')
            missile_launching(arena1, p1ships)
            if anagnwst == 1:
                points['P2'] = points['P2'] + 1
            break
        else:
            if points['P1'] == 5 or points['P2'] == 5:
                break
            print('Player 2 it is your turn to attack.')
            missile_launching(arena1, p1ships)
            if anagnwst == 1:
                points['P2'] = points['P2'] + 1
        for l in range(25):
            if points['P1'] == 5 or points['P2'] == 5:
                break
            print('Player 1 it is your turn to attack.')
            missile_launching(arena2, p2ships)
            if anagnwst == 1:
                points['P1'] = points['P1'] + 1
            break
    if points['P1'] == 5:
        print('|||||||||||||||||||||||||||||| \nCongratulations player 1 you have won the game\n|||||||||||||||||||||||||||||||||||||')
    elif points['P2'] == 5:
        print('|||||||||||||||||||||||||||||| \nCongratulations player 2 you have won the game\n|||||||||||||||||||||||||||||||||||||')
else:
    print('----------Player 1 it is your turn!----------')
    p1ships = place_airships(p1ships)
    for i in range(5):
        temporary = 0
        while temporary < 1:
            temporary = temporary + 1
            thesi1 = random.randint(0,4)
            thesi2 = random.randint(0,4)
            lista = []
            lista.append(thesi1)
            lista.append(thesi2)
            if lista in p2ships:
                temporary = temporary - 1
            else:
                p2ships.append(lista)
                temporary = temporary + 1
    seira = random.randint(1, 2)
    for temp in range(25):
        if seira == 1:
            if points['P1'] == 5 or points['P2'] == 5:
                break
            print('Player 1 it is your turn to attack.')
            missile_launching(arena2, p2ships)
            if anagnwst ==  1:
                points['P1'] = points['P1'] + 1
        for z in range(25):
            if points['P1'] == 5 or points['P2'] == 5:
                break
            print('The bot is about to attack')
            bot_missile(arena1, p1ships)
            if anagnwst == 1:
                points['P2'] = points['P2'] + 1
            break
        else:
            if points['P1'] == 5 or points['P2'] == 5:
                break
            print('The bot is about to attack')
            bot_missile(arena1, p1ships)
            if anagnwst == 1:
                points['P2'] = points['P2'] + 1
        for l in range(25):
            if points['P1'] == 5 or points['P2'] == 5:
                break
            print('Player 1 it is your turn to attack.')
            missile_launching(arena2, p2ships)
            if anagnwst == 1:
                points['P1'] = points['P1'] + 1
            break
    if points['P1'] == 5:
        print('|||||||||||||||||||||||||||||| \nCongratulations player 1 you have won the game\n|||||||||||||||||||||||||||||||||||||')
    elif points['P2'] == 5:
        print('|||||||||||||||||||||||||||||| \nSuch a pity. The bot has won the game!\n|||||||||||||||||||||||||||||||||||||')
