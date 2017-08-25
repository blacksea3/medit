import time
import os

from blog.models import *

## ckeditor上传图片,处理函数
## 输入文件(类似字典)
## 输出(响应,参数) 0正确,参数:文件名 1错误,参数:错误提示
def ck_deal_img(file):
    prefix = "static/ck_upload/"
    path = prefix + time.strftime("%Y%m%d%H%M%S",time.localtime())
    suffix = os.path.splitext(file.name)
    if suffix[1] in (".jpg",".png","gif","img"):
        full_file_name = path + "_" + file.name
        des_origin_f = open(full_file_name, "wb+")
        for chunk in file.chunks():
            des_origin_f.write(chunk)
        des_origin_f.close()
        return (0, full_file_name)
    else:
        return (1, "文件格式不正确（必须为.jpg/.gif/.bmp/.png文件）")

## 通用的上传文件,处理函数(现在只用作上传图片)
## 输入文件(类似字典)
## 输出(响应,参数) 0正确,参数:文件ID 1错误,参数:错误提示
def common_deal_file(file):
    prefix = "static/common_upload/"
    path = time.strftime("%Y%m%d%H%M%S",time.localtime())
    suffix = os.path.splitext(file.name)
    if suffix[1] in (".jpg",".png","gif","img"):
        full_file_name = prefix + path + "_" + file.name
        des_origin_f = open(full_file_name, "wb+")
        for chunk in file.chunks():
            des_origin_f.write(chunk)
        des_origin_f.close()
        newAttach=Attach(src = os.path.join(os.path.dirname(__file__), full_file_name).replace('\\','/'),
            file_name = path + "_" + file.name,
            remark = "")
        newAttach.save()
        thisattach = Attach.objects.filter(file_name = path + "_" + file.name)
        return (0, thisattach[0].id)
    else:
        return (1, "文件格式不正确（必须为.jpg/.gif/.bmp/.png文件）")
        