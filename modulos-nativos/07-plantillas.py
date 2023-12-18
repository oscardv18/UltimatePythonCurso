from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

plantilla = Path("modulos-nativos/plantillas.html").read_text("utf-8")
template = Template(plantilla)
# body = template.substitute({"usuario": "Oscar"})
body = template.substitute(usuario="Oscar")

image_path = Path("modulos-nativos/img.png")

message = MIMEMultipart()
message["from"] = "Hola Mundo"
message["to"] = "oscarddiazvelasquez@gmail.com"
message["subject"] = "Esta es una prueba"
body = MIMEText(body, "html")
mime_image = MIMEImage(image_path.read_bytes())
message.attach(body)
message.attach(mime_image)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("oscarddiazvelasquez@gmail.com", "12345")
    smtp.send_message(message)
    print("Mensaje enviado!")
