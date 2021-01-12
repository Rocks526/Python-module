import xlwt

# 创建Excel对象
excel = xlwt.Workbook()
# 添加页面
sheet = excel.add_sheet('user_info')
sheet.write(0, 0, '用户ID')
sheet.write(0, 1, '用户名')
sheet.write(0, 2, '用户密码')

users_info = [
    [1, 'Jack', '123456'],
    [2, 'Mary', '984264'],
    [3, 'Merry', '200481'],
    [4, 'Lucy', '89100']
]

# 添加用户数据
line = 1
for user in users_info:
    col = 0
    for field in user:
        sheet.write(line, col, field)
        col += 1
    line += 1

# 保存Excel
excel.save('user_infos.xls')