# coding:utf-8

import sys
import os
import win32api
import codecs

import csv

reload(sys)
sys.setdefaultencoding( "utf8" )


class FileRead(object) :
  
    def fread(self,path,heading=0):
        """
        读取csv文件
        :param path:
        :param heading: 0表示csv文件没有表头，1代表有。默认为0
        :return:
        """
        L2 = []
        with codecs.open(path,'r','gbk') as f:
            data = csv.reader(f)
            if heading != 0:
                head = next(data)
            for user in data:
                if not user[0]:
                    break
                L1 = [u.decode('utf8') for u in user]
                L2.append(L1)
            return L2
    def close_proc_by_browser_name(self, browser):
        """Close a process by process name."""
        if browser == 'Chrome':
            process_name = 'chromedriver.exe'
        elif browser == 'Firefox':
            process_name = 'geckodrive.exe'
        else:
            process_name = 'IeDriverserver.exe'
        os.system("taskkill /f /im " + process_name)

    def open_proc(self,pro,url):
        f = 'taskkill /F /IM pro'
        os.system(f)
        win32api.ShellExecute(0, 'open', r'%s' %url, '','',1)
    def close_proc_by_name(self,process_name):
        f = 'taskkill /F /IM ' + process_name
        os.system(f)

if __name__ == '__main__':
    pass
