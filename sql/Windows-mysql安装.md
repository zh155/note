加入环境变量

mysqld --initialize-insecure
会自动在 D:\devtool\mysq\ 下创建data目录，不必手工创建data目录
mysqld -install
这步是安装 mysql 服务, 如果不是管理员运行会提示 “Install/Remove of the Service Denied!” 
, 如果不cd到 mysql的bin目录 服务安装后路径默认在 C:\Program Files\MySQL\ , 启动服务会失败 提示 “
发生系统错误 2。 系统找不到指定的文件”
net start mysql
这步是启动mysql 服务， 如果没有第一步 这步会启动失败 并提示 “请键入 NET HELPMSG 3534 以获得更多的帮助”
启动mysql以后就可以 在cmd 中 输入 mysql -u root -p 完成初次登陆了
然后更新root账户的密码为'root'
命令：update mysql.user set authentication_string=password("root") where user="root";
然后输入flush privileges;（刷新账户信息）