import os
# Importamos las funciones de tus scripts anteriores
from ideas import generar_ideas
from titulos import generar_titulos
from captions import generar_captions
from guion import generar_guion
from analizador import analizar_ideas

def limpiar_pantalla():
    # Limpia la terminal según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    while True:
        limpiar_pantalla()
        print("="*40)
        print("🚀 BEATMAKER AI - TOOLKIT PROFESIONAL 🚀")
        print("="*40)
        print("1. 💡 Generador de Ideas (TikTok/Reels)")
        print("2. 🎧 Generador de Títulos SEO (YT/Beatstars)")
        print("3. 📱 Generador de Captions (Social Media)")
        print("4. 🎬 Generador de Guiones (Minimalista)")
        print("5. ⚖️  Analizador de Ideas (Versus)")
        print("0. ❌ Salir")
        print("-"*40)
        
        opcion = input("👉 Elige una herramienta: ")

        if opcion == "1":
            limpiar_pantalla()
            generar_ideas()
            input("\nPresiona Enter para volver al menú...")
        elif opcion == "2":
            limpiar_pantalla()
            generar_titulos()
            input("\nPresiona Enter para volver al menú...")
        elif opcion == "3":
            limpiar_pantalla()
            generar_captions()
            input("\nPresiona Enter para volver al menú...")
        elif opcion == "4":
            limpiar_pantalla()
            generar_guion()
            input("\nPresiona Enter para volver al menú...")
        elif opcion == "5":
            limpiar_pantalla()
            analizar_ideas()
            input("\nPresiona Enter para volver al menú...")
        elif opcion == "0":
            print("¡Nos vemos en el estudio! 👋")
            break
        else:
            print("Opcíon no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu_principal()