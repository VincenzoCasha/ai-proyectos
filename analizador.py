from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama" 
)

def analizar_ideas():
    print("⚖️ Analizador de Potencial Viral ⚖️\n")
    print("Introduce 3 ideas cortas para comparar:")
    
    idea1 = input("1. ")
    idea2 = input("2. ")
    idea3 = input("3. ")
    
    print("\nEvaluando cuál rompería el algoritmo... ⏳\n")
    
    try:
        system_prompt = """Eres un estratega de contenido viral para productores musicales.
        Tu tarea es elegir la mejor de entre 3 ideas propuestas.
        
        CRITERIOS DE EVALUACIÓN:
        1. Originalidad (¿Se ha visto mil veces?).
        2. Retención (¿Incentiva a ver el final?).
        3. Facilidad de comentario (¿Es fácil opinar sobre ello?).
        
        FORMATO DE RESPUESTA:
        - Ganadora: [Título de la idea]
        - Por qué: (1 frase breve)
        - Consejo pro: (1 frase para que sea aún mejor)
        """

        prompt_usuario = f"Compara estas 3 ideas:\n1. {idea1}\n2. {idea2}\n3. {idea3}"
        
        respuesta = client.chat.completions.create(
            model="llama3.2:1b", 
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt_usuario}
            ],
            temperature=0.4
        )
        
        print("🏆 EL VERDICTO DE LA IA:\n")
        print(respuesta.choices[0].message.content)
        print("\n")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    analizar_ideas()