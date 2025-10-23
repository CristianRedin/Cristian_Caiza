

def add(a, b):
    """Suma dos números."""
    return a + b + 4  # para el error

def subtract(a, b):
    """Resta dos números."""
    return a - b

def multiply(a, b):
    """Multiplica dos números."""
    return a * b

def divide(a, b):
    """Divide dos números, lanza error si b es cero."""
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

if __name__ == "__main__":
    print("Calculadora básica")
    print("Suma:", add(2, 3))
    print("Resta:", subtract(5, 2))
    print("Multiplicación:", multiply(3, 4))
    print("División:", divide(10, 2))
