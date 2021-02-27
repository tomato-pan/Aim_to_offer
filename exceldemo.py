import os
import pandas as pd
import xlwt
import xlrd
import xlutils.copy


# 获取excel文件名
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print("success!")
    return files


# 读取excel文件内容
def read_excel_file(excel):
    table = pd.DataFrame(pd.read_excel(excel, sheet_name=0, header=[1]))
    name_list = []
    address_list = []
    resource_list = []
    name = table.columns[0]
    address = table.columns[1]
    resource = table.columns[3]
    for i in range(len(table)):
        if type(table.iloc[i][name]) != float:
            if "英语" in table.iloc[i][name] and "数字故事" not in table.iloc[i][name]:
                name_list.append(table.iloc[i][name])
                address_list.append(table.iloc[i][address])
                resource_list.append(table.iloc[i][resource])
    return name_list, address_list, resource_list


# 写excel文件
def write_excel_file():
    dir = r"E:\2020英语线上公开课.xls"
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("sheet1")
    title = ["课程名字", "电脑学习网址", "素材来源", "密码"]
    name_list = []
    address_list = []
    resource_list = []
    password = "202066"
    root = "E:\\刘思余\\2020春季线上学习区级视频\\"
    files = file_name(r"E:\刘思余\2020春季线上学习区级视频")
    for i in files:
        name_list1, address_list1, resource_list1 = read_excel_file(root + i)
        name_list+=name_list1
        address_list+=address_list1
        resource_list+=resource_list1
    print(len(name_list))
    for i in range(len(title)):
        sheet.write(0, i, title[i])
    for i in range(1, len(name_list)):
            print()
            print(i,name_list[i])
            sheet.write(i, 0, name_list[i])
            sheet.write(i, 1, address_list[i])
            sheet.write(i,  2, resource_list[i])
            sheet.write(i, 3, password)
    workbook.save(dir)


if __name__ == '__main__':
    write_excel_file()
