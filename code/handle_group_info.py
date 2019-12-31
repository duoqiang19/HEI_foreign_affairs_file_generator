import xlrd
from xlutils.copy import copy  # 导入copy模块


class Handle_group_info():

    def __init__(self, address):
        self.address = address
        self.book = xlrd.open_workbook(self.address)
        self.sheet = self.book.sheet_by_name(self.book.sheet_names()[0])
        self.rows_no = self.sheet.nrows
        self.cols_no = self.sheet.ncols

    def write_group_info(self, group_info):
        temp_book = copy(self.book)  # 利用xlutils.copy下的copy函数复制
        temp_sheet = temp_book.get_sheet(0)
        for i in range(self.cols_no):
            if self.sheet.cell(2, i).value in group_info:
                temp_sheet.write(self.rows_no, i, group_info[self.sheet.cell(2, i).value])
        temp_book.save(self.address)  # 保存文件

    def read_group_info():
        return 1

    def get_group_hei_no(self):
        hei_no = int(self.sheet.cell(self.rows_no - 1, 14).value)
        he_no = int(self.sheet.cell(self.rows_no - 1, 21).value)
        group_no = int(self.sheet.cell(self.rows_no - 1, 0).value)
        return [hei_no, he_no, group_no]


if __name__ == '__main__':
    # import sys, os, re
    staff_info_address = r'D:\Nutstore\python_workspace\HEI_foreign_affairs_file_generator\database\group_info.xls'
    group_info_input = {'group_leader': '马云', 'destination': '美国', 'inviter': 'NASA'}
    a = Handle_group_info(staff_info_address)

    a.write_group_info(group_info_input)

'''
    def read_group_info(self):
        workbook = xlrd.open_workbook(workbook_address)
        sheet1_name = workbook.sheet_names()[0]
    # 根据sheet索引或者名称获取sheet内容
    #sheet1 = workbook.sheet_by_index(0)  # 根据sheet索引获取sheet内容
        sheet1 = workbook.sheet_by_name(sheet1_name)# 根据sheet名称获取sheet内容
    #print(sheet1.name,sheet1.nrows,sheet1.ncols)# sheet的名称，行数，列数

    # 获取整行和整列的值（数组）
        rows = sheet1.row_values(1) # 获取第四行内容
        cols = sheet1.col_values(1) # 获取第三列内容
        print(rows)
        print(cols)

    # 获取单元格内容
        print(sheet1.cell(1,1).value)
    #print sheet2.cell_value(1,0).encode('utf-8')
    #print sheet2.row(1)[0].value.encode('utf-8')

    # 获取单元格内容的数据类型
        print(sheet1.cell(1,1).ctype)
'''
