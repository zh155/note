# markdown笔记

## markdown标题

使用#号表示1-6号标题，几级标题对应几个#号

## markdown段落

markdown 段落没有特殊的格式，直接编写文字就好，段落的换行是使用两个以上空格加回车

### 字体

```
*斜体文本*
_斜体文本_
**粗体文本**
__粗体文本__
***粗斜体文本***
___粗斜体文本___
```

### 分隔线

你可以在一行中用三个以上的星号、减号、底线来建立一个分隔线，行内不能有其他东西。你也可以在星号或是减号中间插入空格。下面每种写法都可以建立分隔线：

```
***

* * *

*****

- - -

----------
```

### 删除线

如果段落上的文字要添加删除线，只需要在文字的两端加上两个波浪线 **~~** 即可

### 下划线

下划线可以通过html的<u>标签实现

<u>下划线文字</u>

### 脚注

脚注[^脚注]

[^脚注]:脚注是对文本的补充说明

## markdown列表

Markdown 支持有序列表和无序列表。

无序列表使用星号(*****)、加号(**+**)或是减号(**-**)作为列表标记  有序列表使用数字并加上 **.** 号来表示

### 列表嵌套

列表嵌套只需在子列表中的选项添加四个空格即可：

```
1. 第一项：
    - 第一项嵌套的第一个元素
    - 第一项嵌套的第二个元素
2. 第二项：
    - 第二项嵌套的第一个元素
    - 第二项嵌套的第一个元素
```

## markdown区块

Markdown 区块引用是在段落开头使用 **>** 符号 ，然后后面紧跟一个**空格**符号

```
> 区块1
> 区块2
> 区块3
```

> 区块

另外区块是可以嵌套的，一个 **>** 符号是最外层，两个 **>** 符号是第一层嵌套，以此类推退

> 区块1
>
> > 区块2

### 区块中使用列表

```
> 区块中使用列表
> 1. 第一项
> 2. 第二项
> + 第一项
> + 第二项
> + 第三项
```

> 区块中使用列表
>
> 1. 第一项
>
> 2. 第二项
>
> + 第一项
>
> + 第二项

### 列表中使用区块

```
* 第一项
    > 菜鸟教程
    > 学的不仅是技术更是梦想
* 第二项
```

 * 第一项

   > 第一项内容

   

## markdown代码

如果是段落上的一个函数或片段的代码可以用反引号把它包起来（**`**）

` print() ` 函数

### 代码区块

你也可以用 **```** 包裹一段代码，并指定一种语言（也可以不指定）

```
​```javascript
$(document).ready(function () {
    alert('RUNOOB');
});
​```
```

  ```python 
for i in range(10):
    print('hello world')
  ```

## markdown链接

### 链接使用方法

```
[链接名称](链接地址)

或者

<链接地址>
```



[百度](www.baidu.com)

<www.baidu.com>

### 高级链接

```
链接也可以用变量来代替，文档末尾附带变量地址：
这个链接用 1 作为网址变量 [Google][1]
这个链接用 runoob 作为网址变量 [Runoob][runoob]
然后在文档的结尾为变量赋值（网址）

  [1]: http://www.google.com/
  [runoob]: http://www.runoob.com/
```

[百度][baidu]

[baidu]:www.baidu.com

## markdown图片

```
![alt 属性文本](图片地址)

![alt 属性文本](图片地址 "可选标题")
```

```
![RUNOOB 图标](http://static.runoob.com/images/runoob-logo.png)

![RUNOOB 图标](http://static.runoob.com/images/runoob-logo.png "RUNOOB")
```

```
这个链接用 1 作为网址变量 [RUNOOB][1].
然后在文档的结尾位变量赋值（网址）
```

```
[1]: http://static.runoob.com/images/runoob-logo.png
```

