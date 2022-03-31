from tkinter import *
from api_test import pression,nuage_pourcent, vue_distance ,temp_fahrenheit, temp_celsius,feels_like_fahrenheit, feels_like_celsius, city, humidity, sunset_time, sunrise_time, weather1, wind_speed, humidity, description
import datetime as dt


print(f"Température a {city}: {temp_celsius:.2f}°C ou {temp_fahrenheit:.2f}°F")
print(f"Température a {city} ressentie: {feels_like_celsius:.2f}°C or {feels_like_fahrenheit:.2f}°F")
print(f"Température a {city}: {temp_celsius:.2f}°C ou {temp_fahrenheit:.2f}°F")
print(f"L'humiditée de {city}: {humidity:.2f}%")
print(f"la vitesse du vent: {wind_speed*3.6:.2f} km/h ou {wind_speed:.2f} m/s")
print(f'Description général de {city}: {description}')
print(f"Levée du soleil à {city} a {sunrise_time} heure local.")
print(f"Couché du soleil a {sunset_time} heure local")
print(f"la météo: {weather1}")
print(f"la description: {description}")
print(f"La vue: {vue_distance/1000:.2f} Kms")
print(f"Pourcentage de nuage:{nuage_pourcent} %")
print(f"Pression atmoshpèrique: {pression} hPa")



mainf = Tk()
mainf.title("Météo")
mainf.geometry("1000x800")
mainf.resizable(False, False)
photo1 = PhotoImage(file="um.png")
nb = Label(mainf, image=photo1, borderwidth=0)
nb.place(x=5, y=5)
#pour la vitesse du vent
Vitesse_vent = Label(mainf, text=f"Vitesse du vent: {wind_speed * 3.6:.2f} Km/h", font=("arial", 15), fg="black",bg="orange")
Vitesse_vent.place(x=20, y=80, height=40, width=300)
#pour l'humiditée
humide = Label(mainf, text=f"Le taux d'humiditée: {humidity} %", font=("arial", 15), fg="black",bg="orange")
humide.place(x=20, y=110, height=40, width=300)
#pour la temperature ressentie
temp_ressentie = Label(mainf, text=f"Température ressentie: {feels_like_celsius:.2f}°C", font=("arial", 15), fg="black",bg="orange")
temp_ressentie.place(x=20, y=140,width=300)
#pour la ville le nom
ville = Label(mainf, text=f"{city}",  font=("calibri bold", 38, ),  fg="black")
ville.place(x=375, y=5)
#pour image de fond de la visibilitée
photo1 = PhotoImage(file="vue.png")
nb = Label(mainf, image=photo1, borderwidth=0)
nb.place(x=90, y=570)
#label pour la visibilitée
visible = Label(mainf, text=f"Visibilitée à: {vue_distance/1000:.2f} Km",  font=("arial", 15),  fg="black")
visible.place(x=50, y=640)
#image pour la vitesse
photo4 = PhotoImage(file="nuage.png")
nb2 = Label(mainf, image=photo4)
nb2.place(x=700, y=540)
#image de fond le vent vittesse
Vitesse_vent2 = Label(mainf, text=f"Vent: {wind_speed * 3.6:.2f} Km/h", font=("arial", 15), fg="black")
Vitesse_vent2.place(x=715, y=640)

#bloc de droite
#pourcentage pour les nuages
nuage_densite = Label(mainf,text=f"Nuageux a: {nuage_pourcent} %", font=("arial", 15), fg="black",bg="orange")
nuage_densite.place(x=720, y=80, height=40, width=250)
#pour la pression
pression_atmo = Label(mainf,text=f"Pression: {pression} hPa", font=("arial", 15), fg="black",bg="orange")
pression_atmo.place(x=720, y=120, height=30, width=250)
#condition pour la meteo
if description == "couvert":
    photo2 = PhotoImage(file="nuageux.png")
    nb1 = Label(mainf, image=photo2, borderwidth=0)
    nb1.place(x=292, y=140)

if description == "légère pluie":
    photo3 = PhotoImage(file="rain.png")
    nb2 = Label(mainf, image=photo3)
    nb2.place(x=335,y=190)


if description =="nuageux":
    photo5 = PhotoImage(file="mainnuageuex.png")
    nb3 = Label(mainf, image=photo5)
    nb3.place(x=292, y=190)


#definir l'heure
def clock():
    now = dt.datetime.now()
    huur = now.strftime("%H:%M")
    lab.config(text=huur)
    lab.after(100, clock)

#température en celsuis
temp = Label(mainf, text=f"{temp_celsius:.2f}°C", font=("arial", 35), fg ="red")
temp.place(x=390, y=459)
#pour afficher l'heure
lab = Label(mainf, text="", font=("arial bold",23), fg="black")
lab.place(x=40, y=20)
clock()

mainf.mainloop()

