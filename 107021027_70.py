# -*- coding: utf-8 -*-
import re
import os
import matplotlib.pyplot as plt
import numpy as np

def cntword(target,openfile_name):
    i=0
    f=open(openfile_name,'r',encoding ='big5')
    f_read=f.read()
    f_all=f_read.strip('\n')
    #print(f_all)
    lines=re.sub(target,'@\n',f_all)
    #print(lines)
    for line in lines:
        #print(line)
        if '@' in line:
            i=i+1
    f.close()
    return(i)

'=============================================================================='

Dir_fileNovel='C:/Users/chiu yu-en/Desktop/程式碼/ChineseArticles_WordCnt_InDirectory/Novels_Content'
InputFileLocation = [Dir_fileNovel+"/07_倚天屠龍記.txt"]
InputFileLocation .append( Dir_fileNovel+"/17_倚天屠龍記.txt")
InputFileLocation .append( Dir_fileNovel+"/27_倚天屠龍記.txt")


Target={}
fp_name='C:/Users/chiu yu-en/Desktop/程式碼/ChineseArticles_WordCnt_InDirectory/name.txt'
f_name=open(fp_name,'r')
for name in f_name:
    name=name.strip('\n')
    Target[name]=0

f_name.close()
#f=open(InputFileLocation,'r',encoding ='UTF-8')
for InputFile in InputFileLocation:
    #print(InputFile)

    InputFileName =InputFile[-12:-4]
    TargetList = Target.items()
    
    char=list()
    num=list()

    for OneTaget, OneCnt in TargetList :
        OneCnt = cntword(OneTaget,InputFile)
        Target[OneTaget] = OneCnt
        char.append(OneTaget)
        num.append(OneCnt)

    Dir_Content =Dir_fileNovel+"/Novels_Content_Statistics"

    if not os.path.exists(Dir_Content):
        os.mkdir(Dir_Content)
    else:
        print(Dir_Content+"已經存在")

    OutputLocation = Dir_Content+"/倚天屠龍記_Statistics.txt"

    if not os.path.exists(OutputLocation):
        fw=open(OutputLocation,'w')

        fw.write("章"+"\t")
        for OneTaget, OneCnt in  TargetList:
            fw.write(OneTaget+"\t")
            print (OneTaget+"\t",end="")
        fw.write("\n")
        print ("\n")    
    else:

        fw=open(OutputLocation,'a')
        
        fw.write(InputFileName+"\t")
        
        for OneTaget, OneCnt in  TargetList:
            fw.write(str(OneCnt)+"\t")
            print (str(OneCnt)+"\t",end="") 
        fw.write("\n")    
    fw.close()
    ind=np.arange(len(char))
    plt.bar(ind,num)
    plt.xticks(ind+0.5,char)
    plt.title(InputFileName)
    plt.show()
