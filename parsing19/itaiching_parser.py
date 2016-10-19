import chardet
import re
import sys



# print (f)
# http://stackoverflow.com/questions/24522394/regex-to-match-chinesenumber-pattern-in-python
# stackoverflow.com/questions/38449902/how-to-remove-english-alphabets-from-list-in-python?s=1|2.2007


def itaiching_parser( form_num,src_file):
    
    list1=[]
    set9=set()
    set10=set()
    out1=""
    linenum=0
    linenum2=0
    
    num1=form_num
    num2=0
    num2text=""
    num3=0
    
    out1=""
    out2=""
    out3=set()
    out4=set()
    
    
    with open(src_file) as f:
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
               
                # 例如 13-07-00，十九式第三式的招式名稱，
                # 設定第二節數字
                num2=temp[0]
                
                # 
                num2=int(num2)
                
                # 第三節數字歸零
                num3 = 0
                
                # 取中文部份
                for x in re.findall('[\u4e00-\u9fff]+',temp[1]):
                    num2text=x   
                    # 開發時快速查看
                    # print(x)
                    for y in x:
                        out4.add(y)
                
                
                
                # zfill, https://docs.python.org/3/tutorial/inputoutput.html
                # temp1 = (str(num1)+"-"+str(num2).zfill(2)+"-"+str(num3).zfill(2)+" === "+num2text+" ===")
                temp1 = (str(num1).zfill(2)+"-"+str(num2).zfill(2)+"-"+str(num3).zfill(2)+" 〓〓〓　"+num2text+"　〓〓〓")
                out1 +="\n"+ temp1 +"\n"
                # 　〓〓〓
                # temp2 = (str(num1)+"-"+str(num2).zfill(2)+"=== "+num2text+" ===")
                # temp2 = (str(num1)+"--"+str(num2).zfill(2)+"\n〓〓〓　"+num2text+"　〓〓〓")
                # out2 +="\n"+ temp2 +"\n"
                # print(temp)
            
    # http://www.runoob.com/python/python-reg-expressions.html
            # 如果不是招式名稱
            else:
                
                m=re.match('[\u4e00-\u9fff]+', perline) 
                
                # 只要是有中文，取整行
                # 因為中文標點不包括在內
                if m:
                    
                    for x in re.findall('[\u4e00-\u9fff]+',perline):
                        out3.add(x)   
                        for y in x:
                            out4.add(y)
                    
                    # 這是招式裡的第幾動
                    # num3 += 1
                    # fix 13-00-01 to be 13-00-00
                    if (num2 > 0):
                        num3 += 1
                    
                    # 做格式
                    temp1 = (str(num1).zfill(2)+"-"+str(num2).zfill(2)+"-"+str(num3).zfill(2)+" "+perline)
                    out1 += temp1 +"\n"
                    
                    # temp2 = (str(num3).zfill(2)+" "+perline)
                    # out2 += temp2 +"\n"
                
    # print (out2) 
    

    def write_content_to_file( content, file ):
        with open(file, 'w') as f:
            f.write( content )
            f.close()
            print ("now, please check filename: ", f.name)
    
    
    # print()
    write_content_to_file(out1,"txt_"+src_file)
    
    
itaiching_parser( 5,'src05.txt')
itaiching_parser( 8,'src08.txt')
itaiching_parser( 13,'src13.txt')
itaiching_parser( 19,'src19.txt')

    