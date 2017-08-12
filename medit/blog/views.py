from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

###外部函数

## 验证用户
## 输入用户名、密码
## 输出类型+代号 F错误 T成功  F0账号不存在 F1账号密码不对应
from blog.user import login_verify
## 自动检查用户
## 输入session
## 输出 True 已登陆 False 未登录
from blog.user import login_auto_check
## 添加板块
## 输入标题、描述、备注
## 输出类型+代号 F错误 T成功 (目前总是T)
from blog.common_add import new_block_add

## 按照时间由近至远寻找板块
## 输入范围
## 输出内容，格式为Queryset
from blog.common_select import select_block_bytime

## 生成页码标记
## 输入每页数量,当前页码和最多同时存在的页数
## 输出 (first_page number==1, 
##  [continuous pages such as 3 4 5 6 7 when present ==5], 
##  first_displaypagenumber, last_displaypagenumber, last page number)
from blog.common_select import generate_block_page

## 生成板块数量
## 输出数字
from blog.common_select import generate_total_block_number

# Create your views here.
def test(request):
    objects = Blog.objects.all()

    return render(request, 'blog/ckeditor_test.html',{
        #'tip':tip,
        #'status':status,
        #'logged':logged,
        })

## 登陆页面
def login(request):
    if request.META['REQUEST_METHOD'] == 'GET':
        result = login_auto_check(request.session)
        if result:
            return HttpResponseRedirect("../index")
        else:
            return render(request, 'blog/login.html',{
                #'tip':tip,
                #'status':status,
                #'logged':logged,
                })
    else:
        result = login_verify(request.POST.get('username'),request.POST.get('password'))
        if result == 'T':
            request.session['username'] = request.POST.get('username')
            request.session['password'] = request.POST.get('password')
            if request.POST.get('online') == '0':
                #浏览器关闭,session失效(这表示不自动登录)
                request.session.set_expiry(0)
            return HttpResponse('T')
        elif result == 'F1' or result == 'F0':
            return HttpResponse(result)
        else:   
            return HttpResponse('F2')

## 首页
def index(request):
    result = login_auto_check(request.session)
    if not result:
        return HttpResponseRedirect("../login")
    else:
        return render(request, 'blog/index.html')

## 板块列表页
def block_list(request):
    result = login_auto_check(request.session)
    if not result:
        return HttpResponseRedirect("../login")
    else:
        block_data = select_block_bytime((0,10))
        if request.GET.get('page'):
            present_page = int(request.GET.get('page'))
        else:
            present_page = 1
        page_data = generate_block_page(2,present_page,5)
        total_data_number = generate_total_block_number()
        return_dict = {'block_data':block_data,'total_data_number':total_data_number} 
        page_dict = {'first_page':page_data[0],
                'display_pages':page_data[1],
                'first_display_page':page_data[2],
                'last_display_page':page_data[3],
                'last_page':page_data[4],
                'display_pagenumber':page_data[3]-page_data[2]+1
                }
        page_dict['prepage_m1'] = present_page if present_page == 1 else present_page - 1
        page_dict['prepage_a1'] = present_page if present_page == page_data[4] else present_page + 1    
        return_dict['page_data'] = page_dict
        return render(request, 'blog/block-list.html',return_dict)

## 添加板块页
def block_add(request):
    if request.META['REQUEST_METHOD'] == 'GET':
        result = login_auto_check(request.session)
        if not result:
            return HttpResponseRedirect("../login")
        else:
            return render(request, 'blog/block-add.html')
    else:
        new_block_add(request.POST.get('title'),
            request.POST.get('description'),
            request.POST.get('remark'))
        return HttpResponse('T')
