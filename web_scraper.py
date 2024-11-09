import requests
from bs4 import BeautifulSoup
import time
import smtplib

def obtener_precio():
    url = "https://www.example.com/product-page"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    
    precio = float(soup.find("span", {"class": "price"}).text.replace("$", ""))
    return precio

def enviar_alerta(precio_actual):
    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    servidor.starttls()
    servidor.login("tuemail@gmail.com", "tucontraseña")
    mensaje = f"¡El precio ha bajado a ${precio_actual}!"
    servidor.sendmail("tuemail@gmail.com", "destinatario@gmail.com", mensaje)
    servidor.quit()

precio_objetivo = 100.0  # Precio deseado para la alerta

while True:
    precio_actual = obtener_precio()
    if precio_actual <= precio_objetivo:
        enviar_alerta(precio_actual)
        break
    time.sleep(3600)  # Revisa cada hora