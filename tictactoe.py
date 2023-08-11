from pyfiglet import Figlet
def show():
    for satr in game_board :
        for sotoon in satr :
            print(sotoon,end=" ")
        print()


def chek_play_1():
    if game_board[0][0]=="x"and game_board[0][1]=="x"and game_board[0][2]=="x":
        print("won1")
    elif game_board[1][0]=="x"and game_board[1][1]=="x"and game_board[1][2]=="x":
        print("won1")
    elif game_board[2][0]=="x"and game_board[2][1]=="x"and game_board[2][2]=="x":
        print("won1")
    elif game_board[0][0]=="x"and game_board[1][0]=="x" and game_board[2][0]=="x":
        print("won1")
    elif game_board[0][1]=="x"and game_board[1][1]=="x"and game_board[2][1]=="x":
        print("won1")
    elif game_board[0][2]=="x"and game_board[1][2]=="x"and game_board[2][2]=="x":
        print("won1")
    elif game_board[0][0]=="x"and game_board[1][1]=="x"and game_board[2][2]=="x":
        print("won1")
    elif game_board[0][2]=="x"and game_board[1][1]=="x"and game_board[2][0]=="x":
        print("won1")
def chek_play_2():
    if game_board[0][0]=="o"and game_board[0][1]=="o" and game_board[0][2]=="o":
        print("won2")
    elif game_board[1][0]=="o"and game_board[1][1]=="o"and game_board[1][2]=="o":
        print("won2")
    elif game_board[2][0]=="o"and game_board[2][1]=="o"and game_board[2][2]=="o":
        print("won2")
    elif game_board[0][0]=="o"and game_board[1][0]=="o" and game_board[2][0]=="o":
        print("won2")
    elif game_board[0][1]=="o"and game_board[1][1]=="o"and game_board[2][1]=="o":
        print("won2")
    elif game_board[0][2]=="o"and game_board[1][2]=="o"and game_board[2][2]=="o":
        print("won2")
    elif game_board[0][0]=="o"and game_board[1][1]=="o"and game_board[2][2]=="o":
        print("won2")
    elif game_board[0][2]=="o"and game_board[1][1]=="o"and game_board[2][0]=="o":
        print("won2")
n = Figlet(font='slant')
print(n.renderText("tic tac toe"))
game_board = [["-","-","-"],
              ["-","-","-"],
              ["-","-","-"]]
show()
while True:
    print("play1")
    while True:
        row=int(input("Enter a number :"))
        col=int(input("Enter a number :"))
        if 0 <= row <3 and 0 <= col< 3 : 
            if game_board[row][col] == "-" :
                game_board[row][col] = "x"
                show()
                chek_play_1()
                break
            elif "-" not in game_board[0]and"-" not in  game_board[1] and "-" not in game_board[2]:
                print("tamam hame khone ha pore")
                break
            else:
                print("baiad ie khone dige antekhab koni in khone pore")
                row=int(input("Enter a number:"))
                col=int(input("Enter a number :"))
                if 0 <= row <3 and 0 <= col < 3 : 
                    if game_board[row][col] == "-" :
                        game_board[row][col] = "x"
                        show()
                        chek_play_1()
                        break
                    elif "-" not in game_board[0]and "-" not in game_board[1] and "-" not in game_board[2]:
                        print("tamam hame khone ha pore")
                        break
                    
        else:
            print("Enter a number bein 0 ta 2!")
            row=int(input("Enter a number :"))
            col=int(input("Enter a number :"))
            if 0 <= row <3 and 0 <= col < 3 : 
                if game_board[row][col] == "-" :
                    game_board[row][col] = "x"
                    show()
                    chek_play_1()
                    break
                elif "-" not in game_board[0]and "-" not in game_board[1]and "-" not in game_board[2]:
                    print("tamam hame khone ha pore")
                    break
            else:
                print(" dighe nemitoni entekhab koni")
                break



#plyer2
    print("plyer2")
    while True:
        row=int(input("Enter a number :"))
        col=int(input("Enter a number :"))
        if 0 <= row <3 and 0 <= col < 3 : 
            if game_board[row][col] == "-" :
                game_board[row][col] = "o"
                show()
                chek_play_2()
                break
            elif "-" not in game_board[0]and "-" not in game_board[1]and "-" not in game_board[2]:
                print("tamam hame khone ha pore")
                break
            else:
                print("baiad ie khone dige antekhab koni in khone pore")
                row=int(input("Enter a number :"))
                col=int(input("Enter a number :"))
                if 0 <= row <3 and 0 <= col< 3 : 
                    if game_board[row][col] == "-" :
                        game_board[row][col] = "o"
                        show()
                        chek_play_2()
                        break
                    elif "-" not in game_board[0]and "-" not in game_board[1]and "-" not in game_board[2]:
                        print("tamam hame khone ha pore")
                        break
                else:
                    print("Enter a number bein 0 ta 2")
                    row=int(input("Enter a number :"))
                    col =int(input("Enter a number :"))
                    if 0 <= row <3 and 0 <= col< 3 : 
                        if game_board[row][col ] == "-" :
                            game_board[row][col ] = "o"
                            show()
                            chek_play_2()
                            break
                        elif "-" not in game_board[0]and "-" not in game_board[1]and "-" not in game_board[2]:
                            print("tamam hame khone ha pore")
                            break
        else:
            print("Enter a number bein 0 ta 2!")
            row=int(input("Enter a number :"))
            col=int(input("Enter a number :"))
            if 0 <= row <3 and 0 <= col < 3 : 
                if game_board[row][col ] == "-" :
                    game_board[row][col ] = "o"
                    show()
                    chek_play_2()
                    break
                elif "-" not in game_board[0]and "-" not in game_board[1]and "-" not in game_board[2]:
                    print("tamam hame khone ha pore")
                    break
            else:
                print(" dighe nemitoni entekhab koni")
                break