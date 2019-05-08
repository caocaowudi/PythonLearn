import requests

# 将参数传到URL里发送get请求
key_dic = {"key1": 'value1', 'key2': 'value2', 'key3': 'value3'}
r = requests.get('http://httpbin.org/get', params=key_dic)
print("URL 已经正确编码:", r.url)
print("-------------响应体------------")
print("字符串方式的响应体", r.text)
print("-------------分割线------------")

# 将参数传到URL里发送get请求
key_dic1 = {"key1": 'value1', 'key2': 'value2', 'key3': 'value3'}
r1 = requests.post('http://httpbin.org/post', params=key_dic1)
print("URL 已经正确编码:", r1.url)
print("字符串方式的响应体", r1.text)
