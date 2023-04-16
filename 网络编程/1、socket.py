import socket
# 创建socket对象
socket_server = socket.socket()
# 绑定IP地址和端口
socket_server.bind(('localhost', 8888))
# 监听端口
# listen方法接收一个整数参数，表示接收的连接数量， 超过则等待排队
socket_server.listen()
# 等待客户端连接
# result: tuple = socket_server.accept()
# conn = result[0]  # 客户端和服务端的连接对象
# address = result[1]  # 客户端的地址信息
conn, address = socket_server.accept()  # 如果没有客户端连接，就会阻塞在这里
print(f'接收到了客户端的信息，客户端的信息是，{address}')
# 接收客户端信息, 要使用客户端和服务端的本次连接对象，而非socket_server对象
# recv接收的参数是缓冲区的大小，一般是1024即可。recv放啊的返回值是一个字节数组，也就是bytes对象，不是字符串，可以通过decode方法采用UTF-8编码，将字节数组转换成字符串对象
while True:
    data: str = conn.recv(1024).decode('UTF-8')  # 将字节数组转换成字符串对象
    print(f"客户端发来的数据， {data}")
    # 发送回复消息
    msg: str = input("请输入你要发送的消息：").encode('UTF-8')  # 将字符串对象转换成字节数组
    if msg == 'exit':
        break
    conn.send(msg)
# 关闭连接
conn.close()
socket_server.close()

