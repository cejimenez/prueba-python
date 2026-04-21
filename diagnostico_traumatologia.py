def diagnostico_rodilla():
    print("=" * 60)
    print("   ASISTENTE DE DIAGNÓSTICO DIFERENCIAL (TRAUMATOLOGÍA)")
    print("                 Foco: Dolor de Rodilla")
    print("=" * 60)
    print("Responda las siguientes preguntas para orientar el diagnóstico.\n")

    print("1. ¿Cuál fue el mecanismo del dolor?")
    print("   [1] Traumático (Golpe agudo, torsión brusca, caída)")
    print("   [2] Insidioso o Crónico (Apareció poco a poco, desgaste)")
    
    origen = input("> Seleccione (1 o 2): ")

    if origen == "1":
        print("\n--- INICIO TRAUMÁTICO ---")
        chasquido = input("¿El paciente sintió/escuchó un chasquido ('pop') seguido de inflamación rápída (hemartros)? (S/N): ").strip().upper()
        if chasquido == "S":
            print("\n>> DIAGNÓSTICO SUGERIDO:")
            print("Posible rotura del Ligamento Cruzado Anterior (LCA) o fractura osteocondral.")
            print("\n>> RECOMENDACIÓN:")
            print("Prueba de Lachman. Evitar apoyo, inmovilizar temporalmente y solicitar Resonancia Magnética.")
        else:
            torsion = input("¿El mecanismo fue girar el cuerpo con el pie fijo en el suelo y hay dolor en la parte interna? (S/N): ").strip().upper()
            if torsion == "S":
                print("\n>> DIAGNÓSTICO SUGERIDO:")
                print("Posible lesión de menisco interno o esguince del Ligamento Colateral Medial.")
                print("\n>> RECOMENDACIÓN:")
                print("Maniobras de McMurray / Apley. Prueba de bostezo articular.")
            else:
                print("\n>> DIAGNÓSTICO SUGERIDO:")
                print("Contusión ósea o muscular, o esguince genérico leve. Tratar con RICE (Reposo, Hielo, Compresión, Elevación) y reevaluar.")
                
    elif origen == "2":
        print("\n--- INICIO INSIDIOSO O CRÓNICO ---")
        escaleras = input("¿El dolor es en la parte frontal (anterior) y empeora al subir/bajar escaleras o estar mucho tiempo sentado? (S/N): ").strip().upper()
        if escaleras == "S":
            print("\n>> DIAGNÓSTICO SUGERIDO:")
            print("Síndrome de dolor Femoropatelar (Condromalacia rotuliana).")
            print("\n>> RECOMENDACIÓN:")
            print("Radiografía axial de rótula. Prescribir kinesiología para fortalecimiento del Vasto Medial Oblicuo.")
        else:
            edad = input("¿El paciente tiene más de 50 años y presenta rigidez articular matutina (menor a 30 mins) que cede al calentar? (S/N): ").strip().upper()
            if edad == "S":
                print("\n>> DIAGNÓSTICO SUGERIDO:")
                print("Posible Artrosis de Rodilla (Osteoartritis gonartrosis).")
                print("\n>> RECOMENDACIÓN:")
                print("Radiografía de rodilla AP y Lateral *con carga* (de pie).")
            else:
                tendon = input("¿Hay dolor localizado y sensible justo debajo de la rótula (polo inferior) exacerbado por saltos? (S/N): ").strip().upper()
                if tendon == "S":
                    print("\n>> DIAGNÓSTICO SUGERIDO:")
                    print("Tendinopatía rotuliana ('Rodilla de saltador').")
                else:
                    print("\n>> DIAGNÓSTICO SUGERIDO:")
                    print("Dolor inespecífico intraarticular. Requiere exploración física exhaustiva (Pata de ganso, banda iliotibial, etc).")
    else:
        print("\n[!] Opción no válida. Por favor, reinicie el programa e ingrese 1 o 2.")

    print("\n" + "=" * 60)
    print("NOTA LEGAL: Este sistema es solo un flujo de apoyo educativo.")
    print("El diagnóstico definitivo y tratamiento deben basarse siempre en")
    print("el juicio clínico del médico y pruebas de imagen confirmatorias.")
    print("=" * 60)

if __name__ == "__main__":
    diagnostico_rodilla()
