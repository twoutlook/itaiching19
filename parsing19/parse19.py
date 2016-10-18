import chardet
import re
import sys



# print (f)
# http://stackoverflow.com/questions/24522394/regex-to-match-chinesenumber-pattern-in-python
# stackoverflow.com/questions/38449902/how-to-remove-english-alphabets-from-list-in-python?s=1|2.2007
list1=[]
set9=set()
set10=set()
out1=""
linenum=0
linenum2=0

num1=19
num2=0
num2text=""
num3=0

out1=""
out2=""



with open('source19.txt') as f:
    content = f.readlines()
    
    # 一行一行讀
    for perline in content:
    
        # 記住行號，開發時先小範圍測試
        linenum +=1
        if (linenum >999):
            sys.exit()
        
        # 略過空白行
        if (len(perline)==0):
            continue
        
        # 去掉前置空格
        perline=perline.strip()
        
        # 先確認招式開始的位置
        # 1. 起势 Beginning form
        # 2.金刚捣碓Jin Gang Dao Dui
        m=re.match('\d+\.', perline)
        if m:
            
            # 以.分割字串
            temp=perline.split(".")
           
            # 例如 19-07-00，十九式第三式的招式名稱，
            # 設定第二節數字
            num2=temp[0]
            # 第三節數字歸零
            num3 = 0
            
            # 取中文部份
            for x in re.findall('[\u4e00-\u9fff]+',temp[1]):
                num2text=x   
                # 開發時快速查看
                # print(x)
            
            # zfill, https://docs.python.org/3/tutorial/inputoutput.html
            # temp1 = (str(num1)+"-"+str(num2).zfill(2)+"-"+str(num3).zfill(2)+" === "+num2text+" ===")
            temp1 = (str(num1)+"-"+str(num2).zfill(2)+"-"+str(num3).zfill(2)+" 〓〓〓　"+num2text+"　〓〓〓")
            out1 +="\n"+ temp1 +"\n"
            # 　〓〓〓
            # temp2 = (str(num1)+"-"+str(num2).zfill(2)+"=== "+num2text+" ===")
            temp2 = (str(num1)+"--"+str(num2).zfill(2)+"\n〓〓〓　"+num2text+"　〓〓〓")
            out2 +="\n"+ temp2 +"\n"
            # print(temp)
        
# http://www.runoob.com/python/python-reg-expressions.html
        # 如果不是招式名稱
        else:
            
            m=re.match('[\u4e00-\u9fff]+', perline) 
            
            # 只要是有中文，取整行
            # 因為中文標點不包括在內
            if m:
                # 這是招式裡的第幾動
                num3 += 1
                
                # 做格式
                temp1 = (str(num1)+"-"+str(num2).zfill(2)+"-"+str(num3).zfill(2)+" "+perline)
                out1 += temp1 +"\n"
                
                temp2 = (str(num3).zfill(2)+" "+perline)
                out2 += temp2 +"\n"
            
print (out2) 


    
# with open('result19a.txt', 'w') as f1:
#     f1.write( out1 )
#     f1.close()
# print ("now, please check filename: ", f1.name)


# with open('result19b.txt', 'w') as f2:
#     f2.write( out2 )
#     f2.close()
# print ("now, please check filename: ", f2.name)


# with open('result19b.txt', 'w') as f2:
#     f2.write( out2 )
#     f2.close()
# print ("now, please check filename: ", f2.name)



def write_content_to_file( content, file ):
    with open(file, 'w') as f:
        f.write( content )
        f.close()
        print ("now, please check filename: ", f.name)

write_content_to_file(out1,'result19a1.txt')
write_content_to_file(out2,'result19b1.txt')

