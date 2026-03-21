start_number = 5
countdown_values = []

# Agregar primero el valor inicial
current = start_number
while current >= 1:
    countdown_values.append(current)  # 1) usar append en vez de +=
    current -= 1                       # 2) decrementar después de agregar

print("Discount countdown complete!")
print(countdown_values)