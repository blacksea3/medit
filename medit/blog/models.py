from django.db import models
from ckeditor.fields import RichTextField

import datetime

##ckeditor,现在还没用上
class Blog(models.Model):
	title = models.CharField(max_length = 50, verbose_name = "标题")
	content = RichTextField(blank = True, null = True, verbose_name = "内容")
	
	def __unicode__(self):
		return self.name

##用户表 字段：ID、用户名、密码、邮箱、注册日期、备注。	
class User(models.Model):
	id = models.AutoField(primary_key = True)
	username = models.CharField(max_length = 16, unique=True)
	password = models.CharField(max_length = 16)
	email = models.CharField(max_length = 50)
	registertime = models.DateTimeField(auto_now = True)
	remark = models.CharField(max_length = 50)
	
	def __str__(self):
		return self.username

	#def getlongid(self):
	#

##文章表 字段：ID、所属板块、标题、正文（富文本）、最后修改日期、备注。	
class Article(models.Model):
	id = models.AutoField(primary_key = True)
	blockid = models.IntegerField()
	title = models.CharField(max_length = 50)
	content = models.TextField()
	modifytime = models.DateTimeField(auto_now = True)
	remark = models.CharField(max_length = 50)
	
	def __str__(self):
		return self.username
		
##板块表 字段：ID、父板块ID、标题、描述、最后修改日期、备注。		
class Block(models.Model):
	id = models.AutoField(primary_key = True)
	parentid = models.IntegerField()
	type = models.BooleanField(default = False)		#板块类型 False为子 True为父
	title = models.CharField(max_length = 50)
	description = models.CharField(max_length = 100)
	modifytime = models.DateTimeField(auto_now = True)
	remark = models.CharField(max_length = 50)
	
	def __str__(self):
		return self.username
		