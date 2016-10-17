import chardet
import re

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

with open('f3.txt') as f:
    content = f.readlines()
    for perline in content:
        for x in re.findall('[\u4e00-\u9fff]+',perline):
            # print(x)
            list1.append(x)
            set9.add(x)  
            for one in x:
                set10.add(one)
            
            
# print (list1)    
        # for item in list1:
        #     print (len(item))
            # if (len(item))
            
        # print (list1) 
set1=set(list1)
# print (set1)
list2=list(set1)
list2.sort()
# for x in set1:
    # print (x)
print("//////////////////////")
print (set9)
print (len(set9))

print (set10)
print (len(set10))

# for x in list2:
#     print (x)
    