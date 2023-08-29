from tkinter import *
import requests#importing libraries
from tkinter import messagebox


url = 'http://api.openweathermap.org/data/2.5/weather'#the url of website that we use for data
api_key = '6c5eb51da0bf280cc725a25e6334d5f5'#api key


#Create our func for get weather.
def getWeather(city):
    params = {'q':city,'appid':api_key,'lang':"tr"}
    data = requests.get(url,params=params).json()
    if data:
        country = data['sys']['country']
        temp = int(data['main']['temp']-273.15)
        icon = data['weather'][0]['icon']
        condition = data['weather'][0]["description"]
        return (city,country,temp,icon,condition)
#Create our main func
def main():

    city = cityEntry.get()
    weather = getWeather(city)
    if weather:
        locationLabel['text'] = '{},{}'.format(weather[0],weather[1])
        tempLabel['text'] = '{} °C'.format(weather[2])
        conditionLabel['text'] = weather[4]

#Create exit func
def exit():
    app.quit()


app = Tk()#create main window
app.configure(bg="red")
app.geometry("300x450")#geometry of app
app.title("YC Weather App")#title of app
messagebox.showinfo("YC","Welcome to Weather App!")
cityEntry = Entry(app,justify="center")#create a entry for city
cityEntry.pack(fill=BOTH,ipady=10,padx=18,pady=5)
cityEntry.focus()

exit_btn = Button(app,text="Exit",fg="red",command=exit)#Create exit button

yclabel = Label(app,text="Yusuf Çeker",fg="Red",font=("Comic Sans MS",20,"bold"))

searhButton = Button(app,text="Arama",font=("Arial",15),command=main)
searhButton.pack(fill=BOTH,ipady=10,padx=20)

iconLabel = Label(app)
iconLabel.pack()

locationLabel = Label(app,font=("Arial",40))
locationLabel.pack()

tempLabel = Label(app,font=("Arial",50))
tempLabel.pack()

conditionLabel = Label(app,font=("Arial",20))
conditionLabel.pack()

yclabel.pack()
exit_btn.pack(side=BOTTOM)
app.mainloop()