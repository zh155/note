import time

from django.core.cache import cache
from rest_framework import throttling

'''
class AddressThrottling(throttling.BaseThrottle):
    def allow_request(self, request, view):
        # 获取唯一标识
        key = self.get_ident(request)
        print(key)
        history = cache.get(key, [])
        # 清洗数据  清除一分钟前的请求记录
        while history and history[-1] <= time.time() - 60:
            history.pop()

        # 超过请求次数被截流
        if len(history) >= 10:
            return False
        # 记录本次请求时间
        history.insert(0, time.time())
        # 记录请求记录于缓存中
        cache.set(key, history, timeout=60)
        return True
'''


class AddressThrottling(throttling.SimpleRateThrottle):
    # 配置请求速率
    # rate = '5/m'

    # 外部配置请求速率
    scope = 'user_address_throttling'

    # 获取缓存 key

    def get_cache_key(self, request, view):
        # 扩展key 以免重复
        return self.cache_format % {'scope': self.scope, 'ident': self.get_ident(request)}
        # return 'cache_' + self.get_ident(request)
        # return self.get_ident(request)
