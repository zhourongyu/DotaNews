创建表结构如下

CREATE TABLE  `url_short` (
  `id` int(10) unsigned NOT NULL auto_increment,
  `url` varchar(2048) character set utf8 collate utf8_bin NOT NULL,
  PRIMARY KEY  (`id`),
  KEY `index_2` (`url`(333))
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

使用mako模板
