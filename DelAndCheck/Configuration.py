class Config:
    CheckThread = 20
    DelThread = 2
    RefreshThread = 6


#---------------------------------要处理的文件--------------------------------------
    #要删除文件
    Delfile = 'txt/0006urllast.txt'
    #需要检查的文件
    checkfile = 'txt/0323.txt'
    #需要刷新的文件
    Refreshfile = 'txt/0006urllast.txt'







# ---------------------------------处理后的文件--------------------------------------
    #检查后存在的文件
    exsitfile = 'txt/0323exsit.txt'


    #出现解析网址错误的文件
    needalterfile = 'txt/needalter.txt'




#-------------------------------------接口------------------------------------------
    DelApi = "http://upload.ws.126.net/api/img/delete"
    # DelApi = "http://upload.buzz.service.163.org/api/img/delete"
    RefreshApi = "https://purge.ws.netease.com/api/purge"

    bucketName = "cdn"
    # bucketName = "nosjustdel"