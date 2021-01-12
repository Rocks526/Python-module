import xlrd

# 打开excel
excel = xlrd.open_workbook('user_infos.xls')
# 获取sheet
sheet = excel.sheet_by_index(0)
# sheet = excel.sheet_by_name('user_info')
# 输出多少行 多少列
print('一共有{}行，{}列'.format(sheet.nrows, sheet.ncols))
# 获取某个位置的值
print('第二行第二列的值是{}'.format(sheet.cell(1, 1).value))
# 获取整行整列的值
print('第一行的所有值为：{}'.format(sheet.row_values(0)))
print('第一列的所有值为：{}'.format(sheet.col_values(0)))
# 输出所有值
for i in range(sheet.nrows):
    print(sheet.row_values(i))