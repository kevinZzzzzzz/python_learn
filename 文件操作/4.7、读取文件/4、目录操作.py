import os
import shutil

# os.mkdir(path): 创建'单级'目录（如果目录已经存在会抛出异常）
# os.mkdir('dome/a/b')

# os.makedirs(path): 创建多级目录（如果路径所有目录都存在了，则会抛出异常）
# os.makedirs('dome/aa/bb/cc')
# with open('dome/aa/bb/cc/c.txt', 'wt+') as file:
#     file.write('hello')

# os.rmdir(path): 删除空目录，如果目录不存在，或目录非空，都会抛出异常
# os.rmdir('dome/aa')

# os.removedirs(path): 递归删除空目录，在成功删除末尾一级后，会向上尝试把父级目录也删除（直到父级目录不是空目录）
# os.removedirs('dome/aa/bb/ee')

# os.path.exists(path): 判断路径是否存在（文件/目录都算）
# result = os.path.exists('dome/aa/bb')
# print(result)


# os.path.isdir(path): 用于判断路径是否目录，具体规则如下：
# 1、路径不存在，返回False
# 2、路径存在，但指向的是文件 返回False
# 3、路径存在，并且是目录，返回True
# result = os.path.isdir('dome/aa/bb')
# print(result)
# result2 = os.path.isdir('dome/aa/bb/cdsc')
# print(result2)
# result3 = os.path.isdir('dome/aa/bb/cc/c.txt')
# print(result3)


# os.path.isfile(path): 用于判断是文件，具体规则如下：
# result4 = os.path.isfile('dome/aa/bb/cc/c.txt')
# print(result4)

# os.scandir(path): 扫描指定目录
# result5 = os.scandir('dome/aa')
# print(result5)
# for item in result5:
#     print(item, item.is_dir())

# os.walk(path): 按层级，递归遍历指定目录下，所有目录和文件
# result6 = os.walk('dome')
# print(result6)
# for item in result6:
#     print(item)


# 删除有内容的目录
shutil.rmtree('dome/a')
