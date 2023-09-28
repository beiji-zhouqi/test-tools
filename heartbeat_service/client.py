import socket

def start_client(server_host, server_port):
    # 创建套接字并连接到服务器
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    
    while True:
        # 向服务器发送消息
        message = input('请输入消息：')
        client_socket.send(message.encode())
        
        # 接收服务器响应
        response = client_socket.recv(1024).decode()
        print(f'收到服务器响应: {response}')
        
    # 关闭客户端套接字
    client_socket.close()

# 示例调用
server_host = '127.0.0.1'  # 替换为实际的服务器IP地址
server_port = 12345  # 替换为实际的服务器端口号

start_client(server_host, server_port)
