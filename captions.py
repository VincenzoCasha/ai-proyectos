from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama" 
)

def generar_captions():
    print("📱 Generador de Captions Virales V3 (Bypass de Filtros) 📱\n")
    
    beat_info = input("👉 Dime cómo es el beat (ej. Trap triste tipo Lil Peep con guitarra): ")
    
    print("\nEscribiendo un copy real y directo... ⏳\n")
    
    try:
        # Quitamos palabras como "asesina" o "demonios" que asustan al filtro de la IA
        system_prompt = """Eres un productor musical de habla hispana subiendo un beat a TikTok o Reels.
        Habla con flow, directo y con energía.
        
        REGLAS:
        - NADA de dar pena, ni ser poético.
        - Sé breve.
        - Añade CTA (llamada a la acción) para el link en la bio.
        
        EJEMPLOS DE CÓMO DEBES RESPONDER:
        Ejemplo 1: Esta guitarra te rompe el cuello 🎸🔥 ¿A qué artista escuchas aquí? Link en mi bio para el beat completo 🎧 #trapbeat #typebeat #lilpeep #guitartrap
        Ejemplo 2: Drill oscuro directo de UK 🥷🏽🇬🇧 ¿Quién la parte en este beat? Link en bio si quieres grabar encima. #ukdrill #centralcee #drillbeat #producer
        Ejemplo 3: Perreo old school pa' la disco 🍑🕺 Mencionad al artista que rompería esto 👇 Beat en la bio. #reggaeton #perreo #typebeat #badbunny
        """

        prompt_usuario = f"Escribe un caption corto siguiendo los ejemplos para este beat: {beat_info}"
        
        respuesta = client.chat.completions.create(
            model="llama3.2:1b", 
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt_usuario}
            ],
            temperature=0.4 
        )
        
        print("🔥 AQUÍ TIENES TU CAPTION:\n")
        print(respuesta.choices[0].message.content)
        print("\n")
        
    except Exception as e:
        print(f"\n❌ Ups, hubo un error al conectar con Ollama: {e}")

if __name__ == "__main__":
    generar_captions()