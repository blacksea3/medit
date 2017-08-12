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
			return HttpResponseRedirect("http://www.baidu.com")
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
				request.session.set_expiry(0)
			return HttpResponse('T')
		elif result == 'F1' or result == 'F0':
			return HttpResponse(result)
		else:	
			return HttpResponse('F2')

			
			