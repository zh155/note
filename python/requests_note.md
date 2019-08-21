import requests

# get请求
r = requests.get('http://httpbin.org/get')
print(r.status_code, r.reason)
print('get请求', r.text)
# 带参数的get请求
r = requests.get('http://httpbin.org/get', params={'a': '1', 'b': '2}'})
print('带参数的get请求', r.json())
# post请求
r = requests.post('http://httpbin.org/post', data={'a': '1'})
print('post请求', r.text)

# 自定义headers请求
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
headers = {'User_Agent': ua}
r = requests.get('http://httpbin.org/headers', headers=headers)
print(r.json())

# 带cookies的请求
cookies = dict(userid='123456', token='xxxxxxxx')
r = requests.get('http://httpbin.org/cookies', cookies=cookies)
print('带cookies的请求', r.json())

# Basic-auth认证请求
r = requests.get('http://httpbin.org/basic-auth/zh/123456', auth=('zh', '123456'))
print('Basic-auth认证请求', r.text)

# 主动抛出状态码异常
bad_r = requests.get('http://httpbin.org/status/404')
print(bad_r.status_code)
bad_r.raise_for_status()

# 检查session中的cookies
s = requests.Session()
# session对象会保存服务器返回的set-cookies头信息里面的内容
r = s.get('http://httpbin.org/cookies/set/userid/123456')
print(r.json())
# 下一次请求会将本地所有的cookies 信息自动添加到请求头信息里面
r = s.get('http://httpbin.org/cookies')
print('检查session中的cookies', r.json())
# {'cookies': {'userid': '123456'}}
# 检查session中的cookies {'cookies': {'userid': '123456'}}

# 在requests中使用代理
print('不使用代理：', requests.get('http://httpbin.org/ip').json())
print('使用代理：', requests.get(
    'http://httpbin.org/ip',
    proxies={'http': 'iguye.com:41801'}, timeout=3).text
      )

r = requests.get('http://httpbin.org/delay/4', timeout=5)
print(r.json())
