"""
列表的遍历  while遍历
"""
myList = ['asdasd', 'asdwqe', 'qweqe', 'qwqwewq', 'qwrqrqw']
def list_while():
    index = 0
    while index < len(myList):
        ele = myList[index]
        print(f"{ele}---{index}")
        index += 1
    return None

def list_for():
    for i in myList:
        print(i, myList.index(i))
    return None

# list_while()
list_for()
