import chardet
import re
import sys


# https://openpyxl.readthedocs.io/en/default/
from openpyxl import Workbook


def make_xlsx_v2(src_list):
    wb = Workbook()
    # grab the active worksheet
    ws = wb.active
    ws.append(['id','num1','num2','num3','data'])
    myid = 0
    
    for filename in src_list:
        print (filename)
        with open(filename) as f:
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
                # print(myid,num1,num2,num3,content)
                print(myid)
                
                ws.append([myid,num1,num2,num3,content])
    wb.save("xlsx_all.xlsx")




def make_xlsx(src_list):
    for filename in src_list:
        print (filename)
        make_xlsx_core(filename)



def make_xlsx_core(filename):
    wb = Workbook()
    # grab the active worksheet
    ws = wb.active
    ws.append(['id','num1','num2','num3','content'])
    myid = 0
    
    with open(filename) as f:
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
    wb.save("xlsx_"+filename.split('.')[0]+".xlsx")

file_list=['txt_src05.txt','txt_src08.txt','txt_src13.txt','txt_src19.txt']
# make_xlsx(file_list)
make_xlsx_v2(file_list)

