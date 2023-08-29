from tkinter import * #our gui library
import sqlite3 #database library
from tkinter import messagebox #message library

# Create the main window
window = Tk()

window.title("Note Writing Page")#the title of page
window.geometry("500x450")#geometry settings

# Create a text box
note_entry = Text(window)
note_entry.pack()

# Create a save button and database connection
def save_note():
   note = note_entry.get("1.0", END)
   con = sqlite3.connect("notes.db")#connect to our database
   cursor = con.cursor()
   cursor.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT)")
   cursor.execute("INSERT INTO notes (content) VALUES (?)", (note,))
   con.commit()
   con.close()

#Create a delete func
def delete():
   note_entry.delete("1.0",END)

#Create a exit func
def exit():
   quest = messagebox.askquestion("Exit","Do you want to exit from program? ")
   if quest == "yes":
      window.destroy()
   else:
      pass

save_button = Button(window, text="Save Note", command=save_note,fg="green")#create a save button
save_button.pack()

delete_btn = Button(window, text="Delete",command=delete,foreground="blue")#create a delete button
delete_btn.pack()

exit_btn = Button(window,text="Exit",foreground="red",command=exit)#create a exit button
exit_btn.pack()

# Adding a button to view saved notes
def view_notes():
   conn = sqlite3.connect("notes.db")#connection to database
   cursor = conn.cursor()
   cursor.execute("SELECT * FROM notes")#this command selects notes from 'notes' table.
   notes = cursor.fetchall()#fetchall command is helps to take all of the notes.
   conn.close()
   
   view_window = Toplevel(window)#crate a second page for app
   view_window.title("View Notes")#the title of second page
   view_text = Text(view_window)
   for note in notes: 
       view_text.insert(END, note[1] + "\n")
   view_text.pack()

   #Create a second exit button for view notes page
   def exit2():
      quest = messagebox.askquestion("Exit","Do you want to exit from program? ")
      if quest == "yes":
         window.destroy()
      else:
         pass

   def go_back():#create a go-back func
      quest = messagebox.askquestion("Go Back","Do you want to go back to Writing Note Page? ")

      if quest =="yes":
         view_window.destroy()
      else:
         pass

   exit2_btn = Button(view_window, text="Exit",command=exit2,fg="red")#create a second exit button for second page.
   exit2_btn.pack()

   go_back_btn = Button(view_window,text="Go Back",command=go_back,foreground="blue")#create a go back button for second page to first page.
   go_back_btn.pack()
view_button = Button(window, text="View Notes", command=view_notes,foreground="purple")#create a view button
view_button.pack()

# Run the app
window.mainloop()