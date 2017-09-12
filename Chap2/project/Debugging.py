import requests
import json
from pprint import pprint       #pprint 方法打印json文本，可以清晰的看到数据结构

location = input('请输入您要查询的城市或指令，如 北京,如需帮助，请输入help。\n> ')

#def fetchWeather(location): # U785B76FC9"   用户ID
result = requests.get('https://api.seniverse.com/v3/weather/now.json', params={
        'key': '4r9bergjetiv1tsd',
        'location': location,
        'language': 'zh-Hans',
        'unit': 'c'
    }, timeout=30) #请求的延时设置
# https://api.seniverse.com/v3/weather/now.json?key=4r9bergjetiv1tsd&location=location&language=zh-Hans&unit=c 此地址效果同
pprint(json.loads(result.text))  #打印获取到的json文本信息，显示格式如下，便于下一步操作，注意，内容是按照字母顺序排序显示
#————————————————————————————————————————————————--------------------
{'results': 
 [
    {'last_update': '2017-08-24T22:35:00+08:00',
        'location': {'country': 'CN',
                     'id': 'WXRVB9QYXKY8',
                     'name': '沈阳',
                     'path': '沈阳,沈阳,辽宁,中国',
                     'timezone': 'Asia/Shanghai',
                     'timezone_offset': '+08:00'},
             'now': {'clouds': '',
                      'code': '1',
                      'dew_point': '',
                      'feels_like': '18',
                      'humidity': '69',
                      'pressure': '1002',
                      'temperature': '18',
                      'text': '晴',
                      'visibility': '35.0',
                      'wind_direction': '南',
                      'wind_direction_degree': '184',
                      'wind_scale': '1',
                      'wind_speed': '4.32'}}]}
#——————————————————————————————————————————————————————————————————————

r = json.loads(result.text)  #json.loads() 将json格式转化为py数据格式
city = r['results'][0]['location']['name']
weather = r['results'][0]['now']['text']
temperature = r['results'][0]['now']['temperature']
search_time = r['results'][0]['last_update']
print("您查询的城市为{0},天气{1} ，气温 {2} 摄氏度" .format(city,weather,temperature))
print("---查询时间：{0}---" .format(search_time))

