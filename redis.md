# redis

## redis 初识

### redis是什么

* 开源
* 基于键值的存储服务系统
* 多种数据结构
  	- String
  	- Hash
  	- Lists
  	- Sets
  	- Sorted Sets
* 高性能、功能丰富

### redis的特性

* 速度快
  * 10W OPS  （官方：每秒10w次读写）
        * 数据存在内存中
        * C语言实现
        * 线程模型：单线程
* 持久化（断电不丢数据）
  * redis 所有数据保存在内存中，对数据的更新将异步地保存在磁盘中
* 多种数据结构（5种主要数据结构）
  * String
  * Hash Tables （objects）
  * Lists
  * Sets
  * Sorted Sets
  * 衍生数据结构
    * BitMaps：位图	（String）
    * HyperLogLog：超小内存唯一值计数（有误差）(String)
    * GEO：地理信息定位  (Sorted Sets)
* 支持多种编程语言
* 功能丰富
  * 发布订阅
  * Lua脚本
  * 事务
  * pipeline
* 简单
  * 源代码量少
  * 不依赖外部库
  * 单线程模型
* 主从复制
* 高可用、分布式
  * 高可用 --> Redis-Sentinel (v2.8)支持高可用
  * 分布式  -->  Redis-Cluster (v3.0)支持分布式

### Redis 典型应用场景

* 缓存系统
  * 用户访问 APP Server  首先从Cache 层获取数据
* 计数器
  * 用于转发数、评论数等
* 消息队列系统
  * 消息队列系统在很多公司中已经成为中间件或者项目开发的标配
* 排行榜（视频、音乐等排行榜）
* 社交网络
  * 关注数、时间轴等  使用 Redis 实现
* 实时系统
  * 垃圾邮件处理系统、过滤器等

### Redis 安装

* Redis 安装
  * redis-server --> redis 服务器
  * redis-cli --> redis 命令行客户端
  * redis-benchmark --> redis 基准测试（性能测试）工具
  * redis-check-aof  --> AOF文件修复工具
  * redis-check-dump --> RDB文件检查工具
  * redis_sentinel --> Sentinel 服务器 （2.8以后）
* 可执行文件说明
* 三种启动方法
  * 最简启动
    * redis-server  （使用redis 默认配置启动）
    * 验证
      * ps -ef | grep redis  （查看进程方式）
      * netstat -antpl | grep redis  （查看端口是否是listening 状态）
      * redis-cli   -h ip  -p port  ping
  * 动态参数启动
    * redis-server --port  6380 (在6380端口启动redis-server)
  * 配置文件启动（推荐）
    * redis-server  configPath
  * 比较
    * 生产环境选择配置启动  （一台机器可能部署很多redis）
    * 单机多实例配置文件可以用端口区分开
* 简单的客户端连接

### redis客户端返回值

* 状态回复
  * \>ping      PONG
* 错误回复
  * 返回错误
* 整数回复
  * 返回整数
* 字符串回复
  * 返回字符串
* 多行字符串回复
  * 返回多个字符串

### redis 常用配置

* daemonize	--> 是否是守护进程（no | yes） 默认是 no  推荐 yes
* port 	-->  redis 对外端口号
* logfile	--> redis 系统日志
* dir    -->  redis 工作目录

## redis API的使用和理解

### 通用命令

* 通用命令

  * keys   O(n)   获取数据库中的键    keys 命令一般不在生产环境中使用
    * keys * 怎么用？   scan   热备从节点
    * keys *   获取所有的 键
    * keys [pattern]    遍历所有 key
      * keys  he*   获取所有以 he 开头的键
      * keys   he[h-l]*   获取以 he 开头 第三个为 h-l 之间的字母  的所有键
      * key   he?   获取以 he 开头 且只有三位  的键
  * dbsize  O(1)	算出数据大小    10个 key  dbsize 为 10 
  * exists  key	O(1)   检查key是否存在   存在 返回 1   不存在返回 0
  * del	key [ key ...]    O(1)   成功删除 返回 1   key 不存在 返回 0
  * expire  key  seconds  O(1)   设置过期时间 
  * ttl  key   O(1)  查询 key 剩余的过期时间    返回 -2  说明 key 已经不存在    返回 -1  说明 key 存在  但是没有过期时间
  * persist  key   O(1)  去掉 key 的过期时间
  * type  key   O(1)   查看 key 数据类型     如果 key 不存在 返回 none

* 数据结构和内部编码

* 单线程架构

  * 同一时刻只能执行一条命令

  * 单线程为什么这么快

    * 纯内存 （主要原因）

    * 非阻塞IO

    * 避免了线程切换和竞态消耗

    * 使用单线程时注意

      * 一次只运行一条命令

      * 拒绝长（慢）命令     keys  flushall  flushdb  slow  lua  script  mutil/exec   operate big value(collection)

        

### 字符串类型

* 场景
  * 缓存
  * 计数器
  * 分布式锁
  * 等等。。。。
* 结构和命令

  * get  key  O(1)
  * mget   key [ key ...]   O(n)  批量获取 key ，原子操作
  * set   key   value  O(1)

    * set  key  value     不管 key 是否存在，都设置
    * setnx  key  value    key不存在时  才设置    (类似 add  添加 操作)
* set  key   value   xx   key 存在  才设置  （类似 update  更新操作）
    * mset  key  value [ key value ...]    O(n)   设置多对 key-value
  * 1 次 mget = 1 次网络时间 + n 次 命令时间
  * 整形操作  O(1)

    * incr  key     key 自增 1 ，如果 key 不存在，自增后 get (key) = 1
    * decr  key     key 自减 1，如果 key  不存在 ，自检后 get (key) = -1
    * incrby  key   k      key  自增 k ，如果 key 不存在，自增后 get(key) = k
    * decrby    key   k    key  自减 k，如果 key 不存在，自减后 get(key) = -k
* 快速实战

  * 如何实现记录网站每个用户个人主页的访问量？  因为 redis 是单线程  所以不用担心 并发 会出现 记错数
    * incr  userid:pageview
  * 缓存视频的基本信息（数据源在 MySQL 中） 伪代码
    * 通过视频 id 在 redis 中获取 ， 如果没有 获取到  则从 MySQL 中获取。取到之后 存入 redis 中
  * 实现分布式 id 生成器
* 内部编码
* 查漏补缺
  * getset  key  newvalue  O(1)  原子组合操作  
    * set  key  newvalue   并返回旧的value
  * append  key  value    O(1)
    * 将 value 追加到旧的value
  * strlen  key   O(1)
    * 返回字符串的长度（注意中文）
  * incrbyfloat    key   3.5  O(1)  增加 key 对应的值 3.5
  * getrange  key  start  end   O(1)   获取字符串指点下标所有的值
  * setrange   key  index  value  O(1)   将字符串对应下标设置成新的值

### 哈希类型

* 特点

  * 哈希键值结构

  * > |       key       | field |  value  |
    > | :-------------: | :---: | :-----: |
    > |                 | name  | Ronaldo |
    > | **user:1:info** |  age  |   40    |
    > |                 | Date  |   201   |

    

* 重要API

  * hget  key   field  O(1)   获取hash  key  对应的 field  的 value
  * hgeall key    获取 key 对应 的所有 file  value
  * hset  key  field  value    O(1)   设置 hash key  对应 field 的 value
  * hdel   key field   O(1)    删除 hash key 对应 field 的 value    
  * hexists  key  field  O(1)  判断 hash  key  是否存在 field
  * hlen   key   O(1)   获取 hash  key field 的数量
  * hmget   key  field1  field2 ...  fieldN   O(n)   批量获取 hash key 的一批 field 对应的值
  * hmset key  field1 value1 [ field2  value2 ... ]  O(n)   批量设置 hash key  的 一批 field  value
  * hgetall  key   O(n)   返回 hash key 对应所有的 field 和 value
  * hvals  key   O(n)   返回 hash key 对应的所有 value
  * hkeys   key   O(n)   返回 hash key 对应的所有 field

* hash  vs  string

  * 相似的 API
    * get   ----  hget
    * set  setnx   ------------ hset hsetnv
    * del   ----------   hdel
    * incr incrby decr decrby   -------------    hincrby
    * mset ---------- hmset          

* 查漏补缺

  * hsetnx  key  field  value  设置hash key 对应 field 的 value （如果 field 已经存在，则失败）
  * hincrby  key  field  intCounter  hash key对应的field 的 value 自增 intCounter
  * hincrbyfloat  key  field  floatCounter       hincrby 浮点数版

* 实战

  * 记录网站每个用户个人主页的访问量？

    * hincrby  user:1:info  pageview  count    用户 user:1:info  中的  pageview 自增

  * 缓存视频的基本信息(数据源在MySQL中)  伪代码

    

### 列表类型

* 特点

  * 有序
  * 可以重复

* 主要API

  * rpush / lpush  key  value1 [ value2 ... ]  O(1 - n)  从列表右 / 左端插入值（1 - N 个）

  * linsert  key  before / after  value newvalue  O(n) 在 value  前 / 后 插入 新值

  * lpop key   O(1)   从左边弹出一个元素

  * rpop key   O(1)   从右边弹出一个元素

  * lrem  key count value  O(n)

    * 根据 count 的值，从列表中删除所有 value 相等的项
    * count > 0  ，从左至右，删除 最多 count 个 与 value 相等的 值
    * count < 0 ，从右至左，删除 最多 abs(count) 个 与 value 相等的值 
    * count = 0 ，删除所有与 value 相等的值

  * ltrim  key  start   end    O(n)   按照索引范围修剪列表

  * lrange  key  start end    O(n)   获取指定范围内列表的元素   如果end < 0  则 从右开始

  * lindex  key  index   O(n)   获取 列表中 对应的 索引值

  * llen  key   O(1)   获取列表的长度

  * lset  key  index  newvalue   设置列表指定索引值为 newvalue 

    

* 实战

  * TimeLine

* 查漏补缺

  * blpop / brpop  key  timeout     lpop 阻塞版本，timeout是阻塞超时时间，timeout = 0 代表永不阻塞

* TIPS

  * LPUSH + LPOP = Stack
  * LPUSH + RPOP = Queue
  * LPUSH + LTRIM = Capped Collection
  * LPUSH + BRPOP = Message Queue

### 集合类型

* 特点
  * 无序
  * 无重复元素
  * 支持集合间操作
* 集合内 API 和实战
  * API
    * sadd  key  element   O(1)  向集合key中添加 element （如果 element 已经存在，添加失败）
    * srem  key   element   O(1)   删除集合key中的 element
    * scard    collection  计算集合大小
    * sismember   collection  it   判断it 是否在集合中   是 返回 1  否则 返回 0  
    * srandmember   collection  count    从 集合中随机挑选 count 个元素
    * smembers   collection    取出集合中多有元素
    * spop  collection   从集合中随机弹出一个元素
  * 实战
    * 抽奖系统
    * 赞、踩
    * 标签（tag）
* 集合间 API 和实战
  * API
    * sinter  collection1   collection2   取交集
    * sdiff    collection1   collection2   取差集
    * sunion    collection1   collection2   取并集
    * sdiff | sinter | suion  +  store  destkey     将 结果集 保存在 destkey  中
  * 实战
    * 共同关注

### 有序集合类型

* 特点

  * >|       key        | score | value |
    >| :--------------: | :---: | :---: |
    >|                  |   1   | kris  |
    >| **user:ranking** |  34   | mike  |
    >|                  |  32   | john  |
    >
    >

* 重要 API

  * zadd   key   score element   O(logN)    （可多个） （score 不可重复）
  * zrem   key  element    O(1) （可以是多个） 删除元素
  * zscore  key  element   O(1)    返回元素 score
  * zincrby  key increScore element    O(1)    增加或减少 元素的 分数 
  * zcard    key    O(1)   返回元素的个数
  * zrank     key  element    获取 element 的排名 （score  从 0开始 从小到大）
  * zrange  key   0  -1  [ withscores ]    O(log(n) + m)   (  n:有序集合中元素的个数   m: 要获取的范围内元素的个数 )  获取所有排名 （升序）
  * zrangebyscore   key  minScore  maxScore  [ withscores ]    O(log(n) + m)  返回指定分数范围内的升序元素
  * zcount  key  minScore  maxScore   O(log(n) + m)   返回有序集合内 在指定分数范围内的个数
  * zremrangebyrank  key  start  end    O(log(n) + m)    删除指定排名内的升序元素 
  * zremrangebyscore  key   minScore  maxScore   O(log(n) + m)    删除指定分值范围内的元素

* 实战

  * 排行榜

* 查漏补缺

  * zrevrank    从高到低 排名   对应 zrank  
  * zrevrange           对应 zrange
  * zrevrangebyscore            对应 zrangebyscore
  * 集合操作
    * zinterstore    
    * zunionstore

## python客户端

* ~~~ python
  import redis
  
  client = redis.StrictRedis(host='127.0.0.1', port=6379)
  key = 'hello'
  setResult = client.set(key, 'python-redis')
  print(setResult)
  value = client.get(key)
  print(value)
  
  ~~~

* 

## redis 其他功能

### 慢查询 

* 生命周期

  1. 发送命令
  2. 排队
  3. 执行命令
  4. 返回结果

* 两点说明

  1. 慢查询发生在第3阶段
  2. 客户端超时不一定慢查询，但慢查询是客户端超时的一个可能因素

* 两个配置

  1. slowlog - max - len

     * 先进先出队列
     * 固定长度

     * 保存在内存内

  2. slowlog - log - slower - than

     * 慢查询阈值（单位：微秒）
     * slowlog - log - slower - than = 0 ， 记录所有命令
     * slowlog - log - slower - than < 0 ， 不记录任何命令

  3. 配置方法

     * 默认值
       * config get slowlog-max-len=128
       * config gt slowlog-log-slower-than=10000 (微秒)
     * 修改配置文件重启（启动以后  不建议重启操作）
     * 动态配置
       * config set slowlog-max-len 1000
       * config set slowlog-log-slower-than 1000

* 慢查询命令

  * slowlog get [n]  获取慢查询队列     n:指定条数
  * slowlog len   获取慢查询队列长度
  * slowlog reset    清空慢查询队列

### 运维经验

1. slowlog-max-len 不要设置过大，默认 10ms ，通常 设置1ms
2. slow-log-slower-than 不要设置过小，通常设置 1000左右
3. 理解命令生命周期
4. 定期持久化慢查询

### pipeline

* 什么是流水线 （节省网络时间的开销）
* 客户端实现
* 与原生操作对比
* 使用建议
  * 注意每次pipeline 携带数据量
  * pipeline 每次只能作用在一个Redis 节点上
  * M操作与 pipeline 的区别

### 发布订阅

* 角色
  1. 发布者
  2. 订阅者
  3. 频道
* 模型 
* API
  * publish    发布
    * publish  channel message      返回订阅个数
  * subscribe   订阅
    * subscribe  [ channel ] 一个或多个
  * unsubscribe    取消订阅
    * unsubscribe  [ channel ]    一个或多个
  * 其他
    * psubscribe  [ pattern ...  ]  订阅模式
    * punsubscribe    退订指定的模式
    * pubsub  channels    列出至少有一个订阅者的频道
    * pubsub numsub  [ channel ... ]  列出给定频道订阅者的数量
* 发布订阅消息队列
  * 使用场景

### Bitmap （节省内存方案）   type=string

* 位图
* API
  * setbit  key  offset  value    给位图指定索引设置值
  * getbit  key offset    获取位图指定索引的值
  * bitcount  key  [ start  end ]    获取位图指定范围（start  end   单位为字节    如果不指定则获取全部）  位置为 1 的个数
  * bitop  op  destkey  key [ key ... ]  做多个 Bitmap 的 and （交集）  or （并集）   not （非） xor （异或） 操作， 并将结果保存在 destkey 中
  * bitops  key  targetBit [start]  [end]  计算位图指定范围  第一个偏移量对应的值等于 targetBit 的 位置   不指定 start end  则 获取全部
* 独立用户统计
  1. 使用 set 和 Bitmap

### HyperLogLog (基于HyperLogLog算法)  type=string

极小空间完成独立数量统计 

* 新的数据结构？
* 三个命令
  * pfadd  key  element [ element ... ]   向 hyperloglog 添加元素
  * pfcount   key [ key ...] 计算 hyperloglog 的独立总数
  * pfmerge  destkey  sourcekey [ sourcekey ... ] 合并多个 hyperloglog
* 内存消耗
* 使用经验 
  1. 是否能容忍错误？ 错误率 0.81%
  2. 是否需要单条数据？

### GEO  （地理信息定位）type=zset

* GEO 是什么
  * GEO（地理信息定位）：存储经纬度，计算两地距离，范围计算等
* 5 个城市经纬度
* 相关命令
  * geoadd  key  longitude latitude  member [ longitude  latitude  member ... ] 增加地理位置信息
  * geopos  key  member  [ member ... ]   获取地理位置信息
  * geodist   key member1  member2  [ unit ]    获取两个地理位置的距离     unit:m、km、mi、ft
  * georadius
* 相关说明

## 开发运维常见问题

* fork 操作

  1. 同步操作
  2. 与内存量息息相关：内存越大，耗时越长 （与机器类型相关）
  3. info:latest_fork_usec

* 改善 fork

  1. 有限使用物理机或者高效支持fork操作的虚拟化技术
  2. 控制Redis 实力最大可用内存 maxmemory
  3. 合理配置 Linux 内存分配策略 vm.overcommit_memory = 1
  4. 降低 fork 频率 ：例如放宽 AOF 重写自动触发时机， 不必要的全量复制

* 子进程开销和优化

  1. CPU

     * 开销：RDB 和 AOF 文件生成， 属于 CPU 密集型
     * 优化： 不做CPU 绑定，不和CPU 密集型部署

  2. 内存

     * 开销：fork 内存开销， copy-on-write

  3. 硬盘

     * 开销：AOF 和 RDB 文件写入，可以结合 iostat, iotop 分析

     * 不要和高硬盘负载服务部署在一起：存储服务，消息队列等
     * no-appendfsync-on-rewrite = yes
     * 根据写入量决定磁盘类型：例如ssd
     * 单机多实例持久化文件目录可以考虑分盘

* AOF 追加阻塞

* 单机多实例部署



