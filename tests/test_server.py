from app.server import broadcast

class MockSocket:
    def __init__(self):
        self.messages = []

    def sendall(self, message):
        self.messages.append(message)

    def recv(self, buffer_size):
        if self.messages:
            return self.messages.pop(0)
        return b""


def test_broadcast():
    """
    Prueba que el mensaje se envíe a todos los clientes excepto al emisor.
    """
    sender = MockSocket()
    client1 = MockSocket()
    client2 = MockSocket()

    global clientes
    clientes = [client1, client2]

    broadcast(b"Mensaje de prueba", exclude_client=sender)

    assert b"Mensaje de prueba" in client1.messages
    assert b"Mensaje de prueba" in client2.messages
