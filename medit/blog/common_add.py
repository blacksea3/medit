from blog.models import *

## 添加板块
## 输入标题、描述、备注
## 输出类型+代号 F错误 T成功 (目前总是T)
def new_block_add(title,description,remark):
    newblock=Block(parentid=0,title=title,description=description,remark=remark)  
    newblock.save()
    return 'T'
