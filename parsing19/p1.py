import chardet
import re

# from pprint import pprint
# f=open('19-04.txt')
# UnicodeDecodeError: 'gbk' codec can't decode byte
# f=open('19forms.txt')
     # http://stackoverflow.com/questions/2718196/find-all-chinese-text-in-a-string-using-python-and-regex
        # for n in re.findall(ur'[\u4e00-\u9fff]+',perline):
  
sample = u'I am from 美国。We should be friends. 朋友。'
for n in re.findall('[\u4e00-\u9fff]+',sample):
    print (n)
f=open('f2.txt').read()

# print (f)

# with open('f2.txt') as f:
#     content = f.readlines()
#     for perline in content:
#         # print(perline)
#         for n in re.findall('[\u4e00-\u9fff]+',perline):
#             print (n)
        
         #     print n