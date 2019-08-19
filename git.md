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

### 将本地库内容推送到远程库

git   push  -u  origin  master

把本地库的内容推送到远程，用`git push`命令，实际上是把当前分支`master`推送到远程

由于远程库是空的，我们第一次推送`master`分支时，加上了`-u`参数，Git不但会把本地的`master`分支内容推送到远程新的`master`分支，还会把本地的`master`分支和远程的`master`分支关联起来，在以后的推送或者拉取时就可以简化命令。

```
 git push origin master
```

### 从远程库克隆

git clone git@github.com:zh155/note.git

## 分支管理

### 创建与合并分支

git checkout  -b  dev    创建并切换分支

git    branch  dev    创建分支

git    checkout   dev   切换分支

### 查看分支

git   branch

### 合并分支

git   merge  dev

git   merge  命令用于合并指定分支到当前分支，合并之后可以删除dev分支

git   branch  -d   dev

删除 dev  分支

### 解决冲突

当Git无法自动合并分支时，就必须首先解决冲突。解决冲突后，再提交，合并完成。

用`git log --graph`命令可以看到分支合并图。

### 分支管理策略

通常，合并分支时，如果可能，Git会用`Fast forward`模式，但这种模式下，删除分支后，会丢掉分支信息。

如果要强制禁用`Fast forward`模式，Git就会在merge时生成一个新的commit，这样，从分支历史上就可以看出分支信息

### 禁用 fast forward

```
git merge --no-ff -m "merge with no-ff" dev
```

--no-ff   参数表示禁用 fast  forward

因为本次合并要创建一个新的commit，所以加上`-m`参数，把commit描述写进去。

合并分支时，加上`--no-ff`参数就可以用普通模式合并，合并后的历史有分支，能看出来曾经做过合并，而`fast forward`合并就看不出来曾经做过合并。

### bug分支

git   stash   可以把当前工作现场“储藏”起来，等以后恢复现场后继续工作

修复bug之后使用

git stash list查看之前的工作现场

工作现场还在，Git把stash内容存在某个地方了，但是需要恢复一下，有两个办法：

一是用`git stash apply`恢复，但是恢复后，stash内容并不删除，你需要用`git stash drop`来删除；

另一种方式是用`git stash pop`，恢复的同时把stash内容也删了

#### 复制提交到当前分支

同样的bug，要在dev上修复，我们只需要把`4c805e2 fix bug 101`这个提交所做的修改“复制”到dev分支。注意：我们只想复制`4c805e2 fix bug 101`这个提交所做的修改，并不是把整个master分支merge过来。

为了方便操作，Git专门提供了一个`cherry-pick`命令，让我们能复制一个特定的提交到当前分支：

```
git cherry-pick 4c805e2
```

### 多人协作

git   remote  查看远程库的信息

git   remote   -v   详细查看远程库信息，显示抓取和推送的origin地址。如果没有推送权限，就看不到push的地址

#### 推送分支

git   push  origin   master / dev

推送分支，就是把该分支上的所有本地提交推送到远程库。推送时，要指定本地分支，这样，Git就会把该分支推送到远程库对应的远程分支上：

#### 多人协作的工作模式通常是这样：

1. 首先，可以试图用`git push origin <branch-name>`推送自己的修改；
2. 如果推送失败，则因为远程分支比你的本地更新，需要先用`git pull`试图合并；
3. 如果合并有冲突，则解决冲突，并在本地提交；
4. 没有冲突或者解决掉冲突后，再用`git push origin <branch-name>`推送就能成功！

如果`git pull`提示`no tracking information`，则说明本地分支和远程分支的链接关系没有创建，用命令`git branch --set-upstream-to <branch-name> origin/<branch-name>`。

这就是多人协作的工作模式，一旦熟悉了，就非常简单。

### 小结

- 查看远程库信息，使用`git remote -v`；
- 本地新建的分支如果不推送到远程，对其他人就是不可见的；
- 从本地推送分支，使用`git push origin branch-name`，如果推送失败，先用`git pull`抓取远程的新提交；
- 在本地创建和远程分支对应的分支，使用`git checkout -b branch-name origin/branch-name`，本地和远程分支的名称最好一致；
- 建立本地分支和远程分支的关联，使用`git branch --set-upstream branch-name origin/branch-name`；
- 从远程抓取分支，使用`git pull`，如果有冲突，要先处理冲突。

### 标签管理

标签也是版本库的一个快照。

#### 创建标签

git   tag   \<name\>  

先切换到需要打标签的分支上   然后使用   git   tag   \<name\> 

git   tag

查看所有标签 注意，标签不是按时间顺序列出，而是按字母排序的

git   show   \<tagname\> 

查看标签信息

git   tag  v1.0  f5434

对已有提交 打标签

```
git tag -a v0.1 -m "version 0.1 released" 1094adb
```

还可以创建带有说明的标签，用`-a`指定标签名，`-m`指定说明文字

git   tag  -d  v1.0

删除标签    因为创建的标签都只存储在本地，不会自动推送到远程。所以，打错的标签可以在本地安全删除。

git push origin \<tagname\>

推送某个标签到远程

git   push  origin  --tags

一次性推送全部尚未推送到远程的本地标签

#### 删除远程标签

git  tag  -d  v1.0

先删除本地标签

git  push  origin  :refs/tags/v1.0

从远程删除标签   命令也是 push

#### 小结

- 命令`git push origin <tagname>`可以推送一个本地标签；
- 命令`git push origin --tags`可以推送全部未推送过的本地标签；
- 命令`git tag -d <tagname>`可以删除一个本地标签；
- 命令`git push origin :refs/tags/<tagname>`可以删除一个远程标签。

