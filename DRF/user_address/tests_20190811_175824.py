cache_format = 'throttle_%(scope)s_%(ident)s'
# cache_format = 'throttle_%s_%s'
print(cache_format % ({'scope': 11, 'ident': 11}))
print(cache_format.format(scope=11, ident=11))
