from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from .forms import BlogForm

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details':details})

#CREATE 버튼 누름에 대해 작동하는 함수
def new(request):
    if request.method == 'POST':
        forms = BlogForm(request.POST)

        if forms.is_valid:
            forms.save()
            return redirect('home')
    forms = BlogForm()
    return render(request,'new.html',{'forms':forms})


#수정하기에 대해 작동하는 함수
def update(request,blog_id):
    blog_edit=get_object_or_404(Blog,id=blog_id)
    if request.method == 'POST':
        forms = BlogForm(request.POST,instance=blog_edit)
        if forms.is_valid:
            forms.save()
            return redirect('home')
        
    forms = BlogForm(instance=blog_edit)
    return render(request,'new.html',{'forms':forms})

def delete(request, blog_id):
    blog_delete = get_object_or_404(Blog, id = blog_id)
    blog_delete.delete()
    return render(request, 'home.html')