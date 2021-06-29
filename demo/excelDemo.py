import os
import pandas as pd
import openpyxl

file_path = r"D:\接口自动化.xlsx"
sheet_name = ["接口信息","接口字段","正常用例数据","异常用例数据"]
df = pd.read_excel(file_path,sheet_name="接口信息",header=None)
df1 = pd.read_excel(file_path,sheet_name="接口字段")
# 取一行数据
# print(df.loc[[0]])
api_info = {}
for i,j in zip(df[0],df[1]):
    # print(i,j)
    api_info[i]=j
print(api_info)
data_info = {api_info["url"]:{}}
for i1,i2,i3,i4,i5 in zip(df1["字段名称"],df1["字段类型"],df1["默认值"],df1["是否必填"],df1["自动构造异常用例映射"]):
    # print(i1,i2,i3,i4,type(i5))
    data_info[api_info["url"]][i1]={"type":i2,"default":i3,"must":i4,"error":i5}
print(data_info)

