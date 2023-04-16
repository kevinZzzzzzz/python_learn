import socket
socket_client = socket.socket()
socket_client.connect(('localhost', 8888))
socket_client.send('你好呀'.encode('UTF-8'))
while True:
    recv_data: str = socket_client.recv(1024)
    print(f'服务端回复的消息是：{recv_data.decode("UTF-8")}')
    client_msg: str = input('你的回复是：')
    if client_msg == 'exit':
        break
    socket_client.send(client_msg.encode('UTF-8'))

socket_client.close()

