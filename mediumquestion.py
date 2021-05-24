import colorama
from colorama import Fore,Style
colorama.init(autoreset = True)
blue = Fore.BLUE+Style.BRIGHT
red = Fore.RED+Style.BRIGHT
green = Fore.GREEN+Style.BRIGHT
yellow = Fore.YELLOW+Style.BRIGHT
cyan = Fore.CYAN+Style.BRIGHT
lcyan = Fore.LIGHTCYAN_EX+Style.BRIGHT
class mediumques:
    def __init__(self):
        self.Intermediate_list = {}            #To Store Quiz Details
        self.topic = ""
    def intermediate_equiz(self):               #To Start Creating Quiz
        if self.topic == "":
            print("Enter The Topic Name")
            a = input()
            self.topic = a
        que = input("Enter The Question \n")
        self.Intermediate_list[que] = []        #Making Question As Key So Each Question Will Be Diffrent
        print(yellow+"Enter Four Option")
        for i in range(4):
            option = input()
            self.Intermediate_list[que].append(option)   #Appending The Four Option For The Question
        print(yellow+"Enter the Correct Answer --> A/B/C/D")
        corans = input()
        self.Intermediate_list[que].append(corans)       #Taking And Storing The Correct Quiz
        print()


    def start_intermediate(self):                   #To Start The Quiz
        self.count = 0                              #To Count The Score
        answers = []                                #To Store The Answer Given BY USer
        for i in self.Intermediate_list.items():    #Iterating Through The Set Of question And displaying Only 1
            print("Question: ",i[0])                #Question And its Option At a Time And Accepting The
            print("A ",i[1][0])                     #Answer From The User And Counting The Score If The Answer Is
            print("B ",i[1][1])                     #Correct And Then Displaying The NExt Question After Completion
            print("C ",i[1][2])                     #Of Each Loop
            print("D ",i[1][3])
            ans = input(yellow+"Enter Your Answer A/B/C/D: ")
            answers.append(ans)
            if ans == i[1][4]:
                self.count += 10
                print()

    def display_intermediate(self):                 #To Display The Correct Answer
        for i in self.Intermediate_list.items():    #Iterating Through The Set Of question And displaying Only 1
            print("Question: ", i[0])               #Question And its Option At a Time And Also Displaying The Correct
            print("A ", i[1][0])                    #Answer After Completion Of Each Loop Next Question is Displayed
            print("B ", i[1][1])
            print("C ", i[1][2])
            print("D ", i[1][3])
            if i[1][4] == 'A':
                print(green+"Correct Answer A: ",i[1][0])
            elif i[1][4] == 'B':
                print(green+"Correct Answer B: ",i[1][1])
            elif i[1][4] == 'C':
                print(green+"Correct Answer C: ",i[1][2])
            elif i[1][4] == 'D':
                print(green+"Correct Answer D: ",i[1][3])
