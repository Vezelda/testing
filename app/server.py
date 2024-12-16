import socket
import threading

# Lista global para clientes conectados
clientes = []

def broadcast(message, exclude_client=None):
    for client in clientes:
        if client is not exclude_client:
            try:
                client.sendall(message)
            except Exception as e:
                print(f"Error al enviar mensaje: {e}")


def handle_client(cliente):
    try:
        message = cliente.recv(1024)
        if message:
            cliente.sendall(message)  # Reenvía el mensaje recibido.
        else:
            print("Conexión cerrada por el cliente.")
    except socket.timeout:
        print("Tiempo de espera agotado.")
    except Exception as e:
        print(f"Error en cliente: {e}")
    finally:
        cliente.close()


def start_server():
    """
    Inicia el servidor.
    """
    host = "127.0.0.1"
    port = 54321

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Permitir reutilizar el puerto
    server.bind((host, port))
    server.listen(5)
    print(f"Servidor escuchando en {host}:{port}")

    try:
        while True:
            cliente, _ = server.accept()
            clientes.append(cliente)
            thread = threading.Thread(target=handle_client, args=(cliente,))
            thread.start()
    except KeyboardInterrupt:
        print("Servidor detenido")
    finally:
        server.close()
