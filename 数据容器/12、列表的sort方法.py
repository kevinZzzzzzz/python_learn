my_list = [['a', 33], ['b', 55], ['c', 11]]
def choose_sort_key(ele):
    return ele[1]
"""
sort 
第一个参数是一个函数，指代sort排序的依据
reverse:表示是否倒序
"""
# my_list.sort(key=choose_sort_key, reverse=True)
# print(my_list)

# lambda 匿名函数
my_list.sort(key=lambda ele: ele[1], reverse=True)
print(my_list)