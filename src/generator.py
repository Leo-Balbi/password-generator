from utils import generate_password, save_password

if __name__ == "__main__":
    level = input("Elige la complejidad (low, medium, high): ")
    length = int(input("Elige la longitud: "))

    new_password = generate_password(length, level)
    print("Tu contraseña segura es:", new_password)

    save_password(new_password)
    print("Se ha guardado en data/passwords.txt")