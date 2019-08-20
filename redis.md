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

  * set   key   value  O(1)

    * set  key  value     不管 key 是否存在，都设置
    * setnx  key  value    key不存在时  才设置    (类似 add  添加 操作)

    * set  key   value   xx   key 存在  才设置  （类似 update  更新操作）

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

### 哈希类型

### 列表类型

### 集合类型

### 有序集合类型









