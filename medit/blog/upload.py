import time
import os

## ckeditor上传图片,处理函数
## 输入文件(类似字典)
## 输出(响应,参数) 0正确,参数:文件名 1错误,参数:错误提示
def ck_deal_img(file):
    path = "static/ck_upload/" + time.strftime("%Y%m%d%H%M%S",time.localtime())
    suffix = os.path.splitext(file.name)
    if suffix[1] in (".jpg",".png","gif","img"):
        file_name = path + "_" + file.name
        des_origin_f = open(file_name, "wb+")
        for chunk in file.chunks():
            des_origin_f.write(chunk)
        des_origin_f.close()
        return (0, file_name)
    else:
        return (1, "文件格式不正确（必须为.jpg/.gif/.bmp/.png文件）")
