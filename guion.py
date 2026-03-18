import os
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama" 
)

def generar_guion():
    print("🎬 Generador de Guiones de TikTok V2 (Minimalista Extremo) 🎬\n")
    
    idea = input("👉 Dime la idea del vídeo (ej. Hacer un beat con una lata): ")
    
    print("\nEstructurando un guion directo y sin relleno... ⏳\n")
    
    try:
        # System Prompt: Reglas absolutas y ejemplos 100% minimalistas
        system_prompt = """Eres un creador de TikTok minimalista y directo.
        Tu estilo es rápido: cero relleno, directo al grano.
        
        REGLA ABSOLUTA: Tu respuesta debe tener EXACTAMENTE 3 LÍNEAS. 
        ESTÁ PROHIBIDO añadir introducciones, conclusiones, consejos o herramientas.
        
        FORMATO OBLIGATORIO:
        [HOOK]: (Qué dices a cámara en 1 frase corta)
        [VISUAL]: (Qué grabas con el móvil en 1 frase)
        [CTA]: (Llamada a la acción en 1 frase)
        
        EJEMPLO DE RESPUESTA PERFECTA:
        [HOOK]: Hice un beat de trap usando solo una lata de Monster.
        [VISUAL]: Abres la lata cerca del micro, lo pasas al DAW y lo conviertes en un hi-hat.
        [CTA]: Comenta 'LATA' y te paso el drum kit gratis.
        """

        prompt_usuario = f"Crea el guion ultra-minimalista para esta idea: {idea}"
        
        respuesta = client.chat.completions.create(
            model="llama3.2:1b", 
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt_usuario}
            ],
            temperature=0.2 # Temperatura bajísima: esto obliga al modelo a ser casi robótico y no inventar secciones
        )
        
        print("🔥 AQUÍ TIENES TU GUION MINIMALISTA:\n")
        print(respuesta.choices[0].message.content)
        print("\n")
        
    except Exception as e:
        print(f"\n❌ Ups, hubo un error al conectar con Ollama: {e}")

if __name__ == "__main__":
    generar_guion()