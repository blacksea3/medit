from django.shortcuts import render
from blog.models import *

# Create your views here.
def test(request):
    objects = Blog.objects.all()

    return render(request, 'blog/ckeditor_test.html',{
        #'tip':tip,
        #'status':status,
        #'logged':logged,
        })
