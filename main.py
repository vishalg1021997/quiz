import colorama
from colorama import Fore,Style
from os import system, name
from time import sleep
import eazyquestion as eq            #Importing Question Of Easy QUiz
import mediumquestion as mq          #Importing Question Of Medium QUiz
import hardquestion as hq            #Importing Question Of Hard QUiz
colorama.init(autoreset = True)
blue = Fore.BLUE+Style.BRIGHT
red = Fore.RED+Style.BRIGHT
green = Fore.GREEN+Style.BRIGHT
yellow = Fore.YELLOW+Style.BRIGHT
cyan = Fore.CYAN+Style.BRIGHT
lcyan = Fore.LIGHTCYAN_EX+Style.BRIGHT

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def menu():                          #Definng Menu Function To Display All The Operation Which Can Be Performed
    username = 'Vishal'              #And User and Passwor For Super_USer (ADMIN)
    password = 'Vishal@18'
    clear()
    print()
    print(Fore.MAGENTA + Style.BRIGHT + "====Welcome To Python Quiz====")
    print()
    print(blue +"1 Create Quiz")           #Operation 1
    print(blue + "2 Start Quiz")            #Operation 2
    print(blue + "3 Display All Score")     #Operation 3
    print(red + "0 To Exist")              #Operation 4
    a = int(input())
    clear()
    cont = 3
    if a == 1:
        while cont > 0:
            user = input("Enter Username:  ")
            pswd = input("Enter Password:  ")           #Operation 1 To Create Quiz
            if user == username and pswd == password:   #Validating Credential Incase Of Super_User
                print(green+"Login Sucessful")                #3 Chance To Login If Login Sucessful
                print()                                 #Create Quiz Function Is Called
                sleep(3)
                clear()
                createquiz()
                break
            else:
                cont -= 1
                print(red+"Username or Password Incorrect {} of 3 Try Remaining".format(cont))
                sleep(4)
                clear()
                print()
    elif a == 2:
        startquiz()                 #Operation 2 Start Quiz Function Is Called For User To Start/Give Quiz
    elif a == 3:
        all_score(std_score)        #Operation 3 All_Score Function Is Called Quiz TO display All Score And To Search Score For PArticular User
    elif a == 0:
        exit()                      #Operation 4 To Exit/Close The Program
    else:
        print(red + "Enter Valid Input")

def createquiz():            #Creating Quiz
    print(yellow+"Start Creating Quiz To Stop Press q:")
    while True:
        print(cyan+"Press 1 For Beginner Level")            #Super USer Can Create Quiz
        print(cyan+"Press 2 For Intermediate Level")        #Bassed On Diffrent Difficulty Level
        print(cyan+"Press 3 For Pro Level")
        diff = int(input())
        clear()
        while True:
            if diff == 1:                           #To Create Eazy Level Quiz (Biginner)
                print("Your Creating Quiz For Beginner Level")
                big.beginnerequiz()
            elif diff == 2:                         #To Create Medium Level Quiz (Intermediate)
                print("Your Creating Quiz For Intermediate Level")
                inter.intermediate_equiz()
            elif diff == 3:                         #To Create Hard Level Quiz (Pro)
                print("Your Creating Quiz For Pro Level")
                prof.pro_equiz()
            a = input(yellow+"Stop/Add More Question: ")     #If Super User Want to Stop Adding Question Press q
            if a == 'q':                            #Else Press Enter To Continue
                break
        a = input(yellow+"Do You Want to Add More Quiz Y/N: ")
        if a =='Y':                            #If Super User Want To Add QUiz Of Another Level Press Y
            clear()
            continue                           #Elese N To Stop
        else:
            clear()
            break

def startquiz():                             #Start Taking?Giving Quiz
    stdname = input("Enter Your Name: ")     #User Have to Enter Name So Score Can Be Store Uniquely For Each User
    std_score[stdname] = [0,0,0]             #Intially The Score For Student Will Be Zero
    while True:
        print()
        print(blue+"Press 1 For Beginner Level")          #User Can Take Quiz Bassed On Diffrent Level
        print(blue+"Press 2 For Intermediate Level")
        print(blue+"Press 3 For Pro Level")
        diff = int(input())
        print()
        while True:
            if diff == 1:
                clear()
                if big.Beginner_list == {}:                 #If No Question Is Added In Beginner Level Quiz
                    print(red+"Beginner Level Quiz Not Made Contact Your Administration")  #This Message Will Be Displayed
                    break
                else:
                    clear()
                    print(yellow+"You Chosse Beginner Level Quiz Topic is "+big.topic)
                    big.start_beginner()                 #Else The Beginner Quiz Will Start
                    for i in std_score.items():          #For Each Correct Answer The Score Will Be Counted
                        if i[0] == stdname:              #And It Will Get Stored
                            i[1][0]=big.count
            elif diff == 2:
                clear()
                if inter.Intermediate_list == {}:             #If No Question Is Added In Intermediate Level Quiz
                    print(red+"Intermediate Level Quiz Not Made Contact Your Administration")  #This Message Will Be Displayed
                    break
                else:
                    clear()
                    print(yellow + "You Chosse Intermediate Level Quiz Topic is "+ inter.topic)
                    inter.start_intermediate()           #Else The Intermediate Quiz Will Start
                    for i in std_score.items():          #For Each Correct Answer The Score Will Be Counted
                        if i[0] == stdname:              #And It Will Get Stored
                            i[1][1] = inter.count
            elif diff == 3:
                clear()
                if prof.Pro_list == {}:                     #If No Question Is Added In Pro Level Quiz
                    print(red+"Pro Quiz Not Made Contact Your Administration")  #This Message Will Be Displayed
                    break
                else:
                    clear()
                    print(yellow + "You Chosse Pro Level Quiz Topic is "+ prof.topic)
                    prof.start_pro()                     #Else The Pro Quiz Will Start
                    for i in std_score.items():          #For Each Correct Answer The Score Will Be Counted
                        if i[0] == stdname:              #And It Will Get Stored
                            i[1][1] = prof.count
            a = input(yellow+"Stop/Try Again: ")   #If The User Wants to Take Same Quiz Again Then Press Enter
            if a == 'q':                  #Else TO Stop The Quiz Pres Q
                break
        print()
        a = input(yellow+"Do You Want Take Another Round Off Quiz Y/N: ")
                                              #If User Wants To Take Another Level Of Quiz Press Y Else Press N
        if a =='Y':
            continue
        else:
            clear()
            a = std_score.get(stdname)    #The Score For Each Level Will Be Displayed After Completion OF Quiz
            print(cyan+stdname," Your Score For Beginner Level is: ",a[0])
            print(cyan+stdname, " Your Score For Intermediate Level is: ", a[1])
            print(cyan+stdname, " Your Score For Pro Level is: ", a[2])
            print()                       #The Correct Answer For Each Quiz And Each Question Will BE Displayed
            print(yellow+"Correct Answer Of Beginner Level Question")
            big.display_beginner()
            print(yellow+"Correct Answer Of Intermediate Level Question")
            inter.display_intermediate()
            print(yellow+"Correct Answer Of Pro Level Question")
            prof.display_pro()
            a = input()
            if a == range(ord('0'),ord('~')):
                pass
            break

def all_score(std_score):        #To See The Score Of All USer Who Have Given Quiz
    clear()
    if std_score == {}:           # IF No QUiz IS Conducted The Mesaage Will Be Displayed
        print(red+"No Quiz Conducted")
    else:
        d1 = {}
        for i in std_score.items():  #To Iterate In The User List And Get Score Of Each Student With Difficulty
            a = sum(i[1])            #Level And The Total
            d1[i[0]] = a
            print(cyan +i[0] + " Score : Beginner {} Intermeidate {} Pro {} Total {}".format(i[1][0], i[1][1], i[1][2],a))
            print()
        a = sorted(d1.items(), key=lambda x: x[1])   #TO Show The Topper OF The Quiz
        print(Fore.MAGENTA+Style.BRIGHT+"Topper is", a[-1][0], "Marks Score", a[-1][1])

        print(yellow+"To Search Your Score Enter Your Name or Press q To End")
        search = input()
        if search == 'q':
            menu()
        else:                      #To Search The Score Of Any Particular User
            for i in std_score.items():
                if i[0] == search:
                    print(cyan+i[0] + " Score : Beginner {} Intermeidate {} Pro {} Total {}".format(i[1][0], i[1][1], i[1][2],(i[1][0] + i[1][1] + i[1][2])))
            a = input()
            if a == range(ord('0'), ord('~')):
                pass

big = eq.eazyques()                  #Declaring Endividual Object For Each Quiz
inter = mq.mediumques()
prof = hq.hardyques()
std_score = {}
while True:
    print()
    menu()

