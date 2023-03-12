"""
文件处理相关的功能模块
"""
def print_file_info(file_name):
    """
    功能是将给定的文件内容输出到控制台中
    :param file_name: 文件名或者文件路径
    :return: None
    """
    f = None
    try:
        f = open(file_name, 'r', encoding="UTF-8")
        content = f.read()
        print("文件全部内容如下：")
        print(content)
    except Exception as e:
        print(f'程序出现异常， 原因是：{e}')
    finally:
        if f:
            f.close()

def append_to_file(file_name, data):
    """
    功能是将字符串追加写入到文件中
    :param file_name:
    :param data:
    :return:
    """
    f = None
    try:
        f = open(file_name, 'a', encoding="UTF-8")
        f.write(data)
        print('写入完成')
    except Exception as e:
        print(f'程序出现异常，原因是：{e}')
    finally:
        if f:
            f.close()

if __name__ == '__main__':
    print_file_info('bill.txt')
    append_to_file('python.txt', 'hahahaha')
    print_file_info('python.txt')
