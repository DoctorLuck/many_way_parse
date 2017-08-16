import json

#json.loads()   把json格式字符串解码转换成Python对象

#json.dumps()   实现python类型转化为json字符串，返回一个str对象 把一个Python对象编码转换成Json字符串

#json.dump()    将Python内置类型序列化为json对象后写入文件

listStr = [{"city": "北京"}, {"name": "大刘"}]
json.dump(listStr, open("listStr.json","w"), ensure_ascii=False)
