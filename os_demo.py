# os模块示例

import os
import sys

# 判断目前正在使用的平台，并给出操作系统的名字
print(os.name)
print(sys.platform)

# 获取当前工作的目录
print(os.getcwd())

# 获取进程id
print(os.getpid())

# 列出path目录下所有的文件和目录名
print(os.listdir("."))

# 创建目录 默认目录存在会报错  exist_ok设置为True 不会报错
os.makedirs("./demo1/demo2/demo3", exist_ok=True)

# 创建文件
with open("./demo1/demo2/demo3/demo.txt", 'w+') as f:
    f.write("Hello World")

# 判断指定对象是否为文件
print(os.path.isfile("./demo1/demo2/demo3/demo.txt"))
print(os.path.isdir("./demo1"))

# 返回路径的目录和文件名，即将目录和文件名分开，而不是一个整体
print(os.path.split("./demo1/demo2/demo3/demo.txt"))

# 获得文件的大小，如果为目录，返回0
print(os.path.getsize("./demo1"))
print(os.path.getsize("./demo1/demo2/demo3/demo.txt"))

# 删除path指定的文件
print(os.remove("./demo1/demo2/demo3/demo.txt"))

# 删除目录
print(os.removedirs("./demo1/demo2/demo3"))

# 检验指定的对象是否存在
print(os.path.exists("./demo1"))

# 执行shell命令。返回值是脚本的退出状态码，0代表成功，1代表不成功
print(os.system("cd d:"))

# 改变目录到指定目录
print(os.getcwd())
print(os.chdir("../"))
print(os.getcwd())

# 连接目录和文件名
print(os.path.join("d:", "demo"))

# 终止当前进程
os._exit(-1)


