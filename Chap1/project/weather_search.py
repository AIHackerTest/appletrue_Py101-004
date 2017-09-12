# -*- coding: UTF-8 -*-
#读取文件weather_info.txt 文件，完成一个最简天气查询程序，运行在命令行界面，实现以下功能：
# 输入城市名，返回该城市的天气数据；
#输入help，打印帮助文档；
#输入exit，退出程序的交互
#退出程序之前，打印查询过的所有城市
#
dict = {}
history = {}
with open('weather_info.txt','r') as f:   #打开文件，需要将转换为字典的数据结构
    for line in f.readlines():
        sep = line.rstrip("\n").split(",") #rstrip（）用于去除每行之后的换行符，打印行内容或sep可以看到\n；
				      	   #split（）用中间的逗号分隔符对每一个列表内容进行拆分，为字典的对应key和value值
        #print(sep)
        dict[sep[0]]= sep[1]
#print(dict)
print("请输入您要查询的城市：")
while True:
    city = input("> ")

    if city in dict:
        print(dict[city])
        history[city]= dict[city]
        history.update({city:dict[city]}) 
    elif city == "help":
        print("""
        输入'help'，打印帮助文档；
        输入'exit'，退出程序文档
        输入'history'，打印查询过的城市""")
    elif city == "history":
        print(history)
    elif city == "exit":
        print(history)
        break
    else:
        print("找不到您查询的城市，输入help获得帮助。")

-## ----—以下为尝试过的代码————————————————————————————————————————————————————
dict = {}
with open('weather_info.txt','r') as f: 
    for line in f.readlines():
    sep = line.rstrip("\n").split(",")
    print(sep) 
    dict[sep[0]]=sep[1]
print(dict)
## macOS 下运行，可以形成字典，为什么？
_##_________________________________________________________________________
dict = {}
with open('weather_info.txt','r',encoding = 'utf-8') as f: #PyCharm 下可以自动输出中文，“encoding=utf-8”省略
    kv = f.readlines()
    for line in kv:
	sep = line.split(",")
	dict[sep[0] = sep[1]
	f.close()  #本句错，with..as 可以自动关闭文件
print(dict)

### indexError :list index out of range 
