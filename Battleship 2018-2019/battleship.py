# gameMode = int(input("If you want to play alone type 1, otherwise type 2: "))
# while gameMode != 1 and gameMode != s2:
#     gameMode = int(input("Please enter 1 for A.I game or 2 for versus game: "))
# else:
#     print (gameMode)

points = {'P1':0 , 'P2': 0}
arena = []
for i in range(5):
    arena.append(["0"] * 5)

def print_arena(a):
    for i in arena:
        print (" ".join(i))

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

def place_airships():
    p = []
    n = 0
    while n < 5:
        n = n + 1
        temp = str(input("Please give me coordinates for your ship position: "))
        if (temp[0] == 'a' or temp[0] == 'b' or temp[0] == 'c' or temp[0] == 'd' or temp[0] == 'e') and (temp[1] == '1' or temp[1] == '2' or temp[1] == '3' or temp[1] == '4' or temp[1] == '5'):
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

def missile_launchingp1():
    n = 0
    while (points['P1'] < 5 or points['P2']) < 5 and n < 1:
        n = n + 1
        a = str(input("Player 1 please enter the position you want to attack: "))
        if (a[0] == 'a' or a[0] == 'b' or a[0] == 'c' or a[0] == 'd' or a[0] == 'e') and (a[1] == '1' or a[1] == '2'or a[1] == '3' or a[1] == '4' or a[1] == '5'):
            temp = list(a)
            temp[0] = translate(a[0])
            temp[1] = translate(temp[1])
            if temp in p2ships:
                print("Missile launched at {}".format(a))
                print("Gratz! Your missile hit an enemy ship. You are one step closer to the victory.")
                arena[temp[0]][temp[1]] = 'X'
                print_arena(arena)
                points['P1'] = points['P1'] + 1
            else:
                print("Missile launched at {}" .format(a))
                print("No ships here try again some other time")
                arena[temp[0]][temp[1]] = 'G'
                print_arena(arena)

        else:
            print("\n*WARNING*\nThe position you gave me is out of range!")
            n = n -1


p1ships = ['a1','a2','a3','a4','a5']
p2ships = place_airships()
print("This is here")
print(p2ships)
print_arena(arena)
print('---')
print_arena(arena)
missile_launchingp1()




