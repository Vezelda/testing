def validate_message(message):
    """
    Valida que el mensaje cumpla con las reglas básicas:
    - No debe estar vacío.
    - Debe tener una longitud menor o igual a 1024 caracteres.
    """
    return bool(message.strip()) and len(message) <= 1024
