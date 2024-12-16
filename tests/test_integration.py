import socket
import threading
import time
import pytest
from app.server import start_server

@pytest.fixture(scope="function", autouse=True)
def setup_server():
    """
    Inicia y detiene el servidor automáticamente para cada prueba.
    """
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()

    time.sleep(1)  # Espera breve para asegurar que el servidor está listo
    yield

def test_multiple_clients():
    """
    Prueba la interacción entre múltiples clientes.
    """
    def client_action(messages, received):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect(("127.0.0.1", 54321))
            for msg in messages:
                client.sendall(msg.encode())
                time.sleep(0.1)
            for _ in range(len(messages)):
                response = client.recv(1024).decode()
                received.append(response)

    received1 = []
    received2 = []

    thread1 = threading.Thread(target=client_action, args=(["Mensaje de cliente 1"], received1))
    thread2 = threading.Thread(target=client_action, args=(["Mensaje de cliente 2"], received2))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    # Verifica que ambos clientes recibieron los mensajes correctos
    assert "Mensaje de cliente 1" in received2
    assert "Mensaje de cliente 2" in received1
