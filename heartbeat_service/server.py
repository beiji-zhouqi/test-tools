import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            # 接收客户端消息
            data = client_socket.recv(1024).decode()
            if not data:
                break
            
            print(f'收到客户端消息: {data}')
            
            # 向客户端发送消息
            response = '服务端收到消息：' + data
            client_socket.send(response.encode())
        except ConnectionResetError:
            break
    
    # 关闭客户端套接字
    client_socket.close()

def start_server(host, port):
    # 创建套接字并绑定到指定地址
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    
    print('服务器已启动，等待客户端连接...')
    
    while True:
        # 接受客户端连接
        client_socket, client_address = server_socket.accept()
        print(f'客户端已连接：{client_address}')
        
        # 创建线程处理客户端
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

# 示例调用
server_host = '0.0.0.0'  # 替换为实际的服务器IP地址
server_port = 12345  # 替换为实际的服务器端口号

start_server(server_host, server_port)
