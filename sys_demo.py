# sys模块示例

import sys

# 实现从程序外部向程序传递参数，返回元组，第一个是程序名
print(sys.argv)

# 返回python版本号
print(sys.version)

# `sys.modules`是一个全局字典，该字典是python启动后就加载在内存中
print(sys.modules)

# 获取系统当前编码，一般默认为ascii。
print(sys.getdefaultencoding())

# 设置系统默认编码 windows下报错
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')
print(sys.getdefaultencoding())

# 获取文件系统使用编码方式
print(sys.getfilesystemencoding())

# 获取指定模块搜索路径的字符串集合
print(sys.path)

# 获取当前系统平台。
print(sys.platform)

# 标准输出  类似于print
sys.stdout.write('demo')

# 程序退出，arg=0为正常退出
sys.exit(-2)
