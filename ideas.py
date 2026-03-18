import os
from datetime import datetime
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama" 
)

# --- DÍA 4: FUNCIÓN PARA GUARDAR EN ARCHIVO ---
def guardar_historial(tema, plataforma, ideas):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Abrimos (o creamos) el archivo en modo 'a' (append) para no borrar lo anterior
    with open("historial_ideas.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"\n{'='*50}\n")
        archivo.write(f"📅 FECHA: {fecha}\n")
        archivo.write(f"📱 PLATAFORMA: {plataforma}\n")
        archivo.write(f"🎹 BEAT: {tema}\n")
        archivo.write(f"{'='*50}\n\n")
        archivo.write(ideas)
        archivo.write("\n")
        
    print("💾 ¡Tus ideas se han guardado a salvo en 'historial_ideas.txt'!")

def generar_ideas():
    print("🔥 Generador de Ideas (NIVEL GOD - Menú e Historial) 🔥\n")
    
    # --- DÍA 5: MENÚ DE PLATAFORMAS ---
    print("¿Para dónde estamos creando hoy?")
    print("1. TikTok")
    print("2. Instagram Reels")
    print("3. YouTube Shorts")
    opcion = input("Elige un número (1/2/3): ")
    
    plataformas = {"1": "TikTok", "2": "Instagram Reels", "3": "YouTube Shorts"}
    plataforma = plataformas.get(opcion, "TikTok") # Si pones algo raro, va a TikTok por defecto
    
    tema = input("\n👉 Dime el tipo de beat (ej. trap emocional, drill oscuro): ")
    
    print(f"\nGenerando la estrategia para {plataforma} sobre '{tema}'... ⏳\n")
    
    try:
        # He ajustado el prompt para que entienda mejor la vibra del beat
        system_prompt = f"""Eres un experto en marketing musical para {plataforma} y creador de contenido para beatmakers.
        Habla como un productor urbano hispanohablante. Usa jerga: 'beat', 'track', 'hook', 'DAW'.
        Respeta el subgénero: si es Drill debe ser oscuro y callejero, si es Reggaeton debe ser para el club.
        Nunca uses palabras inventadas. Sé directo y creativo."""

        prompt_usuario = f"Dame 5 ideas virales para {plataforma} sobre beats tipo {tema}, incluyendo hook (los primeros 3 segundos), concepto del vídeo y título corto."
        
        respuesta = client.chat.completions.create(
            model="llama3.2:1b", 
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt_usuario}
            ],
            temperature=0.5 # Bajamos a 0.5 para que alucine menos y sea más lógico
        )
        
        ideas = respuesta.choices[0].message.content
        print("💡 AQUÍ TIENES TUS IDEAS VIRALES:\n")
        print(ideas)
        print("\n")
        
        # Llamamos a la función mágica que guarda todo
        guardar_historial(tema, plataforma, ideas)
        
    except Exception as e:
        print(f"\n❌ Ups, hubo un error al conectar con Ollama: {e}")

if __name__ == "__main__":
    generar_ideas()