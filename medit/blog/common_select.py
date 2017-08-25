from blog.models import *

## 按照时间由近至远寻找板块
## 输入范围
## 输出内容，格式为Queryset
def select_block_bytime(range):
    newblocks = Block.objects.all().order_by('-modifytime')[range[0]:range[1]]
    return newblocks

## 寻找所有板块(按照时间由近至远)
## 输出内容，格式为Queryset
def select_block_all():
    newblocks = Block.objects.all().order_by('-modifytime')
    return newblocks    
    
## 按照ID寻找板块
## 输入ID
## 输出格式为Queryset    
def select_block_byid(bid):
    blockdata = Block.objects.filter(id=bid)
    return blockdata

## 生成板块数量
## 输出数字
def generate_total_block_number():
    return Block.objects.all().count()

## 按照时间由近至远寻找某版块下的文章
## 输入blockid,范围(若blockid=0表示全板块搜索)
## 输出内容，格式为Queryset
def select_article_bytime(bid,range):
    if not bid:
        newarticles = Article.objects.all().order_by('-modifytime')[range[0]:range[1]]
    else:
        newarticles = Article.objects.filter(blockid=bid).order_by('-modifytime')[range[0]:range[1]]
    return newarticles

## 寻找寻找某版块下所有的文章(按照时间由近至远)
## 输入blockid
## 输出内容，格式为Queryset
def select_article_all(bid):
    newarticles = Article.objects.filter(blockid=bid).order_by('-modifytime')
    return newarticles    

## 按照ID寻找文章
## 输入ID
## 输出格式为Queryset
def select_article_byid(aid):
    articledata = Article.objects.filter(id=aid)
    return articledata

## 搜索某版块热门文章,当前实现:按照时间由近至远寻找某版块下的文章
## 输入板块id(若blockid=0表示全板块搜索),数量
## 输出格式为Queryset
def select_article_byhot(bid,range):
    return select_article_bytime(bid,range)
    
## 搜索某版块高置顶文章,当前实现:按照时间由近至远寻找某版块下的文章
## 输入板块id(若blockid=0表示全板块搜索),数量
## 输出格式为Queryset
def select_article_bytop(bid,range):
    return select_article_bytime(bid,range)

## 生成文章数量(某版块下的)
## 输入blockid(若blockid=0表示全板块搜索)
## 输出数字
def generate_total_article_number(bid):
    if not bid:
        return Article.objects.all().count()
    else:
        return Article.objects.filter(blockid=bid).count()

## 生成板块页码标记
## 输入每页数量,当前页码和最多同时存在的页数
## 输出 (first_page number==1, 
##  [continuous pages such as 3 4 5 6 7 when present ==5], 
##  first_displaypagenumber, last_displaypagenumber, last page number)

def generate_block_page(number,present,occurnumber):
    last_page_number = Block.objects.all().count()//number + 1
    return generate_page(present,occurnumber,last_page_number)

## 生成文章页码标记
## 输入blockid,每页数量,当前页码和最多同时存在的页数(若blockid=0表示全板块搜索)
## 输出 (first_page number==1, 
##  [continuous pages such as 3 4 5 6 7 when present ==5], 
##  first_displaypagenumber, last_displaypagenumber, last page number)
def generate_article_page(bid,number,present,occurnumber):
    if not bid:
        last_page_number = Article.objects.all().count()//number + 1
        return generate_page(present,occurnumber,last_page_number)
    else:
        last_page_number = Article.objects.filter(blockid=bid).count()//number + 1
        return generate_page(present,occurnumber,last_page_number)

#页码参考表
'''
present occur   out         total==9
1       4       1234
2       4       1234
3       4       2345
1       5       12345
2       5       12345
3       5       12345
4       5       23456
7       4       6789
8       4       6789
9       4       6789
6       5       56789
7       5       56789
8       5       56789
9       5       56789
'''
    
## 生成页码标记
## 输入当前页码、最多同时存在的页数和总页数
## 输出 (first_page number==1, 
##  [continuous pages such as 3 4 5 6 7 when present ==5], 
##  first_displaypagenumber, last_displaypagenumber, last page number)  
def generate_page(present,occurnumber,last_page_number):
    if last_page_number <= occurnumber:
        return (1, [_ + 1 for _ in range(last_page_number)], 1, last_page_number, last_page_number)
    else:
        #页码靠前处理
        if present <= occurnumber//2:
            return (1, [_ + 1 for _ in range(occurnumber)], 1, occurnumber, last_page_number)
        #页码靠后处理 
        elif (last_page_number - present + 1) <= occurnumber//2:
            return (1, [last_page_number - occurnumber + _ + 1 for _ in range(occurnumber)], 
                last_page_number - occurnumber + 1, last_page_number, last_page_number)
        #页码居中处理
        else:
            return (1, [present - (occurnumber - occurnumber//2) + _ + 1 for _ in range(occurnumber)], 
                present - (occurnumber - occurnumber//2) + 1,
                present + occurnumber//2,
                last_page_number)
            