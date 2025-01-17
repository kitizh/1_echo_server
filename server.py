import socket

def start_server(host='0.0.0.0', port=8080):
    print("Запуск сервера...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        print(f"Сервер привязан к {host}:{port}")
        server_socket.listen(1)
        print("Сервер слушает порт...")

        while True:
            print("Ожидание подключения клиента...")
            client_socket, client_address = server_socket.accept()
            print(f"Клиент подключился: {client_address}")

            with client_socket:
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        print(f"Клиент отключился: {client_address}")
                        break
                    print(f"Получено от клиента: {data.decode('utf-8')}")
                    client_socket.sendall(data)
                    print(f"Отправлено клиенту: {data.decode('utf-8')}")

if __name__ == "__main__":
    try:
        start_server()
    except KeyboardInterrupt:
        print("\nСервер остановлен.")
