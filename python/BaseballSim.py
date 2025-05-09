import random

# Definir probabilidades para los resultados de cada turno al bate
resultados = {
    "hit": 0.3,
    "out": 0.6,
    "error": 0.1
}

def simular_turno():
    """Simula el turno de un bateador basado en las probabilidades."""
    r = random.random()  # valor entre 0 y 1
    acumulado = 0
    for resultado, prob in resultados.items():
        acumulado += prob
        if r < acumulado:
            return resultado
    return "out"  # fallback

def simular_inning():
    """Simula una mitad de entrada hasta conseguir 3 outs.
       Retorna la cantidad de carreras anotadas."""
    outs = 0
    carreras = 0
    while outs < 3:
        resultado = simular_turno()
        print(f"Resultado del turno: {resultado}")
        if resultado == "hit":
            # Simplificando: cada hit anota una carrera
            carreras += 1
            print("¡Carrera!")
        elif resultado == "out":
            outs += 1
            print(f"Out! ({outs}/3)")
        elif resultado == "error":
            # Error: se anota carrera sin contar como out
            carreras += 1
            print("Error, carrera automática!")
    return carreras

def simular_partido():
    """Simula un partido con 9 entradas para cada equipo."""
    total_innings = 9
    puntaje_local = 0
    puntaje_visitante = 0
    
    for inning in range(1, total_innings+1):
        print(f"\n--- Entrada {inning} ---")
        print("Turno de los visitantes:")
        carreras_visitante = simular_inning()
        puntaje_visitante += carreras_visitante
        print(f"Carreras esta entrada (visitantes): {carreras_visitante}")
        
        print("Turno de los locales:")
        carreras_local = simular_inning()
        puntaje_local += carreras_local
        print(f"Carreras esta entrada (locales): {carreras_local}")
    
    print("\n--- Resultado Final ---")
    print(f"Visitantes: {puntaje_visitante}")
    print(f"Locales: {puntaje_local}")
    if puntaje_local > puntaje_visitante:
        print("¡Ganaron los locales!")
    elif puntaje_visitante > puntaje_local:
        print("¡Ganaron los visitantes!")
    else:
        print("Empate.")

if __name__ == "__main__":
    simular_partido()