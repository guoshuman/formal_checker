#-*-coding:utf-8-*-
import re
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')
#定义的变量
fileName = [] #读取目录下的文件名
zifilePath = [] #读取目录下的文件路径
anno_path = []
# anno_count = 0
doc_path = []
# doc_count = 0
spe_path = []
# spe_count = 0
info = []
desc = []

adress = raw_input('Address:')
top_list = adress.split('\\')[-1]

pro_list = []
#adress = 'E:\\testcase\\haierkongtiao_rerecord_3m_6.26.0.7_20160824_2'
#top_list = 'haierkongtiao_rerecord_3m_6.26.0.7_20160824_2'


# 遍历指定目录，得到目录下的所有文件名和对应的路径
def eachFile(filepath,path,name):
    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
        path.append(os.path.join('%s%s%s' % (filepath, '\\',allDir)))
        name.append(os.path.join('%s'%(allDir)))
        # print zifilePath.decode('gbk') # .decode('gbk')是解决中文显示乱码问题
        # print fileName.decode('gbk')
    # return name,path

def getFilePath(filename,zifilepath):#得到每个文件夹对应的路径
    i = 0
    global anno_count
    global anno_path
    while i < len(filename):
        if filename[i] == 'annotation':
            anno_path.append(zifilepath[i])
           # anno_count +=1 
            i += 1
        elif filename[i] == 'doc':
            doc_path.append(zifilepath[i])
            #doc_count +=1 
            i += 1
        elif filename[i] == 'speech':
            spe_path.append(zifilepath[i])
            #spe_count +=1 
            i += 1 
        else :
            i += 1

def judgeTop(filename):#判断顶层目录是否符合要求
    global info
    global desc
    global pro_list
    i = 0
#    if len(anno_path) == len(doc_path) == len(spe_path) == 1:
    while i < len(filename):
        if '.info' in filename[i]:
            if top_list in filename[i]:
                info.append(filename[i])
                i += 1
            else:
                print u'顶层目录.info文件命名格式不符合规定'
                print u'不符合规定的info文件的名字：' + filename[i] + '\n'
                pro_list.append(u'顶层目录.info文件命名格式不符合规定'+'\n'+u'不符合规定的info文件的名字：' + filename[i])
                info.append(filename[i])
                i += 1
        elif '.desc' in filename[i]:
            if top_list in filename[i]:
                desc.append(filename[i])
                i += 1
            else:
                print u'顶层目录.desc文件命名格式不符合规定'
                print u'不符合规定的desc文件的名字：' + filename[i] + '\n'
                pro_list.append(u'顶层目录.desc文件命名格式不符合规定'+'\n'+u'不符合规定的desc文件的名字：' + filename[i]) 
                desc.append(filename[i])
                i += 1
        else:
            i += 1
   
    if len(info) != 1:
        print u'顶层文件中存在{}个info文件目录'.format(len(info))
        pro_list.append(u'顶层文件中存在{}个info文件目录'.format(len(info))) 
    if len(desc) != 1:
        print u'顶层文件中存在{}个desc文件目录'.format(len(desc))
        pro_list.append(u'顶层文件中存在{}个desc文件目录'.format(len(desc)))
#    else:

    if len(anno_path) != 1:
        print u'存在{}个anno文件目录'.format(len(anno_path))
        pro_list.append(u'存在{}个anno文件目录'.format(len(anno_path)))
    if len(doc_path) != 1:
        print u'存在{}个doc文件目录'.format(len(doc_path))
        pro_list.append(u'存在{}个doc文件目录'.format(len(doc_path)))
    if len(spe_path) != 1:
        print u'存在{}个spe文件目录'.format(len(spe_path))
        pro_list.append(u'存在{}个spe文件目录'.format(len(spe_path)))



def judgeAnno(annopath):#判断annotation目录下的文件是否符合
    global pro_list
    anno_zipath = []
    anno_ziname = []
    i = 0
    if len(annopath) == 1:
        eachFile(annopath[0],anno_zipath,anno_ziname)
        if len(anno_ziname) == 1:
            if '.txt' in anno_ziname[0]:
                if top_list in anno_ziname[0]:
                    pass
                else:
                    print u'annotation文件中的txt文件命名不符合规定'
                    print u'不符合规定的txt文件的名字：' + anno_ziname[0] + '\n'
                    pro_list.append(u'annotation文件中的txt文件命名不符合规定'+'\n'+u'不符合规定的txt文件的名字：' + anno_ziname[0])
        else:
            print u"annotation文件中存在{}个文件".format(len(anno_ziname))
            pro_list.append(u'annotation文件中存在{}个文件'.format(len(anno_ziname)))
            while i < len(anno_ziname):
                if '.txt' in anno_ziname[i]:
                    if top_list in anno_ziname[i]:
                        i += 1
                    else :
                        print u'annotation文件中第{}个txt文件命名不符合规定'.format(i)
                        print u'不符合规定的txt文件的名字：' + anno_ziname[i] + '\n'
                        pro_list.append(u'annotation文件中第{}个txt文件命名不符合规定'.format(i)+'\n'+u'不符合规定的txt文件的名字：' + anno_ziname[i])
                        i += 1
                else :
                    print u'annotation文件中的第{}个文件不是txt格式'.format(i)
                    print u'不符合规定的txt文件的名字：' + anno_ziname[i] + '\n'
                    pro_list.append(u'annotation文件中的第{}个文件不是txt格式'.format(i)+'\n'+u'不符合规定的txt文件的名字：' + anno_ziname[i])
                    i += 1


def judgeSpeech(speechpath):#判断speech目录下文件是否符合规定
    global pro_list
    spe_zipath = []
    spe_ziname = []
    i = 0
    if len(speechpath) == 1:
        eachFile(speechpath[0],spe_zipath,spe_ziname)
        if len(spe_ziname) == 0:
            print u'speech文件夹下没有文件'
            pro_list.append(u'speech文件夹下没有文件')
        else :
            while i < len(spe_ziname):
                if '.wav' in spe_ziname[i]:
                    i += 1
                else :
                    print u'speech文件中第{}个文件不是.wav文件'.format(i)
                    print u'不符合规定的文件的名字：' + spe_ziname[i] + '\n'
                    pro_list.append(u'speech文件中第{}个文件不是.wav文件'.format(i) + '\n' +u'不符合规定的文件的名字：' + spe_ziname[i])
                    i += 1


eachFile(adress,zifilePath,fileName)
getFilePath(fileName,zifilePath)
judgeTop(fileName)
judgeAnno(anno_path)
judgeSpeech(spe_path)

# def writeToTxt(list_name,file_path):
#     try:
#         fp = open(file_path,"w+")
#         for item in list_name:
#             fp.write(str(item)+"\n")//list中一项占一行
#         fp.close()
#     except IOError:
#         print("fail to open file")
# pro_path = "problem.txt"
# writeToTxt(pro_list,pro_path)

with open('problem.txt', 'wb') as out:
     for i in range(len(pro_list)):
            out.write('\n'.join(pro_list[i]).encode('utf-8'))
            out.write('\r\n')
# print pro_list[103]        



