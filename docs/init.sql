/*
 Navicat Premium Data Transfer

 Source Server         : 175.178.3.27_3306
 Source Server Type    : MySQL
 Source Server Version : 80031
 Source Host           : 175.178.3.27:3306
 Source Schema         : brian_blog

 Target Server Type    : MySQL
 Target Server Version : 80031
 File Encoding         : 65001

 Date: 10/02/2023 22:04:37
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for art_article
-- ----------------------------
DROP TABLE IF EXISTS `art_article`;
CREATE TABLE `art_article` (
  `article_id` bigint unsigned NOT NULL AUTO_INCREMENT COMMENT '文章ID',
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '标题',
  `digest` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT '' COMMENT '摘要',
  `cover` char(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'art_default.jpg' COMMENT '封面图',
  `content` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '内容',
  `read_count` int unsigned NOT NULL DEFAULT '0' COMMENT '阅读量',
  `comment_count` int unsigned NOT NULL DEFAULT '0' COMMENT '评论量',
  `category_id` int unsigned DEFAULT NULL COMMENT '分类',
  `author_id` int NOT NULL COMMENT '作者',
  `is_delete` tinyint(1) NOT NULL DEFAULT '0' COMMENT '逻辑删除',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `update_time` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`article_id`) USING BTREE,
  UNIQUE KEY `title` (`title`) USING BTREE,
  KEY `category_id` (`category_id`) USING BTREE,
  KEY `author_id` (`author_id`) USING BTREE,
  CONSTRAINT `author_id` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `category_id` FOREIGN KEY (`category_id`) REFERENCES `art_category` (`category_id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of art_article
-- ----------------------------
BEGIN;
INSERT INTO `art_article` VALUES (1, 'macOS重装教程', '重装安装你的MacOS。降级安装或者升级安装', 'FlPypeeEqIJ1X36Fl6T2HR05JlAi', '<p>先决条件:</p>\r\n\r\n<ol>\r\n	<li>大于16g的U 盘或移动硬盘</li>\r\n	<li>Monterey 安装包</li>\r\n</ol>\r\n\r\n<p>InstallAssistant.pkg</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>重装步骤</p>\r\n\r\n<ol>\r\n	<li>关闭&rdquo;查找&ldquo;功能</li>\r\n	<li>点击Monterey安装包,安装程序; 之后会在&ldquo;应用程序&rdquo;中多出&ldquo;安装macos Monterey&rdquo;</li>\r\n	<li>格式化u盘</li>\r\n</ol>\r\n\r\n<p>选择格式macOS 命名为Installer</p>\r\n\r\n<ol>\r\n	<li>终端执行命令</li>\r\n</ol>\r\n\r\n<p>sudo /Applications/Install\\ macOS\\ Monterey.app/Contents/Resources/createinstallmedia --volume /Volumes/Installer</p>\r\n\r\n<ol>\r\n	<li>关机</li>\r\n	<li>按一次开机键，再长按开机键</li>\r\n	<li>选择&ldquo;选项&rdquo;；</li>\r\n	<li>点击&ldquo;实用工具&rdquo;，选择&ldquo;终端&rdquo;</li>\r\n	<li>输入&ldquo;resetpassword&rdquo;；出现&ldquo;重设密码&rdquo;页面</li>\r\n	<li>点击右上角&ldquo;恢复助理&rdquo;，选择&ldquo;抹掉mac&rdquo;；出现窗口&ldquo;抹掉mac&rdquo;</li>\r\n	<li>点击&ldquo;抹掉mac&rdquo;窗口中的&ldquo;抹掉mac&rdquo;；系统重启</li>\r\n	<li>进入开机页面，选择语言&ldquo;中文&rdquo;；进入&ldquo;激活mac&rdquo;</li>\r\n	<li>如果显示mac未激活，点击右上角连接Wi-Fi激活。如果显示已激活，点击左上角苹果logo选择关机</li>\r\n	<li>按一次开机键，再长按开机键</li>\r\n	<li>选择install macOS</li>\r\n	<li>选择语言&ldquo;中文&rdquo;，&ldquo;继续&rdquo;，&ldquo;同意协议&rdquo;，选择安装的系统盘</li>\r\n	<li>等待系统安装，大概30分钟左右。安装完成后系统自动开机，此时系统安装完成，进入初始化界面</li>\r\n	<li>正常设置初始化配置，不过Apple ID先不登陆，以防出现&ldquo;文件保险箱磁盘加密&rdquo;。</li>\r\n	<li>如果在初始化设置时出现&ldquo;文件保险箱磁盘加密&rdquo;，将&ldquo;启动磁盘保险箱加密&rdquo;和&ldquo;允许我的iCloud帐户解锁我的磁盘&rdquo;设置为非勾选。如果没有出现，在初始化设置完成后可正常登陆Apple ID。此时整个重装过程已完成</li>\r\n</ol>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>将U盘修改为正常u盘：</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>https://www.cleanmymac.cn/blog/how-to-clean-install-macos-monterey.html</p>', 37, 0, 3, 1, 0, '2022-09-13 22:46:15', '2023-01-16 03:00:00');
INSERT INTO `art_article` VALUES (2, 'MacOS install python', '在MacOS上安装Python', 'Fm3Ytx0TJJdcbaXKwW-4mIWQN6A_', '<h2>1. 下载python</h2>\r\n\r\n<h2><span style=\"font-size:16px\">可以选择从官网或第三方镜像下载。注意<span style=\"background-color:#f1c40f\">有些python版本不支持MacOS</span></span></h2>\r\n\r\n<ul>\r\n	<li><span style=\"font-size:14px\">从官网下载</span><span style=\"font-size:14px\">：<span style=\"color:#27ae60\">https://www.python.org/downloads</span><span style=\"background-color:#2980b9\">/</span></span></li>\r\n	<li><span style=\"font-size:14px\">从华为云镜像下载(推荐)：<span style=\"color:#27ae60\">https://mirrors.huaweicloud.com/python/</span></span></li>\r\n</ul>\r\n\r\n<p>这里以华为云镜像为例。选择需要安装的python版本, 选择<strong>pkg</strong>后缀的安装包。</p>\r\n\r\n<p><img alt=\"\" src=\"https://image.brianblog.asia/Ft3GOqYzEGfuP2LLX20fVtx7G38Z\" style=\"height:396px; width:650px\" /></p>\r\n\r\n<h2>2. 安装python</h2>\r\n\r\n<p>下载完成后<strong>双击</strong>安装包无脑式安装</p>\r\n\r\n<p><img alt=\"\" src=\"https://image.brianblog.asia/FjVc9LnwS2RhMtfPyUE-NgURAoqb\" style=\"height:323px; width:650px\" /></p>\r\n\r\n<h2>3. 测试运行</h2>\r\n\r\n<p>在终端运行python和pip是否成功。</p>\r\n\r\n<p><img src=\"https://image.brianblog.asia/FtIG1QWNyvcLOKhMsjGGsOezDRui\" style=\"height:407px; width:650px\" /></p>\r\n\r\n<p>如图所示, 输入<code>python3</code>可以被识别而<span style=\"color:#bdc3c7\"><code>python</code>不能被识别</span>, 这时需要创建<code>python3</code>的软链接指向<code>python。</code>pip同样如此。</p>\r\n\r\n<pre>\r\n<code class=\"language-bash\">sudo ln -s /usr/local/bin/python3 /usr/local/bin/python\r\nsudo ln -s /usr/local/bin/pip3 /usr/local/bin/pip</code></pre>\r\n\r\n<p><img src=\"https://image.brianblog.asia/Fk2HPcPrldKlGHVSyHL03D5bu4HK\" style=\"height:305px; width:650px\" /></p>\r\n\r\n<p>&nbsp;</p>', 53, 3, 1, 1, 0, '2022-09-13 23:06:41', '2023-01-21 03:00:00');
INSERT INTO `art_article` VALUES (3, 'selenium 页面等待', 'selenium中的页面等待是什么？如何使用它？', 'FsiCfIDXFip-64oHHZoMiE46EFo2', '<h2>页面等待</h2>\r\n\r\n<p>获取标签(定位元素)时, 页面可能没有渲染完成。所以在get方法(网络请求完成)后立即获取标签可能会因为找不到元素而程序崩溃。</p>\r\n\r\n<p>两种页面等待：</p>\r\n\r\n<ul>\r\n	<li>隐式等待</li>\r\n</ul>\r\n\r\n<ul>\r\n	<li>显式等待</li>\r\n</ul>\r\n\r\n<p>隐式等待：规定在<strong>一定时长</strong>内获取到元素才能运行下一句代码</p>\r\n\r\n<pre>\r\n<code class=\"language-python\"># 每次获取元素时它的运行机制是这样的：\r\n#     1. 每500ms尝试获取一次元素；2. 超过10s抛出异常, 程序崩溃\r\ndriver.implicitly_wait(10)\r\ntag1 = driver.find_element(by=By.NAME, value=\"v1\")\r\ntag2 = driver.find_element(by=By.NAME, value=\"va2\")\r\n</code></pre>\r\n\r\n<p>显示等待：当<strong>某个条件</strong>成立时才能运行下一句代码</p>\r\n\r\n<pre>\r\n<code class=\"language-python\">from selenium.webdriver.common.by import By\r\nfrom selenium.webdriver.support.wait import WebDriverWait\r\nfrom selenium.webdriver.support import expected_conditions as EC\r\n\r\n# 设置元素等待实例，最多等10秒，每0.5秒查看条件是否成立\r\nelement = WebDriverWait(driver, 10, 0.5).until(\r\n    # 条件：直到元素加载完成\r\n    EC.presence_of_element_located((By.ID, \"kw\"))\r\n)\r\n</code></pre>\r\n\r\n<ul>\r\n	<li>显示等待的例子中, 效果和隐式等待是一样的。不过在实际开发中, 我们可以指定其它条件, 当<strong>这些条件成立时</strong>才能执行下一句代码, 这才是显式等待的意义。\r\n\r\n	<ul>\r\n		<li>等待某个元素消失，比如进度条; 等待元素的属性变化，比如 style，src，value 之类的属性变为期望的值;</li>\r\n		<li>等待多个元素都符合期望的条件</li>\r\n		<li>多种复合条件需要同时满足</li>\r\n	</ul>\r\n	</li>\r\n</ul>\r\n\r\n<ul>\r\n	<li>隐式等待<code>implicitly_wait()</code>对每次获取标签有效, 显示等待是作为某一段代码执行前的条件判断</li>\r\n</ul>', 148, 0, 1, 1, 0, '2022-10-19 08:14:09', '2023-01-14 03:00:00');
INSERT INTO `art_article` VALUES (4, 'robots.txt文件说明', 'robots协议说明及简单编写robots.txt文件', 'FuYqcYjY2ttur4Or3QVcHfmqhnwt', '<h2>robots文件说明</h2>\r\n\r\n<p><strong>Robots协议</strong>（也叫爬虫协议、机器人协议等），全称是&ldquo;网络爬虫排除标准&rdquo;（Robots Exclusion Protocol），网站通过Robots协议告诉搜索引擎哪些页面可以抓取，哪些页面不能抓取，例如：</p>\r\n\r\n<p>淘宝网：https://www.taobao.com/robots.txt</p>\r\n\r\n<p>腾讯网：&nbsp;http://www.qq.com/robots.txt</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<h2>robots文件编写</h2>\r\n\r\n<p>允许所有的机器人：</p>\r\n\r\n<div style=\"background:#eeeeee; border:1px solid #cccccc; padding:5px 10px\">User-agent: *<br />\r\nDisallow:</div>\r\n\r\n<p>另一写法</p>\r\n\r\n<div style=\"background:#eeeeee; border:1px solid #cccccc; padding:5px 10px\">User-agent: *<br />\r\nAllow:/</div>\r\n\r\n<p>仅允许特定的机器人：（name_spider用真实名字代替）</p>\r\n\r\n<div style=\"background:#eeeeee; border:1px solid #cccccc; padding:5px 10px\">User-agent: name_spider<br />\r\nAllow:</div>\r\n\r\n<p>拦截所有的机器人：</p>\r\n\r\n<div style=\"background:#eeeeee; border:1px solid #cccccc; padding:5px 10px\">User-agent: *<br />\r\nDisallow: /</div>\r\n\r\n<p>禁止所有机器人访问特定目录：</p>\r\n\r\n<div style=\"background:#eeeeee; border:1px solid #cccccc; padding:5px 10px\">User-agent: *<br />\r\nDisallow: /cgi-bin/<br />\r\nDisallow: /images/<br />\r\nDisallow: /tmp/<br />\r\nDisallow: /private/</div>\r\n\r\n<p>仅禁止坏爬虫访问特定目录（BadBot用真实的名字代替）：</p>\r\n\r\n<div style=\"background:#eeeeee; border:1px solid #cccccc; padding:5px 10px\">User-agent: BadBot<br />\r\nDisallow: /private/</div>\r\n\r\n<p>禁止所有机器人访问特定文件类型<sup>[2]</sup>：</p>\r\n\r\n<div style=\"background:#eeeeee; border:1px solid #cccccc; padding:5px 10px\">User-agent: *<br />\r\nDisallow: /*.php$<br />\r\nDisallow: /*.js$<br />\r\nDisallow: /*.inc$<br />\r\nDisallow: /*.css$</div>', 26, 0, 1, 1, 0, '2022-10-19 08:39:24', '2023-01-20 03:00:00');
COMMIT;

-- ----------------------------
-- Table structure for art_article_tag
-- ----------------------------
DROP TABLE IF EXISTS `art_article_tag`;
CREATE TABLE `art_article_tag` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `article_id` bigint unsigned NOT NULL,
  `tag_id` int unsigned NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `article_id` (`article_id`) USING BTREE,
  KEY `tag_id` (`tag_id`) USING BTREE,
  CONSTRAINT `article_id` FOREIGN KEY (`article_id`) REFERENCES `art_article` (`article_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `tag_id` FOREIGN KEY (`tag_id`) REFERENCES `art_tag` (`tag_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of art_article_tag
-- ----------------------------
BEGIN;
INSERT INTO `art_article_tag` VALUES (6, 2, 4);
INSERT INTO `art_article_tag` VALUES (7, 1, 4);
INSERT INTO `art_article_tag` VALUES (8, 3, 9);
INSERT INTO `art_article_tag` VALUES (9, 3, 5);
INSERT INTO `art_article_tag` VALUES (10, 4, 10);
COMMIT;

-- ----------------------------
-- Table structure for art_category
-- ----------------------------
DROP TABLE IF EXISTS `art_category`;
CREATE TABLE `art_category` (
  `category_id` int unsigned NOT NULL AUTO_INCREMENT COMMENT '分类ID',
  `name` char(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '分类名称',
  `is_delete` tinyint(1) NOT NULL DEFAULT '0' COMMENT '逻辑删除',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `update_time` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`category_id`) USING BTREE,
  UNIQUE KEY `name` (`name`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of art_category
-- ----------------------------
BEGIN;
INSERT INTO `art_category` VALUES (1, 'Python', 0, '2022-09-13 22:43:38', '2022-09-17 16:55:20');
INSERT INTO `art_category` VALUES (2, 'Djagno', 0, '2022-09-13 23:15:06', '2022-10-09 04:19:30');
INSERT INTO `art_category` VALUES (3, '电脑程序', 0, '2022-09-17 16:56:01', '2022-12-10 06:36:12');
COMMIT;

-- ----------------------------
-- Table structure for art_recommend
-- ----------------------------
DROP TABLE IF EXISTS `art_recommend`;
CREATE TABLE `art_recommend` (
  `recommend_id` int unsigned NOT NULL AUTO_INCREMENT,
  `article_id` bigint unsigned NOT NULL,
  `is_delete` tinyint(1) NOT NULL DEFAULT '0' COMMENT '逻辑删除',
  PRIMARY KEY (`recommend_id`) USING BTREE,
  KEY `art_recommend_ibfk_1` (`article_id`) USING BTREE,
  CONSTRAINT `art_recommend_ibfk_1` FOREIGN KEY (`article_id`) REFERENCES `art_article` (`article_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of art_recommend
-- ----------------------------
BEGIN;
INSERT INTO `art_recommend` VALUES (1, 1, 0);
INSERT INTO `art_recommend` VALUES (2, 2, 0);
COMMIT;

-- ----------------------------
-- Table structure for art_tag
-- ----------------------------
DROP TABLE IF EXISTS `art_tag`;
CREATE TABLE `art_tag` (
  `tag_id` int unsigned NOT NULL AUTO_INCREMENT COMMENT '标签ID',
  `name` char(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '标签名称',
  `is_delete` tinyint(1) NOT NULL DEFAULT '0' COMMENT '逻辑删除',
  PRIMARY KEY (`tag_id`) USING BTREE,
  UNIQUE KEY `name` (`name`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of art_tag
-- ----------------------------
BEGIN;
INSERT INTO `art_tag` VALUES (2, '软件分享', 0);
INSERT INTO `art_tag` VALUES (4, '环境安装', 0);
INSERT INTO `art_tag` VALUES (5, '心得分享', 0);
INSERT INTO `art_tag` VALUES (9, 'sulenium', 0);
INSERT INTO `art_tag` VALUES (10, '网络爬虫', 0);
COMMIT;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `name` (`name`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of auth_group
-- ----------------------------
BEGIN;
INSERT INTO `auth_group` VALUES (1, '普通用户');
INSERT INTO `auth_group` VALUES (2, '管理层');
COMMIT;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`) USING BTREE,
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------
BEGIN;
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
COMMIT;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
BEGIN;
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
COMMIT;

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `first_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `is_delete` tinyint(1) NOT NULL DEFAULT '0' COMMENT '逻辑删除',
  `phone` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT '' COMMENT '手机号',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
BEGIN;
INSERT INTO `auth_user` VALUES (1, 'pbkdf2_sha256$260000$bvzHmseQmFwWzbMSutz1cP$2lDFJahNe5uHKZ1GB0dtpJN8IPDUh6zZe63GoMaPv4A=', '2023-01-10 22:35:41.673169', 1, 'brian', '', '', 'chengrip@foxemail.com', 1, 1, '2022-09-22 19:18:45.263961', 0, NULL);
INSERT INTO `auth_user` VALUES (2, 'pbkdf2_sha256$260000$IPNV3hHCPT6v01ykSqB2jW$8gXYYDLpx8EQhpWXcUSPvG+DvFl+i4A++XaFpljLmsI=', '2022-11-01 04:28:07.303691', 0, 'brianf', '', '', '1677880403@qq.com', 1, 1, '2022-11-01 01:01:00.000000', 0, NULL);
COMMIT;

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`) USING BTREE,
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------
BEGIN;
INSERT INTO `auth_user_groups` VALUES (1, 2, 1);
COMMIT;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`) USING BTREE,
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `object_repr` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`) USING BTREE,
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
BEGIN;
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
COMMIT;

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
BEGIN;
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
COMMIT;

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  KEY `django_session_expire_date_a5c62663` (`expire_date`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of django_session
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for home_link
-- ----------------------------
DROP TABLE IF EXISTS `home_link`;
CREATE TABLE `home_link` (
  `link_id` int unsigned NOT NULL AUTO_INCREMENT COMMENT '友情链接ID',
  `name` char(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '链接名称',
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '标题',
  `url` tinytext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '链接地址',
  `is_delete` tinyint(1) NOT NULL DEFAULT '0' COMMENT '逻辑删除',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `update_time` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`link_id`) USING BTREE,
  UNIQUE KEY `name` (`name`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of home_link
-- ----------------------------
BEGIN;
INSERT INTO `home_link` VALUES (5, '画廊', '作者的画廊', 'https://gallery.brianblog.asia/', 0, '2023-01-03 02:02:22', '2023-01-03 02:02:22');
INSERT INTO `home_link` VALUES (3, '大鱼的鱼塘', '大鱼的鱼塘 - 一个总会有收获的地方', 'http://brucedone.com', 0, '2022-09-14 21:15:11', '2022-09-14 21:15:11');
INSERT INTO `home_link` VALUES (4, '灯塔水母', '', 'http://www.songluyi.com/', 0, '2022-09-14 21:15:53', '2022-09-14 21:15:53');
INSERT INTO `home_link` VALUES (6, 'Cheng CV', '作者的名片', 'https://itcheng.brianblog.asia/', 0, '2023-01-03 02:02:49', '2023-01-03 02:02:49');
COMMIT;

-- ----------------------------
-- Table structure for home_notice
-- ----------------------------
DROP TABLE IF EXISTS `home_notice`;
CREATE TABLE `home_notice` (
  `notice_id` int unsigned NOT NULL AUTO_INCREMENT COMMENT '滚动消息ID',
  `content` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `update_time` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  `is_delete` tinyint NOT NULL DEFAULT '0' COMMENT '逻辑删除',
  PRIMARY KEY (`notice_id`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of home_notice
-- ----------------------------
BEGIN;
INSERT INTO `home_notice` VALUES (2, '生命短暂，你需要Python！', '2022-09-15 15:02:32', '2022-12-18 18:00:28', 0);
INSERT INTO `home_notice` VALUES (3, 'Follow your heart, fuck everything else.', '2022-09-15 15:04:24', '2022-11-21 20:16:49', 0);
COMMIT;

-- ----------------------------
-- Table structure for home_slideshow
-- ----------------------------
DROP TABLE IF EXISTS `home_slideshow`;
CREATE TABLE `home_slideshow` (
  `slideshow_id` int unsigned NOT NULL AUTO_INCREMENT COMMENT '轮播图ID',
  `title` char(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT '' COMMENT '标题',
  `image` char(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '图片',
  `url` varchar(2048) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT 'http://www.baidu.com' COMMENT '链接',
  `is_delete` tinyint(1) NOT NULL DEFAULT '0' COMMENT '逻辑删除',
  `create_time` datetime NOT NULL COMMENT '创建时间',
  `update_time` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  `brief` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '简介',
  PRIMARY KEY (`slideshow_id`) USING BTREE,
  UNIQUE KEY `title` (`title`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of home_slideshow
-- ----------------------------
BEGIN;
INSERT INTO `home_slideshow` VALUES (2, 'Brian Griffin', 'FjHMxcQS6hS9Pzff5nXS5xUglS7k', 'https://www.youtube.com/watch?v=p2xqEx2O15Y', 0, '2022-09-15 18:13:54', '2022-11-20 19:53:32', '布赖恩·格里芬（英语：Brian Griffin）是美国喜剧动画《居家男人》角色。一个拟人化的狗，由塞思·麦克法兰配音，本作的主角和格里芬家庭中的一员。他是陷入困境的作家，试图以散文、小说、剧本和报纸上的文章来挽回声誉。');
INSERT INTO `home_slideshow` VALUES (1, '娜塔莎·罗曼诺夫', 'FleTGSNiX1-7BUr8gtM0_-MD6Mjd', 'https://zh.wikipedia.org/wiki/%E9%BB%91%E5%AF%A1%E5%A9%A6_(%E9%9B%BB%E5%BD%B1)', 0, '2022-09-15 17:46:45', '2022-11-20 19:50:55', '娜塔莎·罗曼诺夫从2010年电影《钢铁侠2》被引入到漫威电影宇宙系列中，并成为核心角色且出现在随后的九部电影里。 这个角色在2021年电影《黑寡妇》中最后登场。');
INSERT INTO `home_slideshow` VALUES (3, 'Brian Griffin2', 'Fk3sm2FE9-gHcrsY1f9Ib-5M7bgz', 'https://www.youtube.com/watch?v=p2xqEx2O15Y', 1, '2022-09-22 20:25:34', '2022-11-20 19:54:55', '布赖恩·格里芬（英语：Brian Griffin）是美国喜剧动画《居家男人》角色。一个拟人化的狗，由塞思·麦克法兰配音，本作的主角和格里芬家庭中的一员。他是陷入困境的作家，试图以散文、小说、剧本和报纸上的文章来挽回声誉。');
INSERT INTO `home_slideshow` VALUES (4, '奥黛丽·赫本', 'Fl4Hkc_EEkm8hZ17bW8XqZ5Wgt0r', 'https://zh.wikipedia.org/wiki/%E5%A5%A5%E9%BB%9B%E4%B8%BD%C2%B7%E8%B5%AB%E6%9C%AC', 0, '2022-10-20 20:01:56', '2022-11-20 19:47:54', '奥黛丽·赫本（Audrey Hepburn，1929年5月4日-1993年1月20日），出生于比利时布鲁塞尔，毕业于玛莉·蓝伯特芭蕾舞学校，英国女演员。1948年，因出演《荷兰七课》，开始电影生涯。1954年，凭借电影《罗马假日》获得奥斯卡最佳女主角奖。晚年时，投身慈善事业，是联合国儿童基金会亲善大使的代表人物。1992年被授予美国“总统自由勋章”，1993年获奥斯卡人道主义奖。1993年1月20日，因癌症病逝，享年63岁。1999年，被美国电影学会评为“百年来最伟大的女演员”第三位。');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
