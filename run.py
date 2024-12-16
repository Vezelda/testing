import subprocess

# Ejecutar el servidor
def start_server():
    subprocess.Popen(["python3", "app/server.py"])

if __name__ == "__main__":
    start_server()
