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

## 生成文章页码标记
## 输入blockid,每页数量,当前页码和最多同时存在的页数(若blockid=0表示全板块搜索)
## 输出 (first_page number==1, 
##  [continuous pages such as 3 4 5 6 7 when present ==5], 
##  first_displaypagenumber, last_displaypagenumber, last page number)
from blog.common_select import generate_article_page

## 生成文章数量(某版块下的)
## 输入blockid(若blockid=0表示全板块搜索)
## 输出数字
from blog.common_select import generate_total_article_number

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
    bid = request.GET.get('id')
    if bid and bid.isdigit():
        bid = int(bid)
    else:
        bid = 1
        
    if request.GET.get('page'):
        present_page = int(request.GET.get('page'))
    else:
        present_page = 1
    #文章数据部分 
    new_article_data_thisblock = select_article_bytime(bid,(5*present_page-5,5*present_page))    #此板块热门文章,5条
    new_article_data = select_article_bytime(0,(0,8))   #最新文章,全板块,8条
    hot_article_data = select_article_byhot(0,(0,5))    #热门文章,全板块,5条
    block_data = select_block_bytime((0,6))             #板块列表,6条
    present_block_data = select_block_byid(bid)
    total_data_number = generate_total_article_number(bid)
    return_dict = {'block_data':block_data,
        'presentbid':bid,
        'new_article_data_thisblock':new_article_data_thisblock,
        'new_article_data':new_article_data,
        'hot_article_data':hot_article_data,
        'present_block_data':present_block_data,
        'total_data_number':total_data_number
        }
    #页码部分
    page_data = generate_article_page(bid,5,present_page,5)
    page_dict = {'first_page':page_data[0],
            'display_pages':page_data[1],
            'first_display_page':page_data[2],
            'last_display_page':page_data[3],
            'last_page':page_data[4],
            'display_pagenumber':page_data[3]-page_data[2]+1,
            'present_page':present_page
            }
    page_dict['prepage_m1'] = present_page if present_page == 1 else present_page - 1
    page_dict['prepage_a1'] = present_page if present_page == page_data[4] else present_page + 1    
    return_dict['page_data'] = page_dict        
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
    