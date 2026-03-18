from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama" 
)

def generar_titulos():
    print("🎧 Generador de Títulos SEO para Beats (YouTube/Beatstars) V2 🎧\n")
    
    artistas = input("👉 ¿A qué artistas suena este beat? (ej. Central Cee x Pop Smoke): ")
    vibra = input("👉 ¿Cuál es la vibra o mood? (ej. aggressive drill, dark trap): ")
    
    print(f"\nGenerando títulos profesionales para '{artistas}'... ⏳\n")
    
    try:
        # APLICAMOS LA TÉCNICA "FEW-SHOT" (darle ejemplos exactos)
        system_prompt = """Eres el mejor experto en SEO de YouTube para productores urbanos.
        Generas títulos para vender beats instrumentales. 
        REGLAS ESTRICTAS:
        - No uses corchetes literales como [Vibra] o [Artistas].
        - Los nombres de los beats deben estar en MAYÚSCULAS y sonar épicos, oscuros o callejeros (en inglés o español corto).
        - Añade la vibra al final separada por un "|".
        - NO escribas texto de introducción como "¡Claro! Aquí tienes". DA SOLO LA LISTA.
        
        EJEMPLOS EXACTOS DEL FORMATO QUE DEBES DEVOLVER:
        1. Central Cee x Pop Smoke Type Beat - "GHOST" | Aggressive Drill
        2. Bad Bunny x Mora Type Beat - "PERREO" | Reggaeton Oscuro
        3. Travis Scott x Don Toliver Type Beat - "NIGHTMARE" | Dark Chill Trap
        """

        prompt_usuario = f"Dame 5 opciones de títulos siguiendo exactamente el formato de los ejemplos. Los artistas son: {artistas}. La vibra es: {vibra}."
        
        respuesta = client.chat.completions.create(
            model="llama3.2:1b", 
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt_usuario}
            ],
            temperature=0.6 # Bajamos un poco la creatividad para que respete el formato estricto
        )
        
        print("🔥 AQUÍ TIENES TUS TÍTULOS PRO:\n")
        print(respuesta.choices[0].message.content)
        print("\n")
        
    except Exception as e:
        print(f"\n❌ Ups, hubo un error al conectar con Ollama: {e}")

if __name__ == "__main__":
    generar_titulos()