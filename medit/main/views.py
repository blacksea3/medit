from django.shortcuts import render

## 按照时间由近至远寻找板块
## 输入范围
## 输出内容，格式为Queryset
from blog.common_select import select_block_bytime

## 按照ID寻找板块
## 输入ID
## 输出格式为Queryset    
from blog.common_select import select_block_byid

## 按照时间由近至远寻找某版块下的文章
## 输入blockid,范围(若blockid=0表示全板块搜索)
## 输出内容，格式为Queryset
from blog.common_select import select_article_bytime

## 搜索某版块热门文章,当前实现:按照时间由近至远寻找某版块下的文章
## 输入板块id(若blockid=0表示全板块搜索),数量
## 输出格式为Queryset
from blog.common_select import select_article_byhot
    
## 搜索某版块高置顶文章,当前实现:按照时间由近至远寻找某版块下的文章
## 输入板块id(若blockid=0表示全板块搜索),数量
## 输出格式为Queryset
from blog.common_select import select_article_bytop

## 按照ID寻找文章
## 输入ID
## 输出格式为Queryset
from blog.common_select import select_article_byid

# Create your views here.

## 首页
def index(request):
    top_article_data = select_article_bytop(0,(0,5))    #置顶文章,全板块,5条
    new_article_data = select_article_bytime(0,(0,8))   #最新文章,全板块,8条
    hot_article_data = select_article_byhot(0,(0,5))    #热门文章,全板块,5条
    
    block_data = select_block_bytime((0,6))             #板块列表,6条
    
    return_dict = {'block_data':block_data,
        'top_article_data':top_article_data,
        'new_article_data':new_article_data,
        'hot_article_data':hot_article_data}
    return render(request, 'main/index.html',return_dict)

## 板块页
def block(request):
    blockid = request.GET.get('id')
    if blockid and blockid.isdigit():
        blockid = int(blockid)
    else:
        blockid = 1

    new_article_data_thisblock = select_article_bytime(blockid,(0,5))    #此板块热门文章,5条
    new_article_data = select_article_bytime(0,(0,8))   #最新文章,全板块,8条
    hot_article_data = select_article_byhot(0,(0,5))    #热门文章,全板块,5条
    
    block_data = select_block_bytime((0,6))             #板块列表,6条
    present_block_data = select_block_byid(blockid)
    
    return_dict = {'block_data':block_data,
        'new_article_data_thisblock':new_article_data_thisblock,
        'new_article_data':new_article_data,
        'hot_article_data':hot_article_data,
        'present_block_data':present_block_data
        }
    return render(request, 'main/blocklist.html',return_dict)
    
## 文章页
def article(request):
    articleid = request.GET.get('id')
    if articleid and articleid.isdigit():
        articleid = int(articleid)
    else:
        articleid = 1
    
    present_article_data = select_article_byid(articleid)    #此文章
    new_article_data = select_article_bytime(0,(0,8))   #最新文章,全板块,8条
    hot_article_data = select_article_byhot(0,(0,5))    #热门文章,全板块,5条
    
    block_data = select_block_bytime((0,6))             #板块列表,6条
    
    return_dict = {'block_data':block_data,
        'present_article_data':present_article_data,
        'new_article_data':new_article_data,
        'hot_article_data':hot_article_data
        }
    return render(request, 'main/article.html',return_dict)
    