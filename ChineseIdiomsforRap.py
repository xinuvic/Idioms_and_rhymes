# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 15:47:09 2019

@author: xin

steps：
1. find all 成语 from URL 'http://chengyu.t086.com/'
file_o record_only_cy.txt 只记录成语
file record.txt 记录成语及对应拼音
file_del record_del.txt 只记录成语及韵母（去除声母）
2. find 成语 with the same 韵母
record_colle.txt 记录同韵母的成语，从第一行起循环遍历，将相同韵母的成语记录在同一行，方便去除重复项
record_colle_del_copy.txt 遍历，去除字符串重复的行
"""

f=open("record_del.txt",'r',encoding='utf-8')
f_o = open("record_only_cy.txt",'r',encoding='utf-8')
file_colle = open("record_colle.txt",'w',encoding='utf-8')


lines = f.readlines()
lines2 = f_o.readlines()
nums = len(lines)


for chengyu_chosen in lines2:
    for i in range(nums):
        if chengyu_chosen.replace('\n','') in lines[i]:
            yunjiao =  lines[i].replace(chengyu_chosen.replace('\n',''),'')
            index_chosen = i
    for u in range(nums):
        if yunjiao in lines[u]:
            file_colle.write(lines2[u].replace('\n','\t'))
    file_colle.write('\n')


    
f_o.close()
f.close()
file_colle.close()


'''
delete duplicates
'''
output=[]
with open('record_colle.txt',encoding='utf-8') as fp:
    lines=fp.readlines()
    for i in lines:
        if i not in output and '，' not in i and len(i)>10:
            output.append(i)
with open('record_colle_del_copy.txt','w',encoding='utf-8') as fp1:
    for i in output:
        fp1.write(i)






f1=open("record_del.txt",'r',encoding='utf-8')
f2=open("record_del_wide.txt",'w',encoding='utf-8')

line_c=f1.readlines()

for i in line_c:
    f2.write(i.replace(' ','          '))
f1.close()
f2.close()

f3=open("record_del_wide.txt",'r',encoding='utf-8')
f4=open("record_del_one.txt",'w',encoding='utf-8')
f5=open("record_del_two.txt",'w',encoding='utf-8')
f6=open("record_del_three.txt",'w',encoding='utf-8')
f_o = open("record_only_cy.txt",'r',encoding='utf-8')

line_o=f_o.readlines()
line3=f3.readlines()
nums=len(line3)
for i in range(nums):
    f4.write(line_o[i].replace('\n','')+''+line3[i][-5:])
    f5.write(line_o[i].replace('\n','')+''+line3[i][-19:])
    f6.write(line_o[i].replace('\n','')+''+line3[i][-35:])
f3.close()
f4.close()
f5.close()
f6.close()



'''
#print('******************one********************************')
'''
f7=open("record_del_one.txt",'r',encoding='utf-8')
f8 = open("record_only_cy.txt",'r',encoding='utf-8')
f9 = open("record_colle_one.txt",'w',encoding='utf-8')


lines_one = f7.readlines()
lines2 = f8.readlines()
for chengyu_chosen in lines2:
    for i in range(nums):
        if chengyu_chosen.replace('\n','') in lines_one[i]:
            yunjiao_one =  lines_one[i].replace(chengyu_chosen.replace('\n',''),'')
            index_chosen = i
    for u in range(nums):
        if yunjiao_one in lines_one[u]:
            f9.write(lines2[u].replace('\n','\t'))
    f9.write('\n')


    
f7.close()
f8.close()
f9.close()

'''
delete duplicates
'''
output=[]
with open('record_colle_one.txt',encoding='utf-8') as fp:
    lines=fp.readlines()
    for i in lines:
        if i not in output and '，' not in i and len(i)>10:
            output.append(i)
with open('record_colle_one_del_copy.txt','w',encoding='utf-8') as fp1:
    for i in output:
        fp1.write(i)


        
'''
#print('******************two********************************')
'''
f10=open("record_del_two.txt",'r',encoding='utf-8')
f11 = open("record_only_cy.txt",'r',encoding='utf-8')
f12 = open("record_colle_two.txt",'w',encoding='utf-8')


lines_one = f10.readlines()
lines2 = f11.readlines()
#循环行数
for chengyu_chosen in lines2:
    #print('\n')
    for i in range(nums):
        if chengyu_chosen.replace('\n','') in lines_one[i]:
            yunjiao_one =  lines_one[i].replace(chengyu_chosen.replace('\n',''),'')
            index_chosen = i
    for u in range(nums):
        if yunjiao_one in lines_one[u]:
            #print(lines2[u])
            f12.write(lines2[u].replace('\n','\t'))
    f12.write('\n')


    
f10.close()
f11.close()
f12.close()

'''
delete duplicates
'''
output=[]
with open('record_colle_two.txt',encoding='utf-8') as fp:
    lines=fp.readlines()
    for i in lines:
        if i not in output and '，' not in i and len(i)>10:
            output.append(i)
with open('record_colle_two_del_copy.txt','w',encoding='utf-8') as fp1:
    for i in output:
        fp1.write(i)



'''
#print('******************three********************************')
'''
f13=open("record_del_three.txt",'r',encoding='utf-8')
f14 = open("record_only_cy.txt",'r',encoding='utf-8')
f15 = open("record_colle_three.txt",'w',encoding='utf-8')


lines_one = f13.readlines()
lines2 = f14.readlines()
#循环行数
for chengyu_chosen in lines2:
    #print('\n')
    for i in range(nums):
        if chengyu_chosen.replace('\n','') in lines_one[i]:
            yunjiao_one =  lines_one[i].replace(chengyu_chosen.replace('\n',''),'')
            index_chosen = i
    for u in range(nums):
        if yunjiao_one in lines_one[u]:
            #print(lines2[u])
            f15.write(lines2[u].replace('\n','\t'))
    f15.write('\n')


    
f13.close()
f14.close()
f15.close()

'''
delete duplicates
'''
output=[]
with open('record_colle_three.txt',encoding='utf-8') as fp:
    lines=fp.readlines()
    for i in lines:
        if i not in output and '，' not in i and len(i)>10:
            output.append(i)
with open('record_colle_three_del_copy.txt','w',encoding='utf-8') as fp1:
    for i in output:
        fp1.write(i)
        
