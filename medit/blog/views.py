from django.shortcuts import render
from blog.models import *

#from blog.user import login_verify

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
		return render(request, 'blog/login.html',{
			#'tip':tip,
			#'status':status,
			#'logged':logged,
			})
	else:
		raise Exception('This is a POST request?!')
	#if request.
	
	#result = login_verify(request)
	