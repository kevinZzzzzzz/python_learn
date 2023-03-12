"""
python数据(list或者dict)和JSON数据的相互转化
python -> JSON
    json.dumps(data,[ensure_ascii])  JSON字符串  ensure_ascii表示是否使用ascii码
JSON -> python
    json.loads(data)
"""
import json
data = [{"name": "老王", "age": 16}, {"name": "张三", "age": 18}]

# python -> JSON  转换为JSON字符串
json_str = json.dumps(data, ensure_ascii=False)
print(json_str, type(json_str))  # <class 'str'>
# JSON -> python
json_py = json.loads(json_str)
print(json_py, type(json_py))  # <class 'list'>
