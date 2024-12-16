from app.utils import validate_message

def test_validate_message():
    """Prueba que los mensajes válidos sean aceptados."""
    assert validate_message("Hello") == True
    assert validate_message("") == False
    assert validate_message(" " * 1025) == False
