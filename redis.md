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
    * BitMaps：位图
    * HyperLogLog：超小内存唯一值计数（有误差）
    * GEO：地理信息定位
* 支持多种编程语言
* 功能丰富
  * 发布订阅
  * Lua脚本
  * 事务
  * pipeline
* 简单
* 主从复制
* 高可用、分布式