import Configuration

c = open('txt/1bak_json.txt','w')
f = open('txt/1bak.txt')
for i in f.readlines():
    j = i.split('\n')[0]
    a = {"from":Configuration.Config.bucketName,"uid":"liushaowei","urls":[j]}
    print(a)
