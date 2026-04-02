def countdown(start_number):
    """Generate a countdown list from start_number down to 1."""
    countdown_values = []
    current = start_number
    while current >= 1:
        countdown_values.append(current)  # 1) usar append en vez de +=
        current -= 1                       # 2) decrementar después de agregar
    return countdown_values


if __name__ == "__main__":
    # Agregar primero el valor inicial
    start_number = 5
    countdown_values = countdown(start_number)
    print("Discount countdown complete!")
    print(countdown_values)