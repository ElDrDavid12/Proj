import matplotlib.pyplot as plt
import random
import time

def batalla(poblacion_tijera, poblacion_papel, poblacion_roca):
  """
  Simula una ronda de batalla entre las poblaciones de tijera, papel y roca.

  Args:
    poblacion_tijera: Número de individuos en la población de tijera.
    poblacion_papel: Número de individuos en la población de papel.
    poblacion_roca: Número de individuos en la población de roca.

  Returns:
    Una tupla con las nuevas poblaciones de tijera, papel y roca después de la batalla.
  """
  
  # Asegurar que las poblaciones no sean negativas
  poblacion_tijera = max(0, poblacion_tijera)
  poblacion_papel = max(0, poblacion_papel)
  poblacion_roca = max(0, poblacion_roca)

  opciones = ['tijera', 'papel', 'roca']
  batalla1 = random.choice(opciones)
  batalla2 = random.choice(opciones)

  ataque_tijera = random.randrange(0, poblacion_tijera + 1)  # +1 para incluir la posibilidad de ataque 0
  ataque_papel = random.randrange(0, poblacion_papel + 1)
  ataque_roca = random.randrange(0, poblacion_roca + 1)

  if (batalla1 == "tijera" and batalla2 == "papel") or (batalla1 == "papel" and batalla2 == "tijera"):
    poblacion_papel -= ataque_tijera
    poblacion_tijera += ataque_papel
  elif (batalla1 == "tijera" and batalla2 == "roca") or (batalla1 == "roca" and batalla2 == "tijera"):
    poblacion_tijera -= ataque_roca
    poblacion_roca += ataque_tijera
  elif (batalla1 == "roca" and batalla2 == "papel") or (batalla1 == "papel" and batalla2 == "roca"):
    poblacion_roca -= ataque_papel
    poblacion_papel += ataque_roca

  return poblacion_tijera, poblacion_papel, poblacion_roca


def simular_batalla(poblacion_inicial=100, num_rondas=100):
  """
  Simula una batalla de piedra, papel o tijera entre poblaciones.

  Args:
    poblacion_inicial: Número inicial de individuos en cada población.
    num_rondas: Número de rondas de batalla a simular.
  """

  poblacion_tijera = poblacion_inicial
  poblacion_papel = poblacion_inicial
  poblacion_roca = poblacion_inicial

  historial_poblaciones = {
      'tijera': [poblacion_tijera], 
      'papel': [poblacion_papel], 
      'roca': [poblacion_roca]
  }

  for ronda in range(num_rondas):
    poblacion_tijera, poblacion_papel, poblacion_roca = batalla(poblacion_tijera, poblacion_papel, poblacion_roca)

    historial_poblaciones['tijera'].append(poblacion_tijera)
    historial_poblaciones['papel'].append(poblacion_papel)
    historial_poblaciones['roca'].append(poblacion_roca)

    print("=" * 10)
    print("Ronda:", ronda + 1)
    print("Scissors Population:", poblacion_tijera)
    print("Paper Population:", poblacion_papel)
    print("Rock Population:", poblacion_roca)
    time.sleep(0.5)

  # Graficar los resultados
  plt.figure(figsize=(10, 6))
  plt.plot(historial_poblaciones['tijera'], label='Scissors')
  plt.plot(historial_poblaciones['papel'], label='Paper')
  plt.plot(historial_poblaciones['roca'], label='Rock')
  plt.xlabel("Rounds")
  plt.ylabel("Population")
  plt.title("Battle simulation: Rock, Paper, Scissors")
  plt.legend()
  plt.show()

# Iniciar la simulación
simular_batalla()