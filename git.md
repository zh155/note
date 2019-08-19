# git笔记

## 安装git

安装完成后再命令行中输入

```
$ git config --global user.name "Your Name"
$ git config --global user.email "email@example.com"
```

git config --global	可以为机器上所有的git仓库使用这个配置，也可以为某个仓库指定不同的用户名和mail地址

## 创建版本库

#### git init

通过 git init 命令将目录变成 git 可以管理的仓库

#### git add * / filename

git add 告诉git 把文件添加到仓库

#### git commit -m ' 本次提交说明 '

提交到仓库

## 版本管理

### git  status

运行 git status  可以掌握仓库当前运行状态

### 查看更改内容	git diff

运行 git diff 可以查看更改的内容

## 版本回退

###  查看日志	git log 

git log --pretty=oneline 

git log 命令显示从最近到最远的提交日志

###  版本回退	git  reset  --hard  commit_id    / HEAD~1     

回到某次提

### 查看所有分支的操作记录	git	reflog

## 管理修改

### 查看工作区与最新版本的区别	git  diff  HEAD -- filename

### 丢弃工作区的修改	git  checkout   --   file 	

放弃  file 在  工作区的修改

命令`git checkout -- file`意思就是，把`file`文件在工作区的修改全部撤销，这里有两种情况：

一种是`file`自修改后还没有被放到暂存区，现在，撤销修改就回到和版本库一模一样的状态；

一种是`file`已经添加到暂存区后，又作了修改，现在，撤销修改就回到添加到暂存区后的状态。

总之，就是让这个文件回到最近一次`git commit`或`git add`时的状态。

### 撤销暂存区的修改，重新放回工作区	git 	reset	 HEAD	 file	

## 删除文件

### 删除文件 git	rm	

确实要从版本库中删除该文件

## 远程仓库

如果用户主目录下没有 .ssh 目录 或其目录下没有 id_rsa   id_rsa.pub  文件

### 创建 SSH KEY

ssh-keygen -t rsa -C  your_email

将生成的 id_rsa.pub  文件中的内容添加到GitHub

### 添加远程库

在GitHub中建立远程库后，关联远程库

```
git remote add origin git@github.com:michaelliao/learngit.git
```







