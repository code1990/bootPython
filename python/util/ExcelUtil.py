import xlrd

"""
excel工具类
"""

"""
给定路径
给定列数 
读取给定数量的excel数据 默认去除第一行的表头
"""
def get_list(file_path, col_nums):
    result_list = []
    book = xlrd.open_workbook(file_path)
    sheet = book.sheet_by_index(0)
    for row in range(1, sheet.nrows):
        url_info = ""
        for index in range(col_nums):
            url_info += str(sheet.cell_value(row, index).strip()) + "\t"
        result_list.append(url_info)
    return result_list
