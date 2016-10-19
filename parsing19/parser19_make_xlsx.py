import chardet
import re
import sys


# https://openpyxl.readthedocs.io/en/default/
from openpyxl import Workbook

wb = Workbook()
# grab the active worksheet
ws = wb.active
ws.append(['id','num1','num2','num3','content'])
myid = 0

with open('result19_1.txt') as f:
    content = f.readlines()
    
    # print(content)
    # 一行一行讀
    for perline in content:
        if (len(perline.strip())==0):
            continue
        
        # print(perline)
        myid+=1
        num1=perline[0:2]
        num2=perline[3:5]
        num3=perline[6:8]
        content=perline[9:]
        print(myid,num1,num2,num3,content)
        ws.append([myid,num1,num2,num3,content])


# Rows can also be appended
# ws.append([1, 2, 3])

# Save the file
wb.save("result19.xlsx")


