/*
 Navicat Premium Data Transfer

 Source Server         : 175.178.3.27_3306
 Source Server Type    : MySQL
 Source Server Version : 80031 (8.0.31)
 Source Host           : 175.178.3.27:3306
 Source Schema         : brian_blog

 Target Server Type    : MySQL
 Target Server Version : 80031 (8.0.31)
 File Encoding         : 65001

 Date: 03/11/2022 09:49:59
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for art_article
-- ----------------------------
DROP TABLE IF EXISTS `art_article`;
CREATE TABLE `art_article`  (
  `article_id` bigint UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '文章ID',
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '标题',
  `digest` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT '' COMMENT '摘要',
  `cover` char(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'art_default.jpg' COMMENT '封面图',
  `content` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '内容',
  `read_count` int UNSIGNED NOT NULL DEFAULT 0 COMMENT '阅读量',
  `comment_count` int UNSIGNED NOT NULL DEFAULT 0 COMMENT '评论量',
  `category_id` int UNSIGNED NULL DEFAULT NULL COMMENT '分类',
  `author_id` int NOT NULL COMMENT '作者',
  `is_delete` tinyint(1) NOT NULL DEFAULT 0 COMMENT '逻辑删除',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `update_time` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`article_id`) USING BTREE,
  UNIQUE INDEX `title`(`title` ASC) USING BTREE,
  INDEX `category_id`(`category_id` ASC) USING BTREE,
  INDEX `author_id`(`author_id` ASC) USING BTREE,
  CONSTRAINT `author_id` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `category_id` FOREIGN KEY (`category_id`) REFERENCES `art_category` (`category_id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of art_article
-- ----------------------------
INSERT INTO `art_article` VALUES (1, 'Xadmin2.0(for Django2.0) 基本设置', '使用 Xadmin 您只需定义您数据的字段等信息，即可即刻获得一个功能全面的管理系统。不仅如此，您还可以方便的扩展更多的定制功能和系统界面。', 'art_default.jpg', '<p><strong>目录[-]</strong></p>\r\n\r\n<ul>\r\n	<li><a href=\"http://127.0.0.1:8001/blog/detail/13/#wow0\" title=\"\">一、安装</a></li>\r\n	<li><a href=\"http://127.0.0.1:8001/blog/detail/13/#wow1\">models注册</a></li>\r\n	<li><a href=\"http://127.0.0.1:8001/blog/detail/13/#wow2\">二、基本设置</a></li>\r\n	<li><a href=\"http://127.0.0.1:8001/blog/detail/13/#wow3\">补充</a></li>\r\n</ul>\r\n\r\n<h2>一、安装</h2>\r\n\r\n<ul>\r\n	<li>使用安装工具安装：</li>\r\n</ul>\r\n\r\n<pre>\r\npip install git+git://github.com/sshwsfc/xadmin.git@django2\r\n</pre>\r\n\r\n<ul>\r\n	<li>下载源码：</li>\r\n</ul>\r\n\r\n<pre>\r\ngit clone https://github.com/sshwsfc/xadmin.git\r\n</pre>\r\n\r\n<p>或者将文件夹中的xadmin文件夹，放到项目目录中，然后在setting.py中添加应用路径并注册app * 修改路由urls.py：</p>\r\n\r\n<pre>\r\nfrom django.urls import path\r\nimport xadmin\r\n\r\nurlpatterns = [\r\n    path(&#39;admin/&#39;, xadmin.site.urls),\r\n    ]\r\n</pre>\r\n\r\n<h2>models注册</h2>\r\n\r\n<ul>\r\n	<li>在应用文件目录下新建adminx.py文件</li>\r\n</ul>\r\n\r\n<pre>\r\n#!/usr/bin/env python3\r\n# -*- coding: utf-8 -*-\r\n__author__ = &quot;问道编程&quot;\r\n__date__ = &quot;5/29/18 10:41&quot;\r\n\r\nimport xadmin\r\n\r\nfrom .models import EmailVerification\r\n\r\nclass EmailVerificationAdmin:    # Python2 需要继承object类\r\n    &quot;&quot;&quot;邮箱验证后台管理&quot;&quot;&quot;\r\n    list_display = [&#39;email&#39;, &#39;code&#39;, &#39;send_type&#39;, &#39;send_time&#39;, &#39;is_delete&#39;]\r\n    list_filter = [&#39;email&#39;, &#39;code&#39;, &#39;send_type&#39;]\r\n    search_fields = [&#39;email&#39;, &#39;code&#39;, &#39;send_type&#39;, &#39;send_time&#39;, &#39;is_delete&#39;]\r\n    fields = [&#39;send_type&#39;, &#39;email&#39;, &#39;code&#39;, &#39;is_delete&#39;]\r\n\r\nxadmin.site.register(EmailVerification, EmailVerificationAdmin)\r\n</pre>\r\n\r\n<p>需要注意的是：xadmin默认注册user类（可在xadmin/adminx.py中查看），项目创建超级用户，登录127.0.0.1:8000/admin（或者其他IP/admin）。</p>\r\n\r\n<h2>二、基本设置</h2>\r\n\r\n<ul>\r\n	<li>整个界面主题设置 在其中一个应用的adminx.py中添加：</li>\r\n</ul>\r\n\r\n<pre>\r\nfrom xadmin import views\r\n\r\nclass BaseSetting:     \r\n    enable_themes = True  # 开启主题功能\r\n    use_bootswatch = True\r\n\r\nxadmin.site.register(views.BaseAdminView, BaseSetting)\r\n</pre>\r\n\r\n<p>刷新后端管理页面后，右上角增加了主题标签，点击主题标签，可以选择喜欢的主题样式。</p>\r\n\r\n<ul>\r\n	<li>左上角名称(Django Xadmin)、底部(我的公司)修改、左侧菜单栏折叠</li>\r\n</ul>\r\n\r\n<pre>\r\nclass GlobalSettings:\r\n    &quot;&quot;&quot;\r\n    后台修改\r\n    &quot;&quot;&quot;\r\n    site_title = &#39;修改后的名称&#39;\r\n    site_footer = &#39;修改后的底部&#39;\r\n    menu_style = &#39;accordion&#39;  # 开启分组折叠\r\n\r\nxadmin.site.register(views.CommAdminView, GlobalSettings)\r\n</pre>\r\n\r\n<p>刷新后台管理页面可以发现页面左上角、底部均已修改，且左侧菜单栏可折叠</p>\r\n\r\n<ul>\r\n	<li>左侧apps中文显示 首先在应用目录下，修改apps.py文件为：</li>\r\n</ul>\r\n\r\n<pre>\r\n# _*_ coding:utf-8 _*_\r\nfrom django.apps import AppConfig\r\n\r\n\r\nclass CoursesConfig(AppConfig):\r\n    name = &#39;courses&#39;\r\n    verbose_name = &#39;课程管理&#39;\r\n</pre>\r\n\r\n<p>让后修改__init__.py文件为：</p>\r\n\r\n<pre>\r\ndefault_app_config = &#39;courses.apps.CoursesConfig&#39;\r\n</pre>\r\n\r\n<p>刷新页面，显示中文。</p>\r\n\r\n<h2>补充</h2>\r\n\r\n<ul>\r\n	<li>如果models类显示英文，需要在models.py中类添加：</li>\r\n</ul>\r\n\r\n<pre>\r\nclass Meta:\r\n    verbose_name = &#39;邮箱验证信息&#39;\r\n    verbose_name_plural = verbose_name\r\n\r\ndef __str__(self):    # Python3 使用\r\n    return self.email\r\n\r\ndef __unicode(self):   # Python2 使用\r\n    return self.email\r\n</pre>\r\n\r\n<ul>\r\n	<li>左侧每个models图标设置</li>\r\n</ul>\r\n\r\n<p>左侧菜单栏中，xadmin自动注册的models在左侧有小图标，那么我们自己注册的models小图标如何修改呢？</p>\r\n\r\n<p>首先找到xadmin存放图标icon的文件:</p>\r\n\r\n<p>xadmin/static/vendor/font-awesome/css/font-awesome.css文件设定图标样式</p>\r\n\r\n<p>xadmin/static/vendor/font-awesome/fonts文件夹存放图标的其他设置</p>\r\n\r\n<p>打开font-awesome.css可以看到文件版本（一般默认都是比较早的版本）</p>\r\n\r\n<p>然后登录http://www.fontawesome.com.cn/网站下载最新版，解压后，将css和fonts两个文件夹复制到xadmin/static/vendor/font-awesome/，替换之前的文件夹</p>', 8, 0, 1, 1, 0, '2022-09-13 22:46:15', '2022-10-19 07:36:37');
INSERT INTO `art_article` VALUES (2, 'Python中对闭包、装饰器的基本理解', '<p>闭包(closure)是函数式编程的重要的语法结构。闭包也是一种组织代码的结构，它同样提高了代码的可重复使用性。如果在一个内嵌函数里，对在外部函数内（但不是在全局作用域）的变量进行引用，那么内嵌函数就被认为是闭包(closure)。定义在外部函数内但由内部函数引用或者使用的变量称为自由变量。</p>', 'Fi8aCbWK2OWiwitLxgleYBcOi9os', '<h2>一、闭包</h2>\r\n\r\n<p>​ 首先理解下python中的函数，在python中，函数是一个对象（可以通过type函数查看），在内存中占用空间；函数执行完成之后内部的变量会被解释器回收，但是如果某变量被返回，则不会回收，因为引用计数器的值不为0；既然函数也是一个对象，他也拥有自己的属性；对于python函数来说，返回的不一定是变量，也可以是函数。</p>\r\n\r\n<p>​ 由此引出闭包的概念，当存在函数嵌套时（如上例中的func()和in_func()就是嵌套关系），外部函数的返回值为内部函数，且内部函数引用外部函数的变量、参数，并将引用的变量、参数封装在函数中一起作为返回值，其中的内部函数就称为一个闭包。</p>\r\n\r\n<p>​ 形成闭包的必要条件：</p>\r\n\r\n<p>1)必须有一个内嵌函数(函数里定义的函数）&mdash;&mdash;这对应函数之间的嵌套</p>\r\n\r\n<p>2)内嵌函数必须引用一个定义在闭合范围内(外部函数里)的变量&mdash;&mdash;内部函数引用外部变量</p>\r\n\r\n<p>3)外部函数必须返回内嵌函数&mdash;&mdash;必须返回那个内部函数</p>\r\n\r\n<h2>二、闭包的使用场景</h2>\r\n\r\n<p>第一个例子：</p>\r\n\r\n<pre>\r\n<code class=\"language-python\">#!/usr/bin/env python3\r\n# -*- coding: utf-8 -*-\r\n__author__ = \"问道编程\"\r\n__date__ = \"2018-06-13 15:53\"\r\n\r\ndef funx():\r\n    x=5   # 对于funx，是L作用域，对于funy，是E作用域\r\n    def funy():    # 是一个闭包\r\n        nonlocal x  # 绑定到外部的x，只在python3中使用\r\n        x+=1\r\n        return x\r\n    return funy\r\n\r\na = funx()\r\nprint(a())\r\nprint(a())\r\nprint(a())\r\nprint(x)\r\n-------------------------\r\n6\r\n7\r\n8\r\nNameError: name \'x\' is not defined\r\n</code></pre>\r\n\r\n<p>​ 本来x只是funx()的局部变量，但是形成了闭包之后，它的行为就好像是一个全局变量一样，最后的错误说明x并不是一个全局变量。其实这就是闭包的一个十分浅显的作用，形成闭包之后，闭包变量能够随着闭包函数的调用而实时更新，就好像是一个全局变量那样。 第二个例子，也是讲闭包用的最多的例子：</p>\r\n\r\n<pre>\r\n<code class=\"language-python\">def func_150(val):   # 总分为150时，及格分数为90\r\n    passline = 90\r\n    if val &gt;= passline:\r\n        print \"pass\"\r\n    else:\r\n        print \"fail\"\r\n\r\ndef func_100(val):   # 总分为100时，及格分数为60\r\n    passline = 60 \r\n    if val &gt;= passline:\r\n        print \"pass\"\r\n    else:\r\n        print \"fail\"\r\n\r\nfunc_100(89)  \r\nfunc_150(89)\r\n\r\n# 使用闭包优化上面的代码：\r\n\r\ndef set_passline(passline):\r\n    def cmp(val):\r\n        if val &gt;= passline:\r\n            print \"pass\"\r\n        else:\r\n            print \"fail\"\r\n    return cmp\r\n\r\nf_100 = set_passline(60)    # f_100调用函数set_passline()，并将60赋值给变量passline,这是f_100等于函数的返回值，也就是函数cmp\r\nf_150 = set_passline(90)\r\nf_100(89)     # f_100()=cmp(),将89赋值给val，运行cmp()函数，输出结果\r\nf_150(89)\r\n</code></pre>\r\n\r\n<p>第三个例子：</p>\r\n\r\n<pre>\r\n<code class=\"language-python\">def my_sum(*arg):\r\n    print(\'in my_sum,arg=\',arg)\r\n    return sum(arg)\r\n\r\n\r\ndef dec(func):\r\n    def in_dec(*arg):\r\n        print(\'in in_dec,arg=\', arg)\r\n        if len(arg) == 0:\r\n            return 0\r\n        for val in arg:\r\n            if not isinstance(val, int):\r\n                return 0\r\n        return func(*arg)\r\n\r\n    return in_dec\r\n\r\n\r\nmy_sums = dec(my_sum)  # 命名为my_sums，是为了和my_sum进行区分，便于理解\r\n# ①调用dec()函数，将dec的返回值赋值给my_sums，相当于my_sums=in_dec，②将函数my_sum赋值给func，相当于func=my_sum\r\nresult = my_sums(1, 2, 3, 4, 5)  \r\n# ③相当于将(1, 2, 3, 4, 5)赋值给in_dec函数中的arg，调用并执行函数in_dec()，\r\n# ④in_dec()函数的return返回值是func()函数，将in_dec函数中的arg赋值给func()函数中的arg,也就是赋值给my_sum()中的arg\r\n# ⑤调用并执行函数my_sum()，将sum(arg)结果返回给变量result\r\nprint(result)\r\n------------\r\nin in_dec,arg= (1, 2, 3, 4, 5)\r\nin my_sum,arg= (1, 2, 3, 4, 5)\r\n15\r\n</code></pre>\r\n\r\n<p>​ 整个过程可以简单的理解为，先运行dec()函数，其返回值是in_dec函数，再运行in_dec函数，其返回值为func函数，也就是my_sum函数，再运行my_sum函数dec() -&gt; in_dec() -&gt; my_sum()</p>\r\n\r\n<p>第四个例子：</p>\r\n\r\n<pre>\r\n<code class=\"language-python\">#!/usr/bin/env python3\r\n# -*- coding: utf-8 -*-\r\n__author__ = \"问道编程\"\r\n__date__ = \"2018-06-13 17:08\"\r\n\r\nvariable = 300\r\n\r\ndef test_scopt():\r\n    print(variable)  # variable是test_scopt()的局部变量，但是在打印时并没有绑定内存对象。\r\n    variable = 200  # 因为这里，所以variable就变为了局部变量\r\n\r\ntest_scopt()\r\nprint(variable)\r\n------------\r\nUnboundLocalError: local variable \'variable\' referenced before assignment\r\n</code></pre>\r\n\r\n<p>上面的例子会报出错误，因为在执行程序时的预编译能够在test_scopt()中找到局部变量variable(对variable进行了赋值)。在局部作用域找到了变量名，所以不会升级到嵌套作用域去寻找。但是在使用print语句将变量variable打印时，局部变量variable并有没绑定到一个内存对象(没有定义和初始化，即没有赋值)。本质上还是Python调用变量时遵循的LEGB法则和Python解析器的编译原理，决定了这个错误的发生。所以，在调用一个变量之前，需要为该变量赋值(绑定一个内存对象)。</p>\r\n\r\n<p>注意：为什么在这个例子中触发的错误是UnboundLocalError而不是NameError：name &lsquo;variable&rsquo; is not defined。因为变量variable不在全局作用域。Python中的模块代码在执行之前，并不会经过预编译，但是模块内的函数体代码在运行前会经过预编译，因此不管变量名的绑定发生在作用域的那个位置，都能被编译器知道。Python虽然是一个静态作用域语言，但变量名查找是动态发生的，直到在程序运行时，才会发现作用域方面的问题</p>\r\n\r\n<p>可以使用global将变量variable声明为全局变量。</p>\r\n\r\n<h2>三、装饰器</h2>\r\n\r\n<p>概念性的知识，拗口的表述： 1.装饰器就是对闭包的使用； 2.装饰器的作用是装饰函数； 3.装饰器会返回一个函数对象，被装饰的函数接收； 4.被装饰函数标识符指向返回的函数对象。</p>\r\n\r\n<p>将上面第三个例子用上装饰器：</p>\r\n\r\n<pre>\r\n<code class=\"language-python\">def dec(func):\r\n    def in_dec(*arg):\r\n        print(\'in in_dec,arg=\', arg)\r\n        if len(arg) == 0:\r\n            return 0\r\n        for val in arg:\r\n            if not isinstance(val, int):\r\n                return 0\r\n        return func(*arg)\r\n　　 print(\'in dec\')  # 新增的一行\r\n    return in_dec\r\n@dec \r\ndef my_sum(*arg):\r\n    print(\'in my_sum,arg=\',arg)\r\n    return sum(arg)\r\nprint(type(my_sum))\r\n</code></pre>\r\n\r\n<p>对概念的实例化：</p>\r\n\r\n<p>1、@dec是一个装饰器，是调用dec()函数形成的装饰器；</p>\r\n\r\n<p>2、被装饰的函数是my_sum()，即调用dec()函数形成装饰器时，dec()函数的参数为my_sum()函数，即：func = my_sum</p>\r\n\r\n<p>3、装饰器的返回值是函数in_dec()，该返回值被函数my_sum()接收，其实是传给被装饰函数（即my_sum()函数）的标识符my_sum，即：my_sum=in_dec</p>\r\n\r\n<p>直接运行该文件，输出：</p>\r\n\r\n<pre>\r\n<code class=\"language-bash\">--------------\r\nin dec\r\n&lt;class \'function\'&gt;     # 此时的my_sum并非指定义的def my_sum(*arg)函数，而是变成接收了装饰器的返回值，in_dec函数。\r\n</code></pre>\r\n\r\n<p>说明只要使用了装饰器，就会调用装饰器里的函数；并且装饰器的返回值：in_dec()，被my_sum接收（如果没有return in_dec，直接运行，则my_sum格式为：，说明装饰器没有返回值时，会返回None，这一点跟函数一样）。</p>\r\n\r\n<p>接下来，执行语句：</p>\r\n\r\n<pre>\r\n<code class=\"language-python\">result = my_sum(1, 2, 3, 4, 5)  \r\nprint(result)\r\n------------------\r\nin dec\r\n&lt;class \'function\'&gt;\r\nin in_dec,arg= (1, 2, 3, 4, 5)\r\nin my_sum,arg= (1, 2, 3, 4, 5)\r\n15\r\n</code></pre>\r\n\r\n<p>运行过程为（结合第三个例子进行理解）：</p>\r\n\r\n<p>1、@dec，调用dec函数，其参数就是被装饰的函数my_sum()，即func=my_sum，执行print(&#39;in dec&#39;)，返回in_dec函数，被my_sum接收，即：最后会将函数in_dec的运行结果，传给被装饰函数的标识符my_sum；</p>\r\n\r\n<p>2、调用in_dec函数，参数为(1,2,3,4,5)，执行print、if、for语句，执行return func(*arg)，func=my_sum函数；</p>\r\n\r\n<p>3、调用函数my_sum()，参数为(1,2,3,4,5)，执行print语句，执行return sum(*arg)，返回最终结果；</p>', 4, 3, 1, 1, 0, '2022-09-13 23:06:41', '2022-10-20 20:17:17');
INSERT INTO `art_article` VALUES (3, '# 更新全部         queryset = ArticleInfo.get_all()         writer = init_ix(schema=ArticleSchema(), indexname=INDEX_NAME).writer()#', '<pre>\r\n# 更新全部\r\nqueryset = ArticleInfo.get_all()\r\nwriter = init_ix(schema=ArticleSchema(), indexname=INDEX_NAME).writer()</pre>\r\n\r\n<pre>\r\n# 更新全部\r\nqueryset = ArticleInfo.get_all()\r\nwriter = init_ix(schema=ArticleSchema(), indexname=INDEX_NAME).writer()</pre>', 'art_default.jpg', '<pre>\r\n# 更新全部\r\nqueryset = ArticleInfo.get_all()\r\nwriter = init_ix(schema=ArticleSchema(), indexname=INDEX_NAME).writer()</pre>\r\n\r\n<pre>\r\n# 更新全部\r\nqueryset = ArticleInfo.get_all()\r\nwriter = init_ix(schema=ArticleSchema(), indexname=INDEX_NAME).writer()</pre>\r\n\r\n<pre>\r\n# 更新全部\r\nqueryset = ArticleInfo.get_all()\r\nwriter = init_ix(schema=ArticleSchema(), indexname=INDEX_NAME).writer()</pre>\r\n\r\n<pre>\r\n# 更新全部\r\nqueryset = ArticleInfo.get_all()\r\nwriter = init_ix(schema=ArticleSchema(), indexname=INDEX_NAME).writer()</pre>', 0, 0, 1, 1, 0, '2022-10-19 08:14:09', '2022-10-19 08:14:09');
INSERT INTO `art_article` VALUES (4, '# TODO 当用户保存数据时添加author 更新全部  为当前用户!', '<pre>\r\n# TODO 当用户保存数据时添加author为当前用户!\r\n</pre>', 'art_default.jpg', '<pre>\r\n# TODO 当用户保存数据时添加author为当前用户!\r\n</pre>\r\n\r\n<pre>\r\n# TODO 当用户保存数据时添加author为当前用户!\r\n</pre>\r\n\r\n<pre>\r\n# TODO 当用户保存数据时添加author为当前用户!\r\n</pre>', 0, 0, 2, 16, 0, '2022-10-19 08:39:24', '2022-10-20 00:42:05');

-- ----------------------------
-- Table structure for art_article_tag
-- ----------------------------
DROP TABLE IF EXISTS `art_article_tag`;
CREATE TABLE `art_article_tag`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `article_id` bigint UNSIGNED NOT NULL,
  `tag_id` int UNSIGNED NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `article_id`(`article_id` ASC) USING BTREE,
  INDEX `tag_id`(`tag_id` ASC) USING BTREE,
  CONSTRAINT `article_id` FOREIGN KEY (`article_id`) REFERENCES `art_article` (`article_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `tag_id` FOREIGN KEY (`tag_id`) REFERENCES `art_tag` (`tag_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of art_article_tag
-- ----------------------------
INSERT INTO `art_article_tag` VALUES (1, 1, 1);
INSERT INTO `art_article_tag` VALUES (2, 2, 1);
INSERT INTO `art_article_tag` VALUES (3, 2, 2);
INSERT INTO `art_article_tag` VALUES (4, 3, 2);
INSERT INTO `art_article_tag` VALUES (5, 4, 2);

-- ----------------------------
-- Table structure for art_category
-- ----------------------------
DROP TABLE IF EXISTS `art_category`;
CREATE TABLE `art_category`  (
  `category_id` int UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '分类ID',
  `name` char(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '分类名称',
  `is_delete` tinyint(1) NOT NULL DEFAULT 0 COMMENT '逻辑删除',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `update_time` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`category_id`) USING BTREE,
  UNIQUE INDEX `name`(`name` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of art_category
-- ----------------------------
INSERT INTO `art_category` VALUES (1, 'Python', 0, '2022-09-13 22:43:38', '2022-09-17 16:55:20');
INSERT INTO `art_category` VALUES (2, 'Djagno', 0, '2022-09-13 23:15:06', '2022-10-09 04:19:30');
INSERT INTO `art_category` VALUES (3, 'web前端', 0, '2022-09-17 16:56:01', '2022-09-17 16:56:04');

-- ----------------------------
-- Table structure for art_recommend
-- ----------------------------
DROP TABLE IF EXISTS `art_recommend`;
CREATE TABLE `art_recommend`  (
  `recommend_id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `article_id` bigint UNSIGNED NOT NULL,
  `is_delete` tinyint(1) NOT NULL DEFAULT 0 COMMENT '逻辑删除',
  PRIMARY KEY (`recommend_id`) USING BTREE,
  INDEX `art_recommend_ibfk_1`(`article_id` ASC) USING BTREE,
  CONSTRAINT `art_recommend_ibfk_1` FOREIGN KEY (`article_id`) REFERENCES `art_article` (`article_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of art_recommend
-- ----------------------------
INSERT INTO `art_recommend` VALUES (1, 1, 0);
INSERT INTO `art_recommend` VALUES (2, 2, 0);

-- ----------------------------
-- Table structure for art_tag
-- ----------------------------
DROP TABLE IF EXISTS `art_tag`;
CREATE TABLE `art_tag`  (
  `tag_id` int UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '标签ID',
  `name` char(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '标签名称',
  `is_delete` tinyint(1) NOT NULL DEFAULT 0 COMMENT '逻辑删除',
  PRIMARY KEY (`tag_id`) USING BTREE,
  UNIQUE INDEX `name`(`name` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of art_tag
-- ----------------------------
INSERT INTO `art_tag` VALUES (1, '开发', 0);
INSERT INTO `art_tag` VALUES (2, '软件分享', 0);
INSERT INTO `art_tag` VALUES (3, '中国人民出版社1', 0);

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_group
-- ----------------------------
INSERT INTO `auth_group` VALUES (1, '普通用户');
INSERT INTO `auth_group` VALUES (2, '管理层');

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id` ASC, `permission_id` ASC) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id` ASC) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------
INSERT INTO `auth_group_permissions` VALUES (7, 1, 25);
INSERT INTO `auth_group_permissions` VALUES (8, 1, 26);
INSERT INTO `auth_group_permissions` VALUES (9, 1, 27);
INSERT INTO `auth_group_permissions` VALUES (10, 1, 28);
INSERT INTO `auth_group_permissions` VALUES (1, 1, 36);
INSERT INTO `auth_group_permissions` VALUES (2, 1, 37);
INSERT INTO `auth_group_permissions` VALUES (3, 1, 48);
INSERT INTO `auth_group_permissions` VALUES (4, 1, 52);
INSERT INTO `auth_group_permissions` VALUES (5, 1, 54);
INSERT INTO `auth_group_permissions` VALUES (6, 1, 56);

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id` ASC, `codename` ASC) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 57 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add content type', 4, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (14, 'Can change content type', 4, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (15, 'Can delete content type', 4, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (16, 'Can view content type', 4, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (17, 'Can add session', 5, 'add_session');
INSERT INTO `auth_permission` VALUES (18, 'Can change session', 5, 'change_session');
INSERT INTO `auth_permission` VALUES (19, 'Can delete session', 5, 'delete_session');
INSERT INTO `auth_permission` VALUES (20, 'Can view session', 5, 'view_session');
INSERT INTO `auth_permission` VALUES (21, 'Can add art article tag', 6, 'add_artarticletag');
INSERT INTO `auth_permission` VALUES (22, 'Can change art article tag', 6, 'change_artarticletag');
INSERT INTO `auth_permission` VALUES (23, 'Can delete art article tag', 6, 'delete_artarticletag');
INSERT INTO `auth_permission` VALUES (24, 'Can view art article tag', 6, 'view_artarticletag');
INSERT INTO `auth_permission` VALUES (25, 'Can add 文章', 7, 'add_article');
INSERT INTO `auth_permission` VALUES (26, 'Can change 文章', 7, 'change_article');
INSERT INTO `auth_permission` VALUES (27, 'Can delete 文章', 7, 'delete_article');
INSERT INTO `auth_permission` VALUES (28, 'Can view 文章', 7, 'view_article');
INSERT INTO `auth_permission` VALUES (29, 'Can add 分类', 8, 'add_category');
INSERT INTO `auth_permission` VALUES (30, 'Can change 分类', 8, 'change_category');
INSERT INTO `auth_permission` VALUES (31, 'Can delete 分类', 8, 'delete_category');
INSERT INTO `auth_permission` VALUES (32, 'Can view 分类', 8, 'view_category');
INSERT INTO `auth_permission` VALUES (33, 'Can add 友情链接', 9, 'add_link');
INSERT INTO `auth_permission` VALUES (34, 'Can change 友情链接', 9, 'change_link');
INSERT INTO `auth_permission` VALUES (35, 'Can delete 友情链接', 9, 'delete_link');
INSERT INTO `auth_permission` VALUES (36, 'Can view 友情链接', 9, 'view_link');
INSERT INTO `auth_permission` VALUES (37, 'Can add 流动消息', 10, 'add_notice');
INSERT INTO `auth_permission` VALUES (38, 'Can change 流动消息', 10, 'change_notice');
INSERT INTO `auth_permission` VALUES (39, 'Can delete 流动消息', 10, 'delete_notice');
INSERT INTO `auth_permission` VALUES (40, 'Can view 流动消息', 10, 'view_notice');
INSERT INTO `auth_permission` VALUES (41, 'Can add 推荐文章', 11, 'add_recommend');
INSERT INTO `auth_permission` VALUES (42, 'Can change 推荐文章', 11, 'change_recommend');
INSERT INTO `auth_permission` VALUES (43, 'Can delete 推荐文章', 11, 'delete_recommend');
INSERT INTO `auth_permission` VALUES (44, 'Can view 推荐文章', 11, 'view_recommend');
INSERT INTO `auth_permission` VALUES (45, 'Can add 轮播图', 12, 'add_slideshow');
INSERT INTO `auth_permission` VALUES (46, 'Can change 轮播图', 12, 'change_slideshow');
INSERT INTO `auth_permission` VALUES (47, 'Can delete 轮播图', 12, 'delete_slideshow');
INSERT INTO `auth_permission` VALUES (48, 'Can view 轮播图', 12, 'view_slideshow');
INSERT INTO `auth_permission` VALUES (49, 'Can add 标签', 13, 'add_tag');
INSERT INTO `auth_permission` VALUES (50, 'Can change 标签', 13, 'change_tag');
INSERT INTO `auth_permission` VALUES (51, 'Can delete 标签', 13, 'delete_tag');
INSERT INTO `auth_permission` VALUES (52, 'Can view 标签', 13, 'view_tag');
INSERT INTO `auth_permission` VALUES (53, 'Can add 用户', 14, 'add_user');
INSERT INTO `auth_permission` VALUES (54, 'Can change 用户', 14, 'change_user');
INSERT INTO `auth_permission` VALUES (55, 'Can delete 用户', 14, 'delete_user');
INSERT INTO `auth_permission` VALUES (56, 'Can view 用户', 14, 'view_user');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `first_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL DEFAULT 0 COMMENT '逻辑删除',
  `phone` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT '' COMMENT '手机号',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES (1, 'pbkdf2_sha256$260000$bvzHmseQmFwWzbMSutz1cP$2lDFJahNe5uHKZ1GB0dtpJN8IPDUh6zZe63GoMaPv4A=', '2022-11-03 09:48:00.992894', 1, 'brian', '', '', 'chengrip@foxemail.com', 1, 1, '2022-09-22 19:18:45.263961', 0, NULL);
INSERT INTO `auth_user` VALUES (2, 'pbkdf2_sha256$260000$IPNV3hHCPT6v01ykSqB2jW$8gXYYDLpx8EQhpWXcUSPvG+DvFl+i4A++XaFpljLmsI=', '2022-11-01 04:28:07.303691', 0, 'brianf', '', '', '1677880403@qq.com', 1, 1, '2022-11-01 01:01:00.000000', 0, NULL);

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id` ASC, `group_id` ASC) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id`(`group_id` ASC) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------
INSERT INTO `auth_user_groups` VALUES (1, 2, 1);

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id` ASC, `permission_id` ASC) USING BTREE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`(`permission_id` ASC) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `content_type_id` int NULL DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id` ASC) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id`(`user_id` ASC) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_chk_1` CHECK (`action_flag` >= 0)
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES (1, '2022-11-01 04:23:05.594479', '1', '普通用户', 2, '[{\"changed\": {\"fields\": [\"Permissions\"]}}]', 3, 1);
INSERT INTO `django_admin_log` VALUES (2, '2022-11-01 04:27:50.478669', '16', 'brianf', 2, '[{\"changed\": {\"fields\": [\"Groups\", \"Last login\"]}}]', 14, 1);

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label` ASC, `model` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 15 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (6, 'blog', 'artarticletag');
INSERT INTO `django_content_type` VALUES (7, 'blog', 'article');
INSERT INTO `django_content_type` VALUES (8, 'blog', 'category');
INSERT INTO `django_content_type` VALUES (9, 'blog', 'link');
INSERT INTO `django_content_type` VALUES (10, 'blog', 'notice');
INSERT INTO `django_content_type` VALUES (11, 'blog', 'recommend');
INSERT INTO `django_content_type` VALUES (12, 'blog', 'slideshow');
INSERT INTO `django_content_type` VALUES (13, 'blog', 'tag');
INSERT INTO `django_content_type` VALUES (14, 'blog', 'user');
INSERT INTO `django_content_type` VALUES (4, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (5, 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 20 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2022-11-01 04:11:59.451009');
INSERT INTO `django_migrations` VALUES (2, 'contenttypes', '0002_remove_content_type_name', '2022-11-01 04:11:59.572076');
INSERT INTO `django_migrations` VALUES (3, 'auth', '0001_initial', '2022-11-01 04:12:00.220333');
INSERT INTO `django_migrations` VALUES (4, 'auth', '0002_alter_permission_name_max_length', '2022-11-01 04:12:00.345523');
INSERT INTO `django_migrations` VALUES (5, 'auth', '0003_alter_user_email_max_length', '2022-11-01 04:12:00.360796');
INSERT INTO `django_migrations` VALUES (6, 'auth', '0004_alter_user_username_opts', '2022-11-01 04:12:00.401558');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0005_alter_user_last_login_null', '2022-11-01 04:12:00.413692');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0006_require_contenttypes_0002', '2022-11-01 04:12:00.421512');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0007_alter_validators_add_error_messages', '2022-11-01 04:12:00.436177');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0008_alter_user_username_max_length', '2022-11-01 04:12:00.445117');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0009_alter_user_last_name_max_length', '2022-11-01 04:12:00.457782');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0010_alter_group_name_max_length', '2022-11-01 04:12:00.482817');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0011_update_proxy_permissions', '2022-11-01 04:12:00.495145');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0012_alter_user_first_name_max_length', '2022-11-01 04:12:00.507216');
INSERT INTO `django_migrations` VALUES (15, 'blog', '0001_initial', '2022-11-01 04:12:01.186629');
INSERT INTO `django_migrations` VALUES (16, 'admin', '0001_initial', '2022-11-01 04:12:01.481001');
INSERT INTO `django_migrations` VALUES (17, 'admin', '0002_logentry_remove_auto_add', '2022-11-01 04:12:01.496675');
INSERT INTO `django_migrations` VALUES (18, 'admin', '0003_logentry_add_action_flag_choices', '2022-11-01 04:12:01.510764');
INSERT INTO `django_migrations` VALUES (19, 'sessions', '0001_initial', '2022-11-01 04:12:01.602252');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_session
-- ----------------------------

-- ----------------------------
-- Table structure for home_link
-- ----------------------------
DROP TABLE IF EXISTS `home_link`;
CREATE TABLE `home_link`  (
  `link_id` int UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '友情链接ID',
  `name` char(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '链接名称',
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '标题',
  `url` tinytext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '链接地址',
  `is_delete` tinyint(1) NOT NULL DEFAULT 0 COMMENT '逻辑删除',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `update_time` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`link_id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 5 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of home_link
-- ----------------------------
INSERT INTO `home_link` VALUES (1, '百度', NULL, 'http://baidu.com/', 1, '2022-09-13 22:43:56', '2022-09-13 23:13:56');
INSERT INTO `home_link` VALUES (2, '腾讯', NULL, 'https://www.qq.com/', 0, '2022-09-13 23:15:38', '2022-09-13 23:16:20');
INSERT INTO `home_link` VALUES (3, '大鱼的鱼塘', '大鱼的鱼塘 - 一个总会有收获的地方', 'http://brucedone.com', 0, '2022-09-14 21:15:11', '2022-09-14 21:15:11');
INSERT INTO `home_link` VALUES (4, '灯塔水母', '', 'http://www.songluyi.com/', 0, '2022-09-14 21:15:53', '2022-09-14 21:15:53');

-- ----------------------------
-- Table structure for home_notice
-- ----------------------------
DROP TABLE IF EXISTS `home_notice`;
CREATE TABLE `home_notice`  (
  `notice_id` int UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '滚动消息ID',
  `content` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `update_time` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  `is_delete` tinyint NOT NULL DEFAULT 0 COMMENT '逻辑删除',
  PRIMARY KEY (`notice_id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of home_notice
-- ----------------------------
INSERT INTO `home_notice` VALUES (1, '人生苦短，我用python', '2022-09-15 15:01:27', '2022-09-15 15:01:27', 0);
INSERT INTO `home_notice` VALUES (2, 'Life is short, you need Python!', '2022-09-15 15:02:32', '2022-09-15 15:02:32', 0);
INSERT INTO `home_notice` VALUES (3, 'PHP 是WEB编程的最佳语言!', '2022-09-15 15:04:24', '2022-09-15 15:05:26', 0);

-- ----------------------------
-- Table structure for home_slideshow
-- ----------------------------
DROP TABLE IF EXISTS `home_slideshow`;
CREATE TABLE `home_slideshow`  (
  `slideshow_id` int UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '轮播图ID',
  `title` char(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT '' COMMENT '标题',
  `image` char(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '图片',
  `url` varchar(2048) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT 'http://www.baidu.com' COMMENT '链接',
  `is_delete` tinyint(1) NOT NULL DEFAULT 0 COMMENT '逻辑删除',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `update_time` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  `brief` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '简介',
  PRIMARY KEY (`slideshow_id`) USING BTREE,
  UNIQUE INDEX `title`(`title`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 5 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of home_slideshow
-- ----------------------------
INSERT INTO `home_slideshow` VALUES (2, 'Brian Griffin', 'FkATDUlUtlXEzy20q0LAZ8xOdlA4', 'https://www.youtube.com/watch?v=p2xqEx2O15Y', 0, '2022-09-15 18:13:54', '2022-10-21 04:38:37', '布赖恩·格里芬（英语：Brian Griffin）是美国喜剧动画《居家男人》角色。一个拟人化的狗，由塞思·麦克法兰配音，本作的主角和格里芬家庭中的一员。他是陷入困境的作家，试图以散文、小说、剧本和报纸上的文章来挽回声誉。');
INSERT INTO `home_slideshow` VALUES (1, '娜塔莎·罗曼诺夫', 'FqJGGqXeuoVkvIcfKB5zcY8Xt1cc', 'https://zh.wikipedia.org/wiki/%E9%BB%91%E5%AF%A1%E5%A9%A6_(%E9%9B%BB%E5%BD%B1)', 0, '2022-09-15 17:46:45', '2022-10-21 04:36:58', '娜塔莎·罗曼诺夫从2010年电影《钢铁侠2》被引入到漫威电影宇宙系列中，并成为核心角色且出现在随后的九部电影里。 这个角色在2021年电影《黑寡妇》中最后登场。');
INSERT INTO `home_slideshow` VALUES (3, 'Brian Griffin2', 'Fk3sm2FE9-gHcrsY1f9Ib-5M7bgz', 'https://www.youtube.com/watch?v=p2xqEx2O15Y', 1, '2022-09-22 20:25:34', '2022-10-20 20:01:04', '');
INSERT INTO `home_slideshow` VALUES (4, '奥黛丽·赫本', 'FnxBI9zPOUBkVWymSm87L7LoFdIk', 'https://zh.wikipedia.org/wiki/%E5%A5%A5%E9%BB%9B%E4%B8%BD%C2%B7%E8%B5%AB%E6%9C%AC', 0, '2022-10-20 20:01:56', '2022-10-21 04:36:44', '奥黛丽·赫本（Audrey Hepburn，1929年5月4日-1993年1月20日），出生于比利时布鲁塞尔，毕业于玛莉·蓝伯特芭蕾舞学校，英国女演员。1948年，因出演《荷兰七课》，开始电影生涯。1954年，凭借电影《罗马假日》获得奥斯卡最佳女主角奖。晚年时，投身慈善事业，是联合国儿童基金会亲善大使的代表人物。1992年被授予美国“总统自由勋章”，1993年获奥斯卡人道主义奖。1993年1月20日，因癌症病逝，享年63岁。1999年，被美国电影学会评为“百年来最伟大的女演员”第三位。');

SET FOREIGN_KEY_CHECKS = 1;
