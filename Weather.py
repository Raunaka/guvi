from tkinter import*
import requests

HIGHT=500
WIDTH=600
#7bcefd862cdda4c19f29bd05d563df95
#api.openweathermap.org/data/2.5/forecast?q={city name},{country code}

def test_fun(entry):
    print('this is the entry',entry)

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        
        final_str = 'City: %s \nConditions: %s \nTemperature (°F):' % (name, desc, temp)
        
    except:
        final_str = 'There was a problem retrieving that information'

    return final_str
    
def get_weather(city):
    weather_key = 'a2b522eb4871084340746ab07b892975'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'celsius'}
    response = requests.get(url, params=params)
    weather = response.json()
    label['text'] = format_response(weather)
    
    
a=Tk()

canvas=Canvas(a,height=HIGHT,width=WIDTH)
canvas.pack()

#background=PhotoImage(file='weather.png')
#backgroundl=Label(a,image=background)
#background.place(relwidth=1, relheight=1)

frame=Frame(a,bg='#80c1ff',bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

entry=Entry(frame)
entry.place(relwidth=0.65,relheight=1)

button=Button(frame,text='Get Weather',font=40,command=lambda: get_weather(entry.get()))
button.place(relx=0.7,relheight=1,relwidth=0.3)

lower_frame=Frame(a,bg='#80c1ff',bd=10)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

label=Label(lower_frame)
label.place(relwidth=1,relheight=1)

a.mainloop()