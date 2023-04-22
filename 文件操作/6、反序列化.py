fp = open('text.txt', 'r')
import json
cont = fp.read()
print(cont, type(cont))
context = json.loads(cont)
print(context)
print(type(context))


fp = open('text.txt', 'r')
import json
context = json.load(fp)
print(context)
print(type(context))