from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

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

## 编辑板块
## 输入ID、标题、描述、备注
## 输出类型+代号 F错误 T成功 (目前总是T)
from blog.common_add import old_block_edit

## 删除板块
## 输入ID
## 输出类型+代号 F错误 T成功 F1 板块不存在 F2里面还有文章
from blog.common_add import old_block_del

## 按照时间由近至远寻找板块
## 输入范围
## 输出内容，格式为Queryset
from blog.common_select import select_block_bytime

## 生成板块页码标记
## 输入每页数量,当前页码和最多同时存在的页数
## 输出 (first_page number==1, 
##  [continuous pages such as 3 4 5 6 7 when present ==5], 
##  first_displaypagenumber, last_displaypagenumber, last page number)
from blog.common_select import generate_block_page

## 生成板块数量
## 输出数字
from blog.common_select import generate_total_block_number

## 按照ID寻找板块
## 输入ID
## 输出格式为Queryset    
from blog.common_select import select_block_byid

## 寻找所有板块(按照时间由近至远)
## 输出内容，格式为Queryset
from blog.common_select import select_block_all

## 添加文章
## 输入板块id、标题、内容、备注
## 输出类型+代号 F错误 T成功 (目前总是T)
from blog.common_add import new_article_add

## 按照时间由近至远寻找某版块下的文章
## 输入blockid,范围(若blockid=0表示全板块搜索)
## 输出内容，格式为Queryset
from blog.common_select import select_article_bytime

## 寻找寻找某版块下所有的文章(按照时间由近至远)
## 输入blockid
## 输出内容，格式为Queryset
from blog.common_select import select_article_all

## 按照ID寻找文章
## 输入ID
## 输出格式为Queryset    
from blog.common_select import select_article_byid

## 生成文章数量(某版块下的)
## 输入blockid(若blockid=0表示全板块搜索)
## 输出数字
from blog.common_select import generate_total_article_number
    
## 生成文章页码标记
## 输入blockid,每页数量,当前页码和最多同时存在的页数
## 输出 (first_page number==1, 
##  [continuous pages such as 3 4 5 6 7 when present ==5], 
##  first_displaypagenumber, last_displaypagenumber, last page number)
from blog.common_select import generate_article_page

## 编辑文章
## 输入ID、所属板块ID、标题、内容、备注
## 输出类型+代号 F错误 T成功 (目前总是T)
from blog.common_add import old_article_edit

## 删除文章
## 输入ID
## 输出类型+代号 F错误 T成功 F1 文章不存在
from blog.common_add import old_article_del

## ckeditor上传图片,处理函数
## 输入文件(类似字典)
## 输出(响应,参数) 0正确,参数:文件名 1错误,参数:错误提示
from blog.upload import ck_deal_img

# Create your views here.
def test(request):
    #objects = Blog.objects.all()

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
        if request.GET.get('page'):
            present_page = int(request.GET.get('page'))
        else:
            present_page = 1
        block_data = select_block_bytime((10*present_page-10,10*present_page)) 
        page_data = generate_block_page(10,present_page,5)
        total_data_number = generate_total_block_number()
        return_dict = {'block_data':block_data,'total_data_number':total_data_number} 
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

## 编辑板块页
def block_edit(request):
    if request.META['REQUEST_METHOD'] == 'GET':
        result = login_auto_check(request.session)
        if not result:
            return HttpResponseRedirect("../login")
        else:
            if request.GET.get('id'):
                block_data = select_block_byid(int(request.GET.get('id')))
                return render(request, 'blog/block-edit.html',{'block_data':block_data})
            else:
                #防止意外发生,以后修改成出错页
                raise Exception('ERROR when edit block')
    else:
        old_block_edit(int(request.POST.get('bid')),
            request.POST.get('title'),
            request.POST.get('description'),
            request.POST.get('remark'))
        return HttpResponse('T')

## 删除板块页        
def block_del(request):
    if request.META['REQUEST_METHOD'] == 'GET':
        raise Exception('ERROR because get method found when deleting block')
    else:
        if request.POST.get('bid'):
            result = old_block_del(int(request.POST.get('bid')))
            if result[0] == 'T':
                return HttpResponse(result)
            elif result[0] == 'F':
                return HttpResponse(result)
            else:
                raise Exception('ERROR when del block')
        else:
            return HttpResponse('F3')

## 添加文章页
def article_add(request):
    if request.META['REQUEST_METHOD'] == 'GET':
        result = login_auto_check(request.session)
        if not result:
            return HttpResponseRedirect("../login")
        else:
            block_data = select_block_all()
            return render(request, 'blog/article-add.html',{'block_data':block_data})
    else:
        new_article_add(request.POST.get('blockid'),
            request.POST.get('title'),
            request.POST.get('content'),
            request.POST.get('remark'))
        return HttpResponse('T')

## 文章列表页
def article_list(request):
    result = login_auto_check(request.session)
    if not result:
        return HttpResponseRedirect("../login")
    else:
        if request.GET.get('page'):
            present_page = int(request.GET.get('page'))
        else:
            present_page = 1
        if request.GET.get('bid'):
            bid = int(request.GET.get('bid'))
        else:
            bid = 0
        block_data = select_block_all()
        article_data = select_article_bytime(bid,(10*present_page-10,10*present_page))
        page_data = generate_article_page(bid,10,present_page,5)
        total_data_number = generate_total_article_number(bid)
        return_dict = {'block_data':block_data,'presentbid':bid,
                'article_data':article_data,'total_data_number':total_data_number} 
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
        return render(request, 'blog/article-list.html',return_dict)        

## 编辑文章页
def article_edit(request):
    if request.META['REQUEST_METHOD'] == 'GET':
        result = login_auto_check(request.session)
        if not result:
            return HttpResponseRedirect("../login")
        else:
            if request.GET.get('id'):
                article_data = select_article_byid(int(request.GET.get('id')))
                block_data = select_block_all()
                return render(request, 'blog/article-edit.html',
                        {'article_data':article_data,'block_data':block_data})
            else:
                #防止意外发生,以后修改成出错页
                raise Exception('ERROR when edit article')
    else:
        old_article_edit(int(request.POST.get('aid')),
            request.POST.get('blockid'),
            request.POST.get('title'),
            request.POST.get('content'),
            request.POST.get('remark'))
        return HttpResponse('T')        

## 删除文章页
def article_del(request):
    if request.META['REQUEST_METHOD'] == 'GET':
        raise Exception('ERROR because get method found when deleting article')
    else:
        if request.POST.get('aid'):
            result = old_article_del(int(request.POST.get('aid')))
            if result[0] == 'T':
                return HttpResponse(result)
            elif result[0] == 'F':
                return HttpResponse(result)
            else:
                raise Exception('ERROR when del article')
        else:
            return HttpResponse('F2')
        
## ckeditor上传图片,这里关掉csrf
@csrf_exempt
def ck_upload_img(request):
    if request.method == 'POST':
        callback = request.GET.get('CKEditorFuncNum')  
        f = request.FILES["upload"]
        if not f:
            res = "<script>window.parent.CKEDITOR.tools.callFunction("+callback+",'/"+"NO FILE"+"', '');</script>"
            return HttpResponse(res)
        else:
            code,para = ck_deal_img(f)
        if not code:
            res = "<script>window.parent.CKEDITOR.tools.callFunction("+callback+",'/"+para+"', '');</script>"
            return HttpResponse(res)
        else:
            res = "<script type=\"text/javascript\">" + \
                "window.parent.CKEDITOR.tools.callFunction(" + callback + ",''," + "'" + para + "'" + ");" + \
                "</script>"
            return HttpResponse(res)
    else:
        raise Exception("This method shouldn't be GET!!!")
