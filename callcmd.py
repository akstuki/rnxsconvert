import os
import time
import shutil
'''
* @file     callcmd.py
* @brief    python script to convert Unicore *.obs files to rinex files
* @details  what you need to config:
            1. ext name
            2. path_rnx for output
            3. *.obs path
            4. work path
* @author   name:ChenXiaoqiang mail:309905109@qq.com
* @date     2016-10-14
* @history  2016-10-14 new created
'''

'''
ext name
'''
EXTO = '.15O'
EXTN = '.15N'
EXTC = '.15C'
EXTG = '.15G'

'''
rinex output directory
'''
path_rnx="F:\\1-own\\python\\torinex\\rnx"

def callCMD(command):
    os.system(command)
    

def renameAndMove(newname, path):
    filelist = []
    for root, dirs, files in os.walk(path):
        filelist=files
    if(len(filelist)==0):
        print ('no pictures in path %s' % path)
        return
    count = len(filelist)
    for num in range(count):
        filename = filelist[num]
        fullname = path+'\\'+filename
        print (fullname)
        ext = os.path.splitext(filename)[1]
        if(ext==EXTN):
            shutil.move(fullname,  path_rnx+'\\'+newname+EXTN)
        if(ext==EXTC):
            shutil.move(fullname,  path_rnx+'\\'+newname+EXTC)
        if(ext==EXTG):
            shutil.move(fullname,  path_rnx+'\\'+newname+EXTG)
        if(ext==EXTO):
            shutil.move(fullname,  path_rnx+'\\'+newname+EXTO)
            
    
	
def doColy(path,path2):
    filelist = []
    for root, dirs, files in os.walk(path):
        filelist=files
    if(len(filelist)==0):
        print ('no files in path %s' % path)
        return
    count = len(filelist)
    for num in range(count):
        print (("%d in %d...") % (num,count))
        filename = filelist[num]
        fullname = path+'\\'+filename
        print (fullname)
        ext = os.path.splitext(filename)[1]
        
        fullname2=path2+'\\'+filename
        shutil.copy(fullname,  fullname2)
        print (ext)
        if(ext != '.obs'):
            print ('not match')
            continue
        command = "Converter.exe %s -batch -r301 %d" % (fullname2,num)
        callCMD(command)
        os.remove(fullname2)
        
        renameAndMove(filename, path2)
        
        #time.sleep(1)

if __name__ == '__main__':
    '''
    path - directory of *.obs data
    pathtemp - directory of work
    '''
    path="F:\\1-own\\python\\torinex\\data"
    pathtemp="F:\\1-own\\python\\torinex\\data2"
    doColy(path,pathtemp)
