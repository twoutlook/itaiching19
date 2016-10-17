import chardet
import re
import sys

# from pprint import pprint
# f=open('19-04.txt')
# UnicodeDecodeError: 'gbk' codec can't decode byte
# f=open('19forms.txt')
     # http://stackoverflow.com/questions/2718196/find-all-chinese-text-in-a-string-using-python-and-regex
        # for n in re.findall(ur'[\u4e00-\u9fff]+',perline):
  
# set1 = set()                   # A new empty set
# set1.add("cat")                # Add a single member
# set1.update(["dog", "mouse"])  # Add several members
# if "cat" in set1:              # Membership test
#   set1.remove("cat")
# #set1.remove("elephant") - throws an error
# set1.discard("elephant")       # No error thrown
# print set1
# for item in set1:              # Iteration AKA for each element
#   print item
# print "Item count:", len(set1) # Length AKA size AKA item count
# isempty = len(set1) == 0       # Test for emptiness
# set1 = set(["cat", "dog"])     # Initialize set from a list
# set2 = set(["dog", "mouse"])
# set3 = set1 & set2             # Intersection
# set4 = set1 | set2             # Union
# set5 = set1 - set3             # Set difference
# set6 = set1 ^ set2             # Symmetric difference
# issubset = set1 <= set2        # Subset test
# issuperset = set1 >= set2      # Superset test
# set7 = set1.copy()             # A shallow copy
# set7.remove("cat")
# set8 = set1.copy()
# set8.clear()                   # Clear AKA empty AKA erase
# print set1, set2, set3, set4, set5, set6, set7, set8, issubset, issuperset  
  
  
# sample = u'I am from 美国。We should be friends. 朋友。'
# for n in re.findall('[\u4e00-\u9fff]+',sample):
#     print (n)
f=open('f2.txt').read()

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

with open('f3.txt') as f:
    content = f.readlines()
    for perline in content:
        # print(len(perline.strip()))
        perline2=perline.strip()
        if (len(perline2)==0):
            continue
        linenum +=1
        # print (linenum,perline2)
        # print(re.match('\d+', perline2))  
        
        if (linenum >7000):
            sys.exit()
        
        m=re.match('\d+', perline2)
        if m:
            num3 = 0
            #1. 起势 Beginning form
            # print (m.span())
            perline3=perline2.split(".")
            # print (perline3)
            # print (perline3[0])
            num2=perline3[0]
            for x in re.findall('[\u4e00-\u9fff]+',perline3[1]):
                num2text=x   
                # print(x)
            # list1.append(x)    
            # http://stackoverflow.com/questions/733454/best-way-to-format-integer-as-string-with-leading-zeros
            
            # temp = (str(num1)+"-"+str(num2).zfill(2)+"-"+str(num3).zfill(2)+" === "+num2text+" ===")
            temp = (str(num1)+"-"+str(num2).zfill(2)+" === "+num2text+" ===")
            out1 +="\n"+ temp +"\n"
            # print(temp)
        
# http://www.runoob.com/python/python-reg-expressions.html
        
        else:
            m=re.match('[\u4e00-\u9fff]+', perline2) 
            if m:
                num3 += 1
                # print(perline2)
                # temp = (str(num1)+"-"+str(num2).zfill(2)+"-"+str(num3).zfill(2)+" "+perline2)
                temp = (str(num3).zfill(2)+" "+perline2)
                out1 += temp +"\n"
            
                # print(temp)
        
            # for x in re.findall('[\u4e00-\u9fff]+',perline):
            #     # print(linenum,x)
            #     list1.append(x)
            
print (out1) 
# http://www.runoob.com/python/python-file-write.html
fo = open("result19.txt", "w")
fo.write( out1 )

# 关闭文件
fo.close()
print ("now, please check filename: ", fo.name)

    