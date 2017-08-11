from django.db import models
from ckeditor.fields import RichTextField

class Blog(models.Model):

    title = models.CharField(max_length=50,verbose_name="标题")
    content = RichTextField(blank=True,null=True,verbose_name="内容")

    def __unicode__(self):
        return self.name
