from twilio.rest import Client
import schedule
import time
import os
from dotenv import load_dotenv

# Cargar variables desde un archivo .env (si existe)
load_dotenv()

# --- 1. Credenciales y Configuración (¡IMPORTANTE!) ---
# Reemplaza estas variables con tus propias credenciales de Twilio
ACCOUNT_SID = os.getenv("ACCOUNT_SID") # "TU_ACCOUNT_SID"
AUTH_TOKEN = os.getenv("AUTH_TOKEN") # "TU_AUTH_TOKEN"
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER") # Número de Twilio Sandbox o tu número oficial
RECIPIENT_NUMBER = os.getenv("RECIPIENT_NUMBER") # El número del receptor, con código de país

client = Client(ACCOUNT_SID, AUTH_TOKEN)

# --- 2. Mensaje Personalizable ---
def obtener_mensaje_recordatorio(nombre="preciosa"):
    """
    Función para obtener un mensaje por defecto o personalizado.
    """
    # **Mensaje por defecto (si no personalizas):**
    # mensaje_defecto = "Hola, ¡es hora de tomar tu píldora anticonceptiva! ❤️ No lo olvides."
    
    # **Mensaje Personalizado:**
    mensajes = [
        f"¡Hola, {nombre}! Solo para recordarte que ya es la hora de tu súper píldora. Tómala ahora mismo. ¡Te quiero!",
        f"Recordatorio diario: {nombre}, es hora de tomar la píldora. ¡Hazlo antes de que se te olvide! 😉",
        f"¡Alerta de píldora para mi {nombre}! Tómala y tómate un minuto para ti. Lindo día."
    ]
    # Puedes usar un índice fijo o elegir uno aleatoriamente. Usaremos el primero por simplicidad.
    return mensajes[0]

# --- 3. La Función de Envío ---
def enviar_recordatorio():
    """
    Envía el mensaje de WhatsApp usando la API de Twilio.
    """
    try:

        message = client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            content_sid='HX9e2fe5361eb23368a348ff248d105d43',
            to=RECIPIENT_NUMBER
        )
        print(f"✅ Recordatorio enviado exitosamente. SID: {message.sid}")
    except Exception as e:
        print(f"❌ Error al enviar el mensaje: {e}")

# --- 4. Programación de la Tarea ---
# Programa la función para que se ejecute diariamente a la hora deseada (ej. 8:00 AM)
# Usa el formato de 24 horas (HH:MM)
HORA_RECORDATORIO = "07:55"  # Cambia esto a la hora que desees

schedule.every().day.at(HORA_RECORDATORIO).do(enviar_recordatorio)

print(f"El bot está corriendo. Programado para enviar a las {HORA_RECORDATORIO} todos los días.")

# Bucle principal que verifica continuamente el horario
while True:
    schedule.run_pending()
    time.sleep(1) # Espera 1 segundo antes de volver a verificar

# Nota: Para parar el script, presiona Ctrl+C en la terminal.