from tkinter import * #we have imported Python Tkinter Module.

pencere=Tk()
pencere.title("Calculate-It")#title of app
pencere.configure(background = "black")
#root.geometry("340x555")
pencere.minsize(340, 555)  #***
pencere.maxsize(340, 555)


def click(event): #burada ana fonksiyonu tanımladık
    global emptyString
    text = event.widget.cget("text")
    if text == "=":
        if emptyString.get().isdigit():
            value = int(emptyString.get())
        else:
            value = eval(screen.get())
        emptyString.set(value)
        screen.update()

    elif text == "Clear": #burada clear func'ını tanımladık ve command'ını yazdık
        emptyString.set("") #emptystring variablesi'ni boş bir stringe eşitliyoruz
        screen.update()

    else:
        emptyString.set(emptyString.get() + text)
        screen.update() #burada ekranı refreshledik
def exit():
    #Create exit func
    pencere.quit()
emptyString = StringVar() #boş bir string tanımladık
emptyString.set("")

screen = Entry(pencere,textvar = emptyString, font = "lucida 30 bold")
screen.pack(fill = X, pady = 10, padx = 10)

yclabel = Label(pencere,text="Yusuf Çeker",fg="Red",font=("Comic Sans MS",20,"bold"))

exit_btn = Button(pencere,text="Exit",command=exit,fg="red")

f = Frame(pencere, bg = "black")

b = Button(f, text = "Clear", bg="silver", padx = 10, pady = 10, font = "lucida 25 bold", width=10)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "%", bg="cyan", padx = 10, pady = 10, font = "lucida 25 bold", width=2)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

f.pack()



f = Frame(pencere, bg = "black")

b = Button(f, text = "9", bg="orange", padx = 10, pady = 10, font = "lucida 25 bold", width=2)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "8", bg="orange", padx = 10, pady = 10, font = "lucida 25 bold", width=2)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "7", bg="orange", padx = 10, pady = 10, font = "lucida 25 bold", width=2)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "/", bg="cyan", padx = 10, pady = 10, font = "lucida 25 bold", width=2)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

f.pack()



f = Frame(pencere, bg = "black")

b = Button(f, text = "6", bg="orange", padx = 10, pady = 10, font = "lucida 25 bold", width=2)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "5", bg="orange", padx = 10, pady = 10, font = "lucida 25 bold", width=2)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "4", bg="orange", padx = 10, pady = 10, font = "lucida 25 bold", width=2)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "*", bg="cyan", padx = 10, pady = 10, font = "lucida 25 bold", width=2)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

f.pack()



f = Frame(pencere, bg = "black")

b = Button(f, text = "3", bg="orange", padx = 10, pady = 10, font = "lucida 25 bold", width=2)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "2", bg="orange", padx = 10, pady = 10, font = "lucida 25 bold", width=2)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "1", bg="orange", padx = 10, pady = 10, font = "lucida 25 bold", width=2)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "+", bg="cyan", padx = 10, pady = 10, font = "lucida 25 bold", width=2)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

f.pack()



f = Frame(pencere, bg = "black")

b = Button(f, text = ".", bg="purple", padx = 10, pady = 10, font = "lucida 25 bold", width=2)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "0", bg="orange", padx = 10, pady = 10, font = "lucida 25 bold", width=2)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "=", bg="green", padx = 10, pady = 10, font = "lucida 25 bold", width=2)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f, text = "-", bg="cyan", padx = 10, pady = 10, font = "lucida 25 bold", width=2)
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)

f.pack()
exit_btn.pack(side=BOTTOM)
yclabel.pack()
pencere.mainloop() 