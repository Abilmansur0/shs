def check_password(password):
    # Проверка на минимальную длину
    if len(password) < 8:
        return False

    # Проверка на наличие хотя бы одной цифры
    if not any(char.isdigit() for char in password):
        return False

    # Проверка на наличие хотя бы одной заглавной буквы
    if not any(char.isupper() for char in password):
        return False

    # Проверка на наличие хотя бы одной строчной буквы
    if not any(char.islower() for char in password):
        return False

    # Если все условия выполнены
    return True

# Примеры использования
print(check_password("Password123"))  # True
print(check_password("password"))     # False
print(check_password("PASSWORD"))     # False
print(check_password("Pass123"))      # False
