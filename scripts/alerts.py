import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_alert(ciudad, temperatura, humedad, presion, viento, descripcion, fecha, email, limites=None):
    if limites is None:
        limites = {
            "temperatura": {"min": -10, "max": 40},
            "humedad": {"min": 20, "max": 80},
            "presion": {"min": 980, "max": 1050},
            "viento": {"max": 100}
        }

    if (temperatura < limites["temperatura"]["min"] or 
        temperatura > limites["temperatura"]["max"] or 
        humedad < limites["humedad"]["min"] or 
        humedad > limites["humedad"]["max"] or 
        presion < limites["presion"]["min"] or 
        presion > limites["presion"]["max"] or 
        viento > limites["viento"]["max"]):

        # Crear el mensaje
        msg = MIMEMultipart()
        msg['From'] = 'alertas@tuapp.com'
        msg['To'] = email
        msg['Subject'] = f"Alerta meteorológica para {ciudad}"

        body = f"""
        Alerta meteorológica para la ciudad {ciudad}:
        Fecha: {fecha}
        Temperatura: {temperatura}°C
        Humedad: {humedad}%
        Presión: {presion} hPa
        Viento: {viento} km/h
        Descripción: {descripcion}

        Parámetros límite:
        Temperatura: {limites['temperatura']['min']}°C a {limites['temperatura']['max']}°C
        Humedad: {limites['humedad']['min']}% a {limites['humedad']['max']}%
        Presión: {limites['presion']['min']} hPa a {limites['presion']['max']} hPa
        Viento: Hasta {limites['viento']['max']} km/h
        """

        msg.attach(MIMEText(body, 'plain'))

        # Enviar el email
        server = smtplib.SMTP('smtp.sendgrid.net', 587)
        server.starttls()
        server.login("apikey", "TU_SENDGRID_API_KEY")
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()

        print(f"Alerta enviada a {email} sobre la ciudad {ciudad}")