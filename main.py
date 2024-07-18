import requests
from tkinter import *
import os
from PIL import ImageTk, Image

api_key = 'API_key'

def fetch_weather_data(city):
    complete_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(complete_url)
    return response.json()
def display_weather_data(weather_data):
    if weather_data['cod'] != '404':
        main_data = weather_data['main']
        humidity = main_data['humidity']
        temperature = main_data['temp'] - 273.15
        weather_description = weather_data['weather'][0]['description']

        result_label.config(text=f"Temperature: {temperature:.2f}°C\nHumidity: {humidity}%\nWeather: {weather_description.capitalize()}")
    else:
        result_label.config(text="City not found. Please try again.")

def main_data():
    city = entry.get()
    if city:
        weather_data = fetch_weather_data(city)
        display_weather_data(weather_data)
    else:
        result_label.config(text="Please enter a city.")

root = Tk()
root.geometry("400x500")
root.resizable(0,0)
root.title("Weather App")

canvas = Canvas(root, width=250, height=250)
canvas.pack()

image_path = r"C:\Users\efeba\OneDrive\Masaüstü\pic\weather_removed_bg.png"

if os.path.exists(image_path):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((200, 200), Image.LANCZOS)
    img = ImageTk.PhotoImage(resized_image)
    canvas.create_image(20, 20, anchor=NW, image=img)

else:
    print(f"Error: The file '{image_path}' does not exist.")

label1 = Label(text="Enter City:")
label1.pack()

entry = Entry(width=30)
entry.pack()

get_weather_button = Button(text="Check Weather", font="Verdana 10", command=main_data)
get_weather_button.config(pady=5)
get_weather_button.pack(pady=10)

result_label = Label(root, text="")
result_label.pack()

root.mainloop()
