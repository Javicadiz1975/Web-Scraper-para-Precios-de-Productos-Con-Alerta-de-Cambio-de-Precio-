# Web Scraper de Precios con Alerta por Correo Electrónico

Este proyecto es un script en Python que realiza un seguimiento del precio de un producto en una página web específica. Cuando el precio del producto baja hasta o por debajo de un valor objetivo, el script envía una alerta por correo electrónico al usuario para notificarle la caída del precio.

## Características

- Obtiene el precio de un producto desde una página web.
- Compara el precio actual con un precio objetivo.
- Envía un correo electrónico de alerta cuando el precio cae por debajo del precio objetivo.
- Revisa el precio cada hora automáticamente.

## Requisitos

- Python 3.x
- Librerías: `requests`, `BeautifulSoup`, `smtplib`

Puedes instalar las librerías necesarias con el siguiente comando:
```bash
pip install requests beautifulsoup4