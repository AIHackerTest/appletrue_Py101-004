import requests
import json

# from pprint import pprint

history = []


def fetchWeather(xxx):
    # xxx = input('请输入您要查询的城市或指令，如 北京,如需帮助，请输入help。\n> ')

    result = requests.get('https://api.seniverse.com/v3/weather/now.json', params={
        'key': '4r9bergjetiv1tsd',
        'location': xxx,
        'language': 'zh-Hans',
        'unit': 'c'
    }, timeout=30)  # 请求的延时设置

    print(result)

    r = json.loads(result.text)  # json.loads() 将json格式转化为py数据格式
    print(r)

    city = r['results'][0]['location']['name']
    print(city)

    weather = r['results'][0]['now']['text']
    print(weather)

    temperature = r['results'][0]['now']['temperature']
    print(temperature)

    search_time = r['results'][0]['last_update']
    print(search_time)

    search_result = "您查询的城市为{0},天气{1} ，气温 {2} 摄氏度".format(city, weather, temperature)
    print(search_result)

    print("---查询时间：{0}---".format(search_time))

    history.append(search_result)
    print(history)


# ccc = input('请输入您要查询的城市或指令，如 北京,如需帮助，请输入help。\n> ')
# fetchWeather(ccc)

while True:
    input_words = input('请输入您要查询的城市或指令，如 北京,如需帮助，请输入help。\n> ')

    if input_words == "help":
        print("""
            输入'help'，打印帮助文档；
            输入'exit'，退出程序
            输入'history'，显示您刚刚查询过的城市""")
    elif input_words == "history":
        print(history)
    elif input_words == "exit":
        print(history)
        # break
        exit(0)
    else:
        try:
            fetchWeather(input_words)
        except:
            print("找不到您查询的城市，输入help获得帮助。")
            continue
