def countdown(start_number: int) -> list[int]:
    """Genera una lista de cuenta regresiva desde start_number hasta 1.

    Args:
        start_number: Número entero desde el cual iniciar la cuenta regresiva.

    Returns:
        Lista de enteros en orden descendente desde start_number hasta 1.

    Raises:
        TypeError: Si start_number no es un entero.
    """
    if not isinstance(start_number, int):
        raise TypeError(
            f"start_number debe ser un entero, se recibió {type(start_number).__name__}"
        )

    countdown_values = []
    current = start_number
    while current >= 1:
        countdown_values.append(current)  # 1) usar append en vez de +=
        current -= 1                       # 2) decrementar después de agregar
    return countdown_values


if __name__ == "__main__":
    start_number = 5
    countdown_values = countdown(start_number)
    print("¡Cuenta regresiva completada!")
    print(countdown_values)