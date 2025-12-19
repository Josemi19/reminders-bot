import requests
import time
import os
from dotenv import load_dotenv
from datetime import datetime, timezone

# Cargar variables desde un archivo .env (si existe)
load_dotenv()

# --- 1. CONFIGURACIÓN (¡REEMPLAZA ESTO!) ---
# Pega aquí el Token que te dio BotFather
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") or os.environ.get("TELEGRAM_BOT_TOKEN")
# Pega aquí el ID del chat que obtuviste
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID") or os.environ.get("TELEGRAM_CHAT_ID")

# URL base de la API de Telegram para enviar mensajes
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

# --- 2. Mensaje Personalizable con formato Markdown ---
def obtener_mensaje_recordatorio(nombre="preciosa"):
    """
    Función para construir el mensaje con formato.
    Telegram usa Markdown para formato.
    """
    mensaje = (
        f"Hola {nombre}, *¡ALERTA DE PÍLDORA DIARIA!* 🚨\n\n" # Negritas (*)
        "Es hora de tomar tu pastilla anti bebes. ✨\n"
        "No olvides tomarla a tiempo. ¡Te amo! ❤️"
    )
    return mensaje

# --- 3. La Función de Envío ---
def enviar_telegram(mensaje):
    token = TOKEN
    chat_id = CHAT_ID
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    
    payload = {
        "chat_id": chat_id,
        "text": mensaje,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, data=payload)
        
        if response.status_code == 200:
            print(f"✅ Recordatorio enviado exitosamente a las {time.strftime('%H:%M:%S')}")
        else:
            print(f"❌ Error al enviar. Código: {response.status_code}, Respuesta: {response.text}")

    except Exception as e:
        print(f"❌ Error en la función de envío: {e}")

def decidir_mensaje():
    # Obtenemos la hora actual en UTC
    hora_utc = datetime.now(timezone.utc).hour
    
    # Lógica según la hora UTC (Ajusta según tus cron del YAML)
    if 12 <= hora_utc <= 14:
        return (f"Hola Trollsita, *¡ALERTA DE PÍLDORA DIARIA!* 🚨\n\n" # Negritas (*)
        "Es hora de tomar tu pastilla anti bebes. ✨\n"
        "No olvides tomarla a tiempo. ¡Te amo! ❤️")
    
    elif 1 <= hora_utc <= 3:
        return "🌙 *¡Buenas noches!* Es hora de la última pastilla. Descansa mucho, te quiero. ✨"
    
    else:
        # Mensaje por defecto por si lo activas manualmente
        return "🔔 Este es un recordatorio manual de tu bot favorito."

if __name__ == "__main__":
    texto = decidir_mensaje()
    enviar_telegram(texto)