from django.db import models
from ckeditor.fields import RichTextField

import datetime
import platform

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

##文章表 字段：ID、所属板块、标题、正文（富文本）、最后修改日期、备注、附件的id们。  
class Article(models.Model):
    id = models.AutoField(primary_key = True)
    blockid = models.IntegerField()
    title = models.CharField(max_length = 50)
    content = models.TextField()
    modifytime = models.DateTimeField(auto_now = True)
    remark = models.CharField(max_length = 50)
    attachids = models.CharField(max_length = 20, default = None)
    
    def getblocktitle(self):
        block = Block.objects.filter(id=self.blockid)
        if block:
            return block[0].title
        else:
            return None
            
    def getimgsrc(self):
        if self.attachids:
            if self.attachids.isdigit():     #一个附件(图片)
                attach = Attach.objects.filter(id = int(self.attachids))
                if attach:
                    if platform.system() == 'Windows':  #local windows
                        return '/static/common_upload/' + attach[0].file_name       
                    elif platform.system() == 'Linux':  #aliyun
                        return '/static/common_upload/' + attach[0].file_name
                    else:
                        return 'ERROR'
                else:
                    return None
            else:                       #多个附件,暂不考虑
                return None
        return None

    def getimgname(self):
        if self.attachids:
            if self.attachids.isdigit():     #一个附件(图片)
                attach = Attach.objects.filter(id = int(self.attachids))
                if attach:
                    return attach[0].file_name
                else:
                    return None
            else:                       #多个附件,暂不考虑
                return None
        return None
        
    def __str__(self):
        return self.title
        
##板块表 字段：ID、父板块ID、标题、描述、最后修改日期、备注。      
class Block(models.Model):
    id = models.AutoField(primary_key = True)
    parentid = models.IntegerField()
    type = models.BooleanField(default = False)     #板块类型 False为子 True为父
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100)
    modifytime = models.DateTimeField(auto_now = True)
    remark = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.title

## 附件表 字段：ID、（绝对）路径、文件名、最后修改日期、备注
class Attach(models.Model):
    id = models.AutoField(primary_key = True)
    src = models.CharField(max_length = 100)
    file_name =models.CharField(max_length = 80)
    modifytime = models.DateTimeField(auto_now = True)
    remark = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.src
