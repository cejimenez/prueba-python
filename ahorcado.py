import random

def jugar_ahorcado():
    palabras = [
        "abogado", "abrigo", "aceite", "actriz", "acuario", "adulto", "aeropuerto", "agua", "aguja", "ajedrez",
        "almohada", "amigo", "anillo", "animal", "antena", "apellido", "arroz", "artista", "asiento", "astronauta",
        "ataque", "autobus", "basura", "batalla", "bateria", "bicicleta", "billete", "blanco", "bosque", "botella",
        "brillar", "caballo", "cabeza", "cadena", "calzado", "camino", "campana", "canasta", "canguro", "capitan",
        "carpeta", "carrera", "carroza", "carta", "castillo", "cebolla", "cerebro", "chaleco", "chocolate", "cientifico",
        "cinturon", "ciudad", "clima", "cocina", "codigo", "colegio", "collar", "comedor", "conejo", "corazon",
        "corona", "cristal", "cuaderno", "cuchillo", "deporte", "desierto", "diamante", "diente", "dinero", "dragon",
        "edificio", "ejemplo", "elefante", "energia", "espejo", "espina", "estrella", "familia", "fantasma", "farmacia",
        "fiesta", "flecha", "fuego", "galaxia", "gallina", "gato", "jirafa", "guitarra", "helado", "hermano",
        "hielo", "historia", "hueso", "idioma", "iglesia", "imagen", "insecto", "invierno", "isla", "jardin"
    ]
    
    palabra = random.choice(palabras).upper()
    letras_adivinadas = set()
    intentos_restantes = 6
    
    print("¡Bienvenido al juego del Ahorcado!")
    
    while intentos_restantes > 0:
        # Construye la palabra oculta, ej: A _ O _ A D O
        palabra_oculta = [letra if letra in letras_adivinadas else "_" for letra in palabra]
        print("\n" + "="*40)
        print("Palabra: ", " ".join(palabra_oculta))
        print(f"Intentos restantes: {intentos_restantes}")
        
        # Muestra qué letras ya ha intentado el jugador
        if letras_adivinadas:
            print(f"Letras usadas: {', '.join(sorted(letras_adivinadas))}")
        
        # Comprobar si ya ganó
        if "_" not in palabra_oculta:
            print("\n" + "="*40)
            print("¡Felicidades! Adivinaste la palabra correcta:", palabra)
            break
            
        # Pedir entrada al usuario
        letra = input("\nIngresa una letra: ").upper()
        
        # Validación: solo debe ingresar 1 letra y debe ser parte del alfabeto
        if len(letra) != 1 or not letra.isalpha():
            print("-> Error: Por favor, ingresa solo UNA letra válida.")
            continue
            
        # Validación: revisar si ya había ingresado esa letra
        if letra in letras_adivinadas:
            print(f"-> Ya habías intentado con la letra '{letra}'. Intenta con otra.")
            continue
            
        # Guardar la letra en el registro de intentos
        letras_adivinadas.add(letra)
        
        # Verificar si la letra está en la palabra secreta
        if letra not in palabra:
            print("-> ¡Letra incorrecta!")
            intentos_restantes -= 1
        else:
            print("-> ¡Bien, letra correcta!")
            
    else:  # Solo se ejecuta si el while termina de forma natural (intentos_restantes == 0) sin un 'break'
        print("\n" + "="*40)
        print("¡Perdiste! Te has quedado sin intentos.")
        print("La palabra correcta era:", palabra)

if __name__ == "__main__":
    jugar_ahorcado()
