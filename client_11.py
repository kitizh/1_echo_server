import socket
import threading

def listen_for_messages(sock):
    while True:
        data, _ = sock.recvfrom(1024)
        print(f"Сообщение: {data.decode('utf-8')}")

def start_udp_chat_client(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        server_address = (host, port)
        print(f"Подключение к серверу {host}:{port}...")

        threading.Thread(target=listen_for_messages, args=(client_socket,), daemon=True).start()

        try:
            while True:
                message = input("Введите сообщение (или 'exit' для выхода): ")
                client_socket.sendto(message.encode('utf-8'), server_address)
                if message.lower() == 'exit':
                    print("Выход из чата...")
                    break
        except KeyboardInterrupt:
            print("\nПринудительное завершение работы.")
        finally:
            print("Клиент завершил работу.")

if __name__ == "__main__":
    start_udp_chat_client()
