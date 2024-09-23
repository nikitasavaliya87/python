import requests
from tkinter import *
from datetime import datetime
# response=requests.get(url="http://api.open-notify.org/iss-now.json")
# #print(response)
# #print(response.status_code)
# response.raise_for_status()
# #data=response.json()["iss_position"]
# data=response.json()

# longitude=data["iss_position"]["longitude"]
# latitude=data["iss_position"]["latitude"]
# position=(longitude, latitude)
# print(position)



# def get_quote():
#     response=requests.get(url="https://api.kanye.rest/")
#     #print(response)
#     data=response.json()["quote"]
#     #quote_text = canvas.create_text(150, 207, text=data, width=250, font=("Arial", 30, "bold"), fill="white")
#     #print(data)
#     canvas.itemconfig(quote_text,text=data)


# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)

# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="ISS (International Space Station Current Location)overhead notifier/images/background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
# canvas.grid(row=0, column=0)

# kanye_img = PhotoImage(file="ISS (International Space Station Current Location)overhead notifier/images/kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)



# window.mainloop()
latitude=-38.116530
longitude=145.326610

position={
"lat":latitude,
"lng":longitude,
"formatted":0

}
response=requests.get(" https://api.sunrise-sunset.org/json",params=position)
response.raise_for_status()
data=response.json()
sunrise=data["results"]["sunset"].split("T")[1].split(":")[0]
sunset=data["results"]["sunrise"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

#print(data)

now=datetime.now()
print(now.hour)
