import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#tomar de un archivo de texto las direcciones para enviar correos, leer linea por linea y pasarlas a una lista, después en un for enviarlos

with open("./archivocorreos.txt") as file:
    listacorreo = file.readlines()
    listacorreo = [line.rstrip() for line in listacorreo]


msg = MIMEMultipart()
msg['Subject'] = 'Hey hey hola'
message = 'Un saludo'
msg.attach(MIMEText(message))

user = input("escriba su usuario para mandar correos")
passwrd = input("escriba su contrasena")

mailserver = smtplib.SMTP('smtp.gmail.com',587)
# identify ourselves to smtp gmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
mailserver.login(user, passwrd)

#ciclo for para enviar los correos y dentro va el try except
n=0
for element in listacorreo:
    try:
        mailserver.sendmail(user, [element],msg.as_string())
        print("Correo enviado exitosamente")
    except:
        print("No ha sido posible enviar el correo")



mailserver.quit()