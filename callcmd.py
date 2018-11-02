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
rinex output directory
'''
path_rnx="rnx"

def renameAndMove(newname, path):
    filelist = []
    for root, dirs, files in os.walk(path):
        filelist=files
    if len(filelist) == 0:
        print ('no files in path %s' % path)
        return

    for var in filelist:
        filename = var
        fullname = os.path.join(path, filename)
        ext = os.path.splitext(filename)[1]
        if is_rinex_ext(ext):
            shutil.move(fullname, os.path.join(path_rnx, newname+ext))

def is_rinex_ext(ext: str):
    if ext[1].isdigit() == False:
        return False
    if  ext[2].isdigit() == False:
        return False
    if ext[3] not in ['N', 'G', 'O', 'C']:
        return False
    return True

def do_convert(path, path2):
    filelist = []
    for root, dirs, files in os.walk(path):
        filelist = files
    if len(filelist) == 0:
        print ('no files in path %s' % path)
        return

    for num , val in enumerate(filelist):
        print ("{num} in {total}".format(num = num, total = len(filelist)))
        filename = val
        fullname = os.path.join(path, filename)
        ext = os.path.splitext(filename)[1]

        fullname2 = os.path.join(path2, filename)
        shutil.copy(fullname, fullname2)

        if ext != '.obs' and ext != '.OBS':
            print ('{file} skip'.format(file = filename))
            continue
        command = "Converter.exe {file} -batch -r301 {id}".format(file=fullname2, id=num)
        os.system(command)
        os.remove(fullname2)
        renameAndMove(filename, path2)

if __name__ == '__main__':
    '''
    path - directory of *.obs data   
    pathtemp - directory of work
    '''
    path = "data"
    pathtemp = "data2"
    do_convert(path, pathtemp)
