def calcular_letra(promedio):
    if 1 <= promedio <= 10:
        return 'F'
    elif 11 <= promedio <= 20:
        return 'E'
    elif 21 <= promedio <= 30:
        return 'D'
    elif 31 <= promedio <= 40:
        return 'C'
    elif 41 <= promedio <= 50:
        return 'B'
    elif 61 <= promedio <= 100:
        return 'A'
    else:
        return 'Promedio fuera de rango'

# Solicitar al usuario las 4 notas
notas = []
for i in range(1, 5):
    nota = float(input(f"Ingresa la nota {i}: "))
    notas.append(nota)

# Calcular el promedio
promedio = sum(notas) / 4

# Obtener y mostrar la letra correspondiente
letra = calcular_letra(promedio)
print(f"Tu promedio es: {promedio}, lo que corresponde a la letra: {letra}")
