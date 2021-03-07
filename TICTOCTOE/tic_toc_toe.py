#TIC TOC TOE GAMES CODES WITH PYTHON
#===================================MODULES AND LIBRARY=========================================
import numpy as np
import sys
import time
#=================================== VARIABLES =================================================
TABLE = [" ", " ", " ", " ", " ", " ", " ", " ", " "] #ARRAY FOR TABLE
A = [" "," "," "," "," "," "," "," "," "]#ARRAY TO SHOW PLAYER SYMBOLS AND PLACES
EX= ["00","01","02","10","11","12","20","21","22"]#ARRAY TO EXPLAIN
TABLE_FULL = [" ", " ", " ", " ", " ", " ", " ", " ", " "]# ARRAY FOR SHOW WHERE PLAYED PLACES
TABLE_EMPTY = [] # ARRAY FOR SHOW EMPTY PLACES
PLAYER = ["",""] # ARRAY FOR PLAYER TURNS
NO_LINE = ""
NEW_LINE = "\n"
LINE = ""
U_LINE = "----"
N_LINE = ""
SYMBOL = ""
PLAYER1 = ""
PLAYER2 = ""
C_X = ""
C_O = ""
LOOP = "True"
CONTROL = ""
PLAYER1 = ""
PLAYER2 = ""
A=""
FULL=""
PURPLE="\033[95m"
GREEN="\033[92m"
NOCOLOR="\033[0m"
#===================================-FUNCTIONS-========================================
def HAFIF_BILGILER():
    print(PURPLE)
    print("""  ___  ___           ________""")
    print(""" |\  \/\  \         |\   __  \ """)
    print(""" \ \  \_\  \        \ \  \_\ /_""")
    print("""  \ \   __  \        \ \   __  \ """)
    print("""   \ \  \ \  \  ___   \ \  \_\  \  ___""")
    print("""    \ \__\ \__\|\__\   \ \_______\|\__\ """)
    print("""     \|__|\|__|\|__|    \|_______|\|__| """)
    print( "THIS SCRIPT CREATED BY HAFIFBILGILER ")
    print("________________________________v1.1 ")
    print(NOCOLOR)
    time.sleep(1)
    print(GREEN)
    print("WELCOME TIC TOC TOE GAME")
    time.sleep(1)
    print("T" ,"I","C")
    time.sleep(0.5)
    print("T" ,"O","C")
    time.sleep(0.5)
    print("T" ,"O","E")
    time.sleep(0.5)
    print(NOCOLOR)
#===================================-BOARD FUNCTIONS-==================================
def CREATE_BOARD(A):
    TABLE = A
    for i in range(0,9):
        if(i==2 or i==5 or i==8):
         LINE = NEW_LINE
        else:
         LINE = NO_LINE
        if(i==3 or i == 6):
         print(U_LINE*2)
        if(i==0 or i == 1 or i==3 or i==4 or i==6 or i==7):
         N_LINE = "|"
        else:
         N_LINE = ""
        print(TABLE[i],N_LINE, end=LINE )
#=====================================EXPLAIN OF THE BOARD-=========================
def CREATE_BOARD_EX():
    print("===========Explain Table==============")
    for i in range(0,9):
        if(i==2 or i==5 or i==8):
         LINE = NEW_LINE
        else:
         LINE = NO_LINE
        if(i==3 or i == 6):
         print(U_LINE*3)
        if(i==0 or i == 1 or i==3 or i==4 or i==6 or i==7):
         N_LINE = "|"
        else:
         N_LINE = ""
        print(EX[i],N_LINE, end=LINE )   
    print("======================================")
#================================FUNCTION OF TO CHOOSE SYMBOL FOR PLAYER=========
def CHOSE_SYMBOL():
    while True:
        SYMBOL = str(input("PLAYER1 COULD YOU PLEASE CHOOSE YOUR SYMBOL ( X or O )) :  "))
        if (SYMBOL == "X" or SYMBOL == "O"):
            PLAYER[0] = SYMBOL
            print("\033[92m","REGISTER PLAYER1 SYMBOL----> "+PLAYER[0]+"\033[0m")
            CONTROL = "TRUE"
        else:
            print("\033[31m","PLEASE ENTER JUST X OR O !!!","\033[0m")
            CONTROL = "FALSE"
        if (CONTROL == "TRUE"):
            if (SYMBOL == "X"):
                PLAYER[1] = "O"
                print("\033[92m","REGISTER PLAYER2 SYMBOL----> "+PLAYER[1]+"\033[0m")
            else:
                PLAYER[1] = "X"
                print("\033[92m","REGISTER PLAYER2 SYMBOL---->"+PLAYER[1]+"\033[0m")
            return PLAYER
            break
#====================================MAIN FUNCTION================================
def START_GAME():
    print("\033[92m","GAME IS STARTING....."+PLAYER2+"\033[0m")
    time.sleep(4)        
    print("\033[92m","BEFORE PLAYER1 MUST START TO GAME "+PLAYER2+"\033[0m")
    #CREATE_BOARD()
    TABLE = ["T","I","C","T","A","C","T","O","E"]
    CREATE_BOARD(TABLE)
    CHOSE_SYMBOL()
    COUNT=0
    TABLE = ["T","I","C","t","A","C","t","O","E"]
    TABLE1 = [" "," "," "," "," "," "," "," "," "]
    TABLE_FULL = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    while True: 
        print(PLAYER)
        if(COUNT == 0 or COUNT == 2 or COUNT == 4 or COUNT == 6 or COUNT == 8):
            SYMBOL_GAME = PLAYER[0]
            TURN = 1
        elif(COUNT == 1 or COUNT == 3 or COUNT == 5 or COUNT == 7 or COUNT == 8):
            SYMBOL_GAME = PLAYER[1]
            TURN = 2
        if(TURN == 1):
            TURN_PLYR = "PLAYER1"
        elif(TURN == 2):
            TURN_PLYR ="PLAYER2"
        print ("TURN OF IS----->",TURN_PLYR)
        PLACE_ROW = int(input("PLEASE CHOOSE YOUR ROW :  "))
        PLACE_COLOUMN = int(input("PLEASE CHOOSE YOUR COLOUMN :  "))
        if (PLACE_ROW > 3 or PLACE_ROW < 0  or PLACE_COLOUMN > 3 or PLACE_COLOUMN < 0) :
           print("\033[31m","PLEASE ENTER NUMBER BETWEEN 0 WITH 3","\033[0m") 
           NUMBER = False
        else:
           NUMBER = True
        if(NUMBER):
           if(PLACE_ROW == 0 and PLACE_COLOUMN==0 ):
               if(TABLE_FULL[0] != "T"):
                    TABLE[0] = SYMBOL_GAME
                    TABLE1[0] = SYMBOL_GAME
                    TABLE_FULL[0] = "T"
                    FULL= False
               else:
                    FULL= True  
           elif(PLACE_ROW == 0 and PLACE_COLOUMN == 1): 
               if(TABLE_FULL[1] != "T"):
                    TABLE[1] = SYMBOL_GAME
                    TABLE1[1] = SYMBOL_GAME
                    TABLE_FULL[1] = "T"
                    FULL= False
               else:
                    FULL= True
           elif(PLACE_ROW == 0 and PLACE_COLOUMN == 2): 
               if(TABLE_FULL[2] != "T"):
                    TABLE[2] = SYMBOL_GAME
                    TABLE1[2] = SYMBOL_GAME
                    TABLE_FULL[2] = "T"
                    FULL= False
               else:
                    FULL= True
           elif(PLACE_ROW == 1 and PLACE_COLOUMN == 0): 
               if(TABLE_FULL[3] != "T"):
                    TABLE[3] = SYMBOL_GAME
                    TABLE1[3] = SYMBOL_GAME
                    TABLE_FULL[3] = "T"
                    FULL= False
               else:
                    FULL= True
           elif(PLACE_ROW == 1 and PLACE_COLOUMN == 1): 
               if(TABLE_FULL[4] != "T"):
                    TABLE[4] = SYMBOL_GAME
                    TABLE1[4] = SYMBOL_GAME
                    TABLE_FULL[4] = "T"
                    FULL= False
               else:
                    FULL= True
           elif(PLACE_ROW == 1 and PLACE_COLOUMN == 2): 
               if(TABLE_FULL[5] != "T"):
                    TABLE[5] = SYMBOL_GAME
                    TABLE1[5] = SYMBOL_GAME
                    TABLE_FULL[5] = "T"
                    FULL= False
               else:
                    FULL=True
                    print("\033[31m","PLEASE CHOOSE OTHER PLACE, BECAUSE THIS SECTION IS FULL","\033[0m")
           elif(PLACE_ROW == 2 and PLACE_COLOUMN == 0): 
               if(TABLE_FULL[6] != "T"):
                    TABLE[6] = SYMBOL_GAME
                    TABLE1[6] = SYMBOL_GAME
                    TABLE_FULL[6] = "T"
                    FULL= False
               else:
                    FULL=True
           elif(PLACE_ROW == 2 and PLACE_COLOUMN == 1): 
               if(TABLE_FULL[7] != "T"):
                    TABLE[7] = SYMBOL_GAME
                    TABLE1[7] = SYMBOL_GAME
                    TABLE_FULL[7] = "T"
                    FULL= False
               else:
                    FULL=True
           elif(PLACE_ROW == 2 and PLACE_COLOUMN == 2): 
               if(TABLE_FULL[8] != "T"):
                    TABLE[8] = SYMBOL_GAME
                    TABLE1[8] = SYMBOL_GAME
                    TABLE_FULL[8] = "T"
                    FULL= False
               else:
                    FULL=True
        A = TABLE1
        for i in range(0,9):
          if(TABLE_FULL[i] != 'T'):
            TABLE_EMPTY.append(i)       
        if(TABLE[0]==TABLE[1] and TABLE[1]==TABLE[2]):
           print("\033[92m","GAME IS ENDED----> ""\033[0m")
           if(TABLE[0] == PLAYER[0] ):
             print("\033[92m","PLAYER1 IS WON----> "+PLAYER[0]+"\033[0m")    
           else:
             print("\033[92m","PLAYER2 IS WON----> "+PLAYER[1]+"\033[0m")
           CREATE_BOARD(A)
           break
        elif(TABLE[3]==TABLE[4] and TABLE[4]==TABLE[5]):
           print("\033[92m","GAME IS ENDED----> ""\033[0m")
           if(TABLE[3] == PLAYER[0] ):
             print("\033[92m","PLAYER1 IS WON----> "+PLAYER[0]+"\033[0m")    
           else:
             print("\033[92m","PLAYER2 IS WON----> "+PLAYER[1]+"\033[0m")
           CREATE_BOARD(A)
           break
        elif(TABLE[6]==TABLE[7] and TABLE[7]==TABLE[8]):
           print("\033[92m","GAME IS ENDED----> ","\033[0m")
           if(TABLE[6] == PLAYER[0] ):
             print("\033[92m","PLAYER1 IS WON----> "+PLAYER[0]+"\033[0m")    
           else:
             print("\033[92m","PLAYER2 IS WON----> "+PLAYER[1]+"\033[0m")
           CREATE_BOARD(A)
           break
        elif(TABLE[0]==TABLE[4] and TABLE[4]==TABLE[8]):
           print("\033[92m","GAME IS ENDED----> ","\033[0m")
           if(TABLE[0] == PLAYER[0] ):
             print("\033[92m","PLAYER1 IS WON----> "+PLAYER[0]+"\033[0m")    
           else:
             print("\033[92m","PLAYER2 IS WON----> "+PLAYER[1]+"\033[0m")
           CREATE_BOARD(A)
           break
        elif(TABLE[0]==TABLE[3] and TABLE[3]==TABLE[6]):
           print("\033[92m","GAME IS ENDED----> ","\033[0m")
           if(TABLE[0] == PLAYER[0] ):
             print("\033[92m","PLAYER1 IS WON----> "+PLAYER[0]+"\033[0m")    
           else:
             print("\033[92m","PLAYER2 IS WON----> "+PLAYER[1]+"\033[0m")
           CREATE_BOARD(A)
           break
        elif(TABLE[2]==TABLE[4] and TABLE[4]==TABLE[6]):
           print("\033[92m","GAME IS ENDED----> ","\033[0m")
           if(TABLE[2] == PLAYER[0] ):
             print("\033[92m","PLAYER1 IS WON----> "+PLAYER[0]+"\033[0m")    
           else:
             print("\033[92m","PLAYER2 IS WON----> "+PLAYER[1]+"\033[0m")
           CREATE_BOARD(A)
           break
        elif(TABLE[2]==TABLE[5] and TABLE[5]==TABLE[8]):
           print("\033[92m","GAME IS ENDED----> ","\033[0m")
           if(TABLE[2] == PLAYER[0] ):
             print("\033[92m","PLAYER1 IS WON----> "+PLAYER[0]+"\033[0m")    
           else:
             print("\033[92m","PLAYER2 IS WON----> "+PLAYER[1]+"\033[0m")
           CREATE_BOARD(A)
           break
        #print(A)
        CREATE_BOARD_EX()
        CREATE_BOARD(A)
        print(TABLE_FULL)
        print(TABLE_EMPTY)
        TABLE_EMPTY.clear()
        if(FULL == True):
            print("\033[31m","PLEASE CHOOSE OTHER PLACE, BECAUSE THIS SECTION IS FULL AND USING","\033[0m")
        else:
            COUNT += 1
HAFIF_BILGILER()
START_GAME()

