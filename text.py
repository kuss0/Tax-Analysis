import numpy as np
import pandas as pd
import openpyxl
pd.set_option('display.float_format', lambda x: '%.2f' % x) # 禁用科学计数法
df=pd.read_excel(r'C:\Users\kuss0\OneDrive\桌面/demo.xlsx', sheet_name='Sheet1', header=0)# 按照表名读取
df['税款所属期起']=pd.DataFrame(df['税款所属期起'].str[:7])#对特定列,提取前6个字符
df2=df.groupby(['纳税人名称','征收项目','税款种类','税款属性','税款所属期起'])[['计税依据','实缴金额']].agg('sum').reset_index()#通过reset_index()函数可以将groupby()的分组结果转换成DataFrame对象
print(df2)
df2.to_excel(r'C:\Users\kuss0\OneDrive\桌面\导出台账.xlsx', 'Sheet1', index=None)#存储到Excel中
