import requests
import os
from datetime import datetime, timezone

# --- 1. CONFIGURACIÓN (¡REEMPLAZA ESTO!) ---
# Pega aquí el Token que te dio BotFather
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") or os.environ.get("TELEGRAM_BOT_TOKEN")
# Pega aquí el ID del chat que obtuviste
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID") or os.environ.get("TELEGRAM_CHAT_ID")

# URL base de la API de Telegram para enviar mensajes
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

# # --- 2. Mensaje Personalizable con formato Markdown ---
# def obtener_mensaje_recordatorio(nombre="preciosa"):
#     """
#     Función para construir el mensaje con formato.
#     Telegram usa Markdown para formato.
#     """
#     mensaje = (
#         f"Hola {nombre}, *¡ALERTA DE PÍLDORA DIARIA!* 🚨\n\n" # Negritas (*)
#         "Es hora de tomar tu pastilla anti bebes. ✨\n"
#         "No olvides tomarla a tiempo. ¡Te amo! ❤️"
#     )
#     return mensaje

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
    ahora_utc = datetime.now(timezone.utc)
    hora = ahora_utc.hour
    minuto = ahora_utc.minute

    # Mensajes personalizados según el horario de Venezuela
    # Usamos rangos de hora para absorber pequeños retrasos de GitHub
    
    # 07:55 VET es 11:55 UTC
    if hora == 11 or (hora == 12 and minuto < 15):
        return (
        f"Hola trollsita, *¡ALERTA DE PÍLDORA DIARIA!* 🚨\n\n" # Negritas (*)
        "Es hora de tomar tu pastilla anti bebes. ✨\n"
        "No olvides tomarla a tiempo. ¡Te amo! ❤️"
    )
    
    # 12:55 VET es 16:55 UTC
    elif hora == 16 or (hora == 17 and minuto < 15):
        return (
        f"Trollsita, *¡SEGUNDA PASTILLA DEL DÍA!* 🚨\n\n" # Negritas (*)
        "Es hora de tomar la metformina. ✨\n"
        "No olvides tomarla a tiempo."
        )
    
    
    # 18:55 VET es 22:55 UTC
    elif hora == 22 or (hora == 23 and minuto < 15):
        return (
        f"Buenas noches trollsita, *¡TERCERA Y ÚLTIMA PASTILLA!* 🚨\n\n" # Negritas (*)
        "Turno de la atorvastatina (vaya nombre). ✨\n"
        "No olvides tomarla a tiempo. ¡Te amo! ❤️"
        )
    
    else:
        return "🔔 *Recordatorio manual:* El bot se ha ejecutado fuera del horario programado."

if __name__ == "__main__":
    # Evitar que el script falle si los secretos no están configurados
    if not os.environ.get("TELEGRAM_TOKEN") or not os.environ.get("TELEGRAM_CHAT_ID"):
        print("❌ Error: TELEGRAM_TOKEN o TELEGRAM_CHAT_ID no configurados en los secretos de GitHub.")
    else:
        mensaje = decidir_mensaje()
        enviar_telegram(mensaje)
