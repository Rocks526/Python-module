import xlrd
from xlutils import copy

# xlrd读取一个excel
excel = xlrd.open_workbook('user_infos.xls')
# xlutils复制一份之前的excel
new_excel = copy.copy(excel)
# 获取sheet
sheet = new_excel.get_sheet(0)
# 修改数据
sheet.write(1, 1, 'Rocks')
# 保存
new_excel.save('new_user_infos.xls')