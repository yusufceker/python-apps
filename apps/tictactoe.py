from tkinter import *
from tkinter import messagebox #importing the libraries
from pygame import mixer

#Create main window
window = Tk()

window.geometry('800x500')#set the geometry of window
window.title("Tic Tac Toe - Yusuf Çeker")#set title of the window

mixer.init()


messagebox.showinfo("Yusuf Çeker","Welcome to TicTacToe Game!")

Label(window, text="Yusuf Çeker ", font=('ariel', 45, ), fg='red').pack()
Label(window, text="Tic-Tac-Toe Game", font=('Ariel', 25)).pack()
status_label = Label(window, text="X's turn", font=('Ariel', 15), bg='blue', fg='snow')#create status label
status_label.pack(fill=X)#packing status label

#Create play again func
def playAgain():
    mixer.music.load("/Users/yusufceker/Desktop/sounds/click.wav")#playing click sound
    mixer.music.play()
    global currentChar
    currentChar = 'X'
    for point in xoPointCountr:
        point.button.configure(state=NORMAL)
        point.reset()
    status_label.configure(text="X's turn")
    playAgain.pack_forget()
playAgain = Button(window, text='Play again', font=('Ariel', 15), fg='red', command=playAgain)
def exit():
    #Create exit func
    window.quit()
currentChar = "X" #create current char variable

exit_btn = Button(window,text="Exit",fg="red",command=exit)

play_area = Frame(window, width=500, height=300, bg='white')#create area frame
xoPointCountr = []
xPointCountr = []
oPointCountr = []
#Create a XOPoint class
class XOPoint:
    #Create init func for XOPoint class
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = None
        self.button = Button(play_area, text="", width=10, height=5, command=self.set)
        self.button.grid(row=x, column=y)

    #Create set func
    def set(self):
        global currentChar
        if not self.value:
            self.button.configure(text=currentChar, bg='snow', fg='black')
            self.value = currentChar
            if currentChar == "X":
                xPointCountr.append(self)
                currentChar = "O"
                status_label.configure(text="O's turn",bg="green")
            elif currentChar == "O":
                oPointCountr.append(self)
                currentChar = "X"
                status_label.configure(text="X's turn",bg="blue")
        check_win()

    #Create reset func
    def reset(self):
        self.button.configure(text="", bg='lightgray')
        if self.value == "X":
            xPointCountr.remove(self)
        elif self.value == "O":
            oPointCountr.remove(self)
        self.value = None
for x in range(1, 4):
    for y in range(1, 4):
        xoPointCountr.append(XOPoint(x, y))
class WinningPossibility:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
    def check(self, for_chr):
        p1_satisfied = False
        p2_satisfied = False
        p3_satisfied = False
        if for_chr == 'X':
            for point in xPointCountr:
                if point.x == self.x1 and point.y == self.y1:
                    p1_satisfied = True
                elif point.x == self.x2 and point.y == self.y2:
                    p2_satisfied = True
                elif point.x == self.x3 and point.y == self.y3:
                    p3_satisfied = True
        elif for_chr == 'O':
            for point in oPointCountr:
                if point.x == self.x1 and point.y == self.y1:
                    p1_satisfied = True
                elif point.x == self.x2 and point.y == self.y2:
                    p2_satisfied = True
                elif point.x == self.x3 and point.y == self.y3:
                    p3_satisfied = True
        return all([p1_satisfied, p2_satisfied, p3_satisfied])
winning_possibilities = [
    WinningPossibility(1, 1, 1, 2, 1, 3),
    WinningPossibility(2, 1, 2, 2, 2, 3),
    WinningPossibility(3, 1, 3, 2, 3, 3),
    WinningPossibility(1, 1, 2, 1, 3, 1),
    WinningPossibility(1, 2, 2, 2, 3, 2),
    WinningPossibility(1, 3, 2, 3, 3, 3),
    WinningPossibility(1, 1, 2, 2, 3, 3),
    WinningPossibility(3, 1, 2, 2, 1, 3)
]
#Create a func to disable the game after result
def disable_game():
    for point in xoPointCountr:
        point.button.configure(state=DISABLED)
    playAgain.pack()
#Create check-win func
def check_win():
    for possibility in winning_possibilities:
        if possibility.check('X'):
            mixer.music.load("/Users/yusufceker/Desktop/sounds/winner.mp3")
            mixer.music.play()
            status_label.configure(text="Result: X won!",bg="blue")
            disable_game()
            return

        elif possibility.check('O'):
            mixer.music.load("/Users/yusufceker/Desktop/sounds/winner.mp3")
            mixer.music.play()
            status_label.configure(text="Result: O won!",bg="green")
            disable_game()
            return
        playAgain.pack()
    if len(xPointCountr) + len(oPointCountr) == 9:
        status_label.configure(text="Result: Draw!",bg="blue")
        disable_game()
    playAgain.pack()
play_area.pack(pady=10, padx=10)
exit_btn.pack(side=BOTTOM)
window.mainloop()