import json

bool_word = True
int_word = 1
float_word = 8.99
str_word = "这是一个字符串!"
None_word = None
tuple_word = (12, "Hello", 88.9)
list_word = [12, "Hello", 88.9]
dict_word = {"key1": "value1", "key2": "测试数据"}
set_word = {12, "Hello", 88.9}
print(json.dumps(bool_word))
print(json.dumps(int_word))
print(type(json.dumps(float_word)))
print(json.dumps(str_word))
print(json.dumps(None_word))
print(type(json.dumps(tuple_word)))
print(type(json.dumps(list_word)))
print(json.dumps(dict_word))
print(json.dumps(set_word))


# 格式化输出
jsonStr = json.dumps(dict_word, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
print(jsonStr)


with open("save.txt", "a+") as f:
    json.dump(dict_word, f)
