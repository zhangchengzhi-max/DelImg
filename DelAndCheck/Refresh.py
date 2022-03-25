# -*- coding: utf-8 -*-
import json
import os,time
import threading
import requests
import Configuration


f = open(Configuration.Config.Refreshfile)
delUrl = Configuration.Config.DelApi

rlock = threading.RLock()
curPosition = 0

sum = 0
for i in f.readlines():
    sum+=1

class Reader(threading.Thread):
    def __init__(self, res):
        self.res = res
        super(Reader, self).__init__()
    def run(self):
        global curPosition
        fstream = open(self.res.fileName, 'r')
        sum=0
        while True:
            #加锁
            rlock.acquire()
            startPosition = curPosition
            curPosition = endPosition = (startPosition + self.res.blockSize) if (startPosition + self.res.blockSize) < self.res.fileSize else self.res.fileSize
            #释放锁
            rlock.release()
            if startPosition == self.res.fileSize:
                break
            elif startPosition != 0:
                fstream.seek(startPosition)
                fstream.readline()
            pos = fstream.tell()

            while pos < endPosition:
                sum += 1
                line = fstream.readline()
                rlock.acquire()
                #调用RefreshApi
                url = Configuration.Config.RefreshApi+"?url="+line
                response = requests.get(url)
                ress = response.text
                ress2 = ress.split('resultcode":')[1]
                resultcode = ress2.split('}')[0]
                if int(resultcode)!=200:
                    print(int(resultcode))
                pos = fstream.tell()
                rlock.release()
        fstream.close()

class Resource(object):
    def __init__(self, fileName):
        self.fileName = fileName
        #分块大小
        self.blockSize = int (sum/Configuration.Config.RefreshThread)
        self.getFileSize()
    #计算文件大小
    def getFileSize(self):
        fstream = open(self.fileName, 'r')
        fstream.seek(0, os.SEEK_END)
        self.fileSize = fstream.tell()
        fstream.close()

if __name__ == '__main__':
    starttime = time.time()
    #线程数
    threadNum = Configuration.Config.DelThread
    #文件
    # fileName = 'txt/0006urllast.txt'
    fileName = Configuration.Config.Refreshfile
    res = Resource(fileName)
    threads = []
    #初始化线程
    for i in range(threadNum):
        rdr = Reader(res)
        threads.append(rdr)
    #开始线程
    for i in range(threadNum):
        threads[i].start()
    #结束线程
    for i in range(threadNum):
        threads[i].join()

    print("刷新所消耗的时间为：",time.time() - starttime,"秒")