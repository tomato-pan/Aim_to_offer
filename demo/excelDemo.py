import os
import pandas as pd
import openpyxl

file_path = r"D:\网络编程学习笔记\接口测试用例模板-01.xlsx"

df = pd.read_excel(file_path,sheet_name="参数约定")
print(df)
print(df.index)
print(df.columns)