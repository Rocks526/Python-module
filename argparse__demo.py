import argparse

# 创建解析对象
parser = argparse.ArgumentParser()

# 添加参数  dest是解析后属性名字 required是是否必须 default是默认值 type是参数类型  help是提示信息
parser.add_argument('--db_name', '-n', dest='name', required=False, default='postgres', type=str, help='You want to connect DBName')
parser.add_argument('--db_password', '-p', dest='password', required=True, default='123456', type=str, help='You want to connect DB Password')

# 解析参数
args = parser.parse_args()

print(args)
print("用户名:{},密码:{}".format(args.name, args.password))
