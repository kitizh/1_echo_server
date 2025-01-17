import socket

def start_udp_chat_server(host='127.0.0.1', port=65432):
    print("Запуск UDP-чата-сервера...")
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))
        print(f"Сервер запущен на {host}:{port}")

        clients = set()

        while True:
            data, client_address = server_socket.recvfrom(1024)
            message = data.decode('utf-8').strip()
            print(f"Получено сообщение от {client_address}: {message}")

            if message.lower() == "exit":
                print(f"Клиент {client_address} отключился.")
                clients.discard(client_address)
            else:
                clients.add(client_address)
                for client in clients:
                    if client != client_address:
                        server_socket.sendto(data, client)

if __name__ == "__main__":
    try:
        start_udp_chat_server()
    except KeyboardInterrupt:
        print("\nСервер остановлен.")
