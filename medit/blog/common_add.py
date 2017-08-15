from blog.models import *

## 添加板块
## 输入标题、描述、备注
## 输出类型+代号 F错误 T成功 (目前总是T)
def new_block_add(title,description,remark):
    newblock=Block(parentid=0,title=title,description=description,remark=remark)  
    newblock.save()
    return 'T'

## 编辑板块
## 输入ID、标题、描述、备注
## 输出类型+代号 F错误 T成功 (目前总是T)
def old_block_edit(bid,title,description,remark):
    block = Block.objects.filter(id=bid)
    if block:
        block[0].title = title
        block[0].description = description
        block[0].remark = remark
        block[0].save()
    return 'T'

## 删除板块
## 输入ID
## 输出类型+代号 F错误 T成功 F1 板块不存在 F2里面还有文章
def old_block_del(bid):
    article = Article.objects.filter(blockid=bid)
    if article:
        return 'F2'
    else:
        block = Block.objects.filter(id=bid)
        if not block:
            return 'F1'
        else:
            block[0].delete()
            return 'T'

## 添加文章
## 输入板块id、标题、内容、备注
## 输出类型+代号 F错误 T成功 (目前总是T)
def new_article_add(bid,title,content,remark):
    newarticle=Article(blockid=bid,title=title,content=content,remark=remark)  
    newarticle.save()
    return 'T'          
        
## 编辑文章
## 输入ID、所属板块ID、标题、内容、备注
## 输出类型+代号 F错误 T成功 (目前总是T)
def old_article_edit(aid,blockid,title,content,remark):
    article = Article.objects.filter(id=aid)
    if article:
        article[0].blockid = blockid
        article[0].title = title
        article[0].content = content
        article[0].remark = remark
        article[0].save()
    return 'T'

## 删除文章
## 输入ID
## 输出类型+代号 F错误 T成功 F1 文章不存在
def old_article_del(aid):
    article = Article.objects.filter(id=aid)
    if not article:
        return 'F1'
    else:
        article[0].delete()
        return 'T'
