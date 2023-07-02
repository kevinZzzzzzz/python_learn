from lxml import etree

# xpath解析
# (1)本地文件  etree.parse()
# (2)服务器响应的数据  response.read().decode('utf-8)   etree.HTML()

tree = etree.parse('xpath的基本使用.html')

# tree.解析('xpath的路径')
# 查找ul下面的li
'''
    1 路径查询
        //: 查找所以子孙节点，不考虑层级关系
        /: 找直接子节点
    2 谓词查询
        //div[@id]
        //div[@id='xxx']
    3 属性查询
        //@class
    4 模糊查询
        //div[contains(@id, 'xx')]
        //div[starts-with(@id, 'xx')]
    5 内容查询
        //div/h1/text()
    6 逻辑运算
        //div[@id='xxx' and @class='xxx']
        //title | //price
        
    谷歌快捷键
    command + shift + X
'''
# 查找所有li标签
li_list = tree.xpath('//body/ul/li')
print(li_list)
print(len(li_list))

# 查找所有有id的li标签
li_id_list = tree.xpath('//ul/li[@id]')
li_id_l1_list = tree.xpath('//ul/li[@id="l1"]')
print(li_id_list )
print(li_id_l1_list)
print(len(li_id_list))

# 查找到有id并且class为c1的标签
li_id_class_c1_list = tree.xpath('//ul/li[@id and @class="c1"]')
print(li_id_class_c1_list)

# 查询id中包含l的li标签
li_id_l_list = tree.xpath('//ul/li[contains(@id, "l")]/text()')  # ['北京', '上海']
print(li_id_l_list)

# 查询id的值以l开头的li标签
li_id_start_l_list = tree.xpath('//ul/li[starts-with(@id, "c")]/text()')  # ['深圳', '广州']
print(li_id_start_l_list)

# 获取两个条件的标签
li_list2 = tree.xpath('//ul/li[@id="l1"]/text() | //ul/li[@id="l2"]/text()')  # ['北京', '上海']
print(li_list2)
