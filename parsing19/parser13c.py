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

num1=13
num2=0
num2text=""
num3=0

out1=""
out2=""
out3=set()
out4=set()


with open('source13.txt') as f:
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
                temp1 = (str(num1)+"-"+str(num2).zfill(2)+"-"+str(num3).zfill(2)+" "+perline)
                out1 += temp1 +"\n"
                
                temp2 = (str(num3).zfill(2)+" "+perline)
                out2 += temp2 +"\n"
            
print (out2) 


    
# with open('result13a.txt', 'w') as f1:
#     f1.write( out1 )
#     f1.close()
# print ("now, please check filename: ", f1.name)


# with open('result13b.txt', 'w') as f2:
#     f2.write( out2 )
#     f2.close()
# print ("now, please check filename: ", f2.name)


# with open('result13b.txt', 'w') as f2:
#     f2.write( out2 )
#     f2.close()
# print ("now, please check filename: ", f2.name)



def write_content_to_file( content, file ):
    with open(file, 'w') as f:
        f.write( content )
        f.close()
        print ("now, please check filename: ", f.name)



write_content_to_file(out1,'result13_1.txt')
write_content_to_file(out2,'result13_2.txt')
out3=list(out3)
out3.sort()
print(out3)
out3x=""
for x in out3:
    out3x+=x+"\n"
write_content_to_file(out3x,'result13_3.txt') 

out4=list(out4)
out4.sort()

out4x=""
for x in out4:
    out4x+=x
# write_content_to_file(out4x,'result13_4.txt')    
# print(out4x)

'''
一上下与两中为于云人以伸似体侧倒倾内再出击刁分划刚初到前力劲势勾卷双变口右合同后向含回圈在地处外大头女如实对封小尖左带平并开弧往微心慢懒手扎打托找抬抽拉拗拢拳指按挖挤捣掌探掤推掩提插搂搭摆撑撤支收放斜方旁旋时来松根梭横正步水沉沿点然玉用由盖直相砸碓移穿立站笔线绕继续翻耳肘肩肱胀背胯胸脚腔腕腰腹腿膝膨臂自至落行衣贴起跟跨踏蹚蹬身转轴部里重野金铲闭间随震青顶领马
一上下與兩中為於雲人以伸似體側倒傾內再出擊刁分劃剛初到前力勁勢勾卷雙變口右合同後向含迴圈在地處外大頭女如實對封小尖左帶平並開弧往微心慢懶手扎打托找抬抽拉拗攏拳指按挖擠搗掌探掤推掩提插摟搭擺撐撤支收放斜方旁旋時來松根梭橫正步水沉沿點然玉用由蓋直相砸碓移穿立站筆線繞繼續翻耳肘肩肱脹背胯胸腳腔腕腰腹腿膝膨臂自至落行衣貼起跟跨踏蹚蹬身轉軸部裡重野金鏟閉間隨震青頂領馬
一上下與兩中為於雲人以伸似體側倒傾內再出擊刁分劃剛初到前力勁勢勾卷雙變口右合同後向含迴圈在地處外大頭女如實對封小尖左帶平並開弧往微心慢懶手紥打托找抬抽拉拗攏拳指按挖擠搗掌探掤推掩提插摟搭擺撐撤支收放斜方旁旋時來鬆根梭橫正步水沉沿點然玉用由蓋直相砸碓移穿立站筆線繞繼續翻耳肘肩肱脹背胯胸腳腔腕腰腹腿膝膨臂自至落行衣貼起跟跨踏蹚蹬身轉軸部裡重野金鏟閉間隨震青頂領馬


松 -> 鬆
扎 -> 紥
'''

# s='一上下与两中为于云人以伸似体侧倒倾内再出击刁分划刚初到前力劲势勾卷双变口右合同后向含回圈在地处外大头女如实对封小尖左带平并开弧往微心慢懒手扎打托找抬抽拉拗拢拳指按挖挤捣掌探掤推掩提插搂搭摆撑撤支收放斜方旁旋时来松根梭横正步水沉沿点然玉用由盖直相砸碓移穿立站笔线绕继续翻耳肘肩肱胀背胯胸脚腔腕腰腹腿膝膨臂自至落行衣贴起跟跨踏蹚蹬身转轴部里重野金铲闭间随震青顶领马'
# t='一上下與兩中為於雲人以伸似體側倒傾內再出擊刁分劃剛初到前力勁勢勾卷雙變口右合同後向含迴圈在地處外大頭女如實對封小尖左帶平並開弧往微心慢懶手紥打托找抬抽拉拗攏拳指按挖擠搗掌探掤推掩提插摟搭擺撐撤支收放斜方旁旋時來鬆根梭橫正步水沉沿點然玉用由蓋直相砸碓移穿立站筆線繞繼續翻耳肘肩肱脹背胯胸腳腔腕腰腹腿膝膨臂自至落行衣貼起跟跨踏蹚蹬身轉軸部裡重野金鏟閉間隨震青頂領馬'

def translate_simplified_form13_to_traditional(simplified):
    s='一上下与两中为九于云人以伸似体侧倒倾内再出击刁分划刚初到前力劲势勾十卷双变口右合同后向含回圈在地处外大太头女如实对封小尖左带平并开式弧往微心慢懒手扎打托找抬抽拉拗拢拳指按挖挤捣掌探掤推掩提插搂搭摆撑撤支收放斜方旁旋时易来松极根梭横正步水沉沿点然玉用由盖直相砸碓移穿立站笔线绕继续翻耳肘肩肱胀背胯胸脚腔腕腰腹腿膝膨臂自至落行衣诀贴起跟跨踏蹚蹬身转轴部里重野金铲闭间随震青顶领马高鬃龙'
    t='一上下與兩中為九於雲人以伸似體側倒傾內再出擊刁分劃剛初到前力勁勢勾十卷雙變口右合同後向含迴圈在地處外大太頭女如實對封小尖左帶平並開式弧往微心慢懶手扎打托找抬抽拉拗攏拳指按挖擠搗掌探掤推掩提插摟搭擺撐撤支收放斜方旁旋時易來松極根梭橫正步水沉沿點然玉用由蓋直相砸碓移穿立站筆線繞繼續翻耳肘肩肱脹背胯胸腳腔腕腰腹腿膝膨臂自至落行衣訣貼起跟跨踏蹚蹬身轉軸部裡重野金鏟閉間隨震青頂領馬高鬃龍'


# intab = "aeiou"
# outtab = "12345"
# trantab = str.maketrans(intab, outtab)

# str = "this is string example....wow!!!"
# print (str.translate(trantab))
    trantab = str.maketrans(s, t)
# str = "铲出"
# print (str.translate(trantab))
    return simplified.translate(trantab)
    
# 划->划    
# 回->回 
# 松->鬆
# 扎->紥
s='一上下与两中为九于云人以伸似体侧倒倾内再出击刁分划刚初到前力劲势勾十卷双变口右合同后向含回圈在地处外大太头女如实对封小尖左带平并开式弧往微心慢懒手扎打托找抬抽拉拗拢拳指按挖挤捣掌探掤推掩提插搂搭摆撑撤支收放斜方旁旋时易来松极根梭横正步水沉沿点然玉用由盖直相砸碓移穿立站笔线绕继续翻耳肘肩肱胀背胯胸脚腔腕腰腹腿膝膨臂自至落行衣诀贴起跟跨踏蹚蹬身转轴部里重野金铲闭间随震青顶领马高鬃龙'
t='一上下與兩中為九於雲人以伸似體側倒傾內再出擊刁分划剛初到前力勁勢勾十卷雙變口右合同後向含回圈在地處外大太頭女如實對封小尖左帶平並開式弧往微心慢懶手紥打托找抬抽拉拗攏拳指按挖擠搗掌探掤推掩提插摟搭擺撐撤支收放斜方旁旋時易來鬆極根梭橫正步水沉沿點然玉用由蓋直相砸碓移穿立站筆線繞繼續翻耳肘肩肱脹背胯胸腳腔腕腰腹腿膝膨臂自至落行衣訣貼起跟跨踏蹚蹬身轉軸部裡重野金鏟閉間隨震青頂領馬高鬃龍'
trantab = str.maketrans(s, t)

out3x=""
for x in out3:
    out3x+= x+" "+ x.translate(trantab)+"\n"
    
write_content_to_file(out3x,'result13_3_traditional.txt') 

# https://www.uedsc.com/python3-string-translate.html

# https://openpyxl.readthedocs.io/en/default/


