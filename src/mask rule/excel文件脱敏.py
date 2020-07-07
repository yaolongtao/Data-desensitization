import pandas as pd
import xlrd


def TestExcel():
    # filename = pd.read_csv('15体测demo.csv')
    # names = filename['姓名']
    # names.to_excel('names.xlsx')
    # names_df = names.to_frame()
    # names_df.to_excel('names1.xlsx')
    # filename.to_excel('15体测demo.xlsx', sheet_name='All_data', index=False)

    data = xlrd.open_workbook('E:\数据文件\Python-code\Data-desensitization\src\mask algorithm\DP\data\\2014年学生体质测试结果.xls')
    sheet1 = data.sheet_by_name('统计信息')
    sheet2 = data.sheet_by_name('学生测试结果清单')
    sheet3 = data.sheet_by_name('班级信息')
    print(sheet1.row_values(0))
    print(sheet1.col_values(0))
    print('行数', '=', sheet2.nrows)
    print('列数', '=', sheet2.ncols)
    print(data.sheet_names())


def ExcleMask():
    filename = '15体测demo.xlsx'
    file_obj = pd.read_excel(filename)  # 读取数据
    # names = file_obj.iloc[:, 1]  # 获取姓名列数据
    names = file_obj['姓名']  # 获取姓名列数据
    masked_name = []  # 新建列表，用于存放脱敏过的姓名
    for name in names:
        maskname = name[0]
        for i in range(len(name) - 1):
            maskname = maskname + '*'
        masked_name.append(maskname)
    file_obj.iloc[:, 1] = masked_name
    file_obj.to_excel('masked_name.xlsx', index=False)


ExcleMask()
