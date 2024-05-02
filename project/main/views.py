
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User  # 추가된 import

from .models import Post

# Create your views here.

def mainpage(request):
    return render(request, 'main/mainpage.html')

def secondpage(request):
    posts = Post.objects.all()
    return render(request, 'main/secondpage.html', {'posts': posts})

def new_post(request):
    return render(request, 'main/new-post.html')

def detail(request, id):  # detail 함수의 매개변수 이름을 id로 수정
    post = get_object_or_404(Post, pk=id)
    return render(request, 'main/detail.html', {'post': post})

def edit(request, id):
    edit_post = Post.objects.get(pk=id)
    return render(request, 'main/edit.html', {'post': edit_post})

def create(request):
    new_post = Post()

    new_post.title = request.POST['title']
    writer_username = request.POST['writer']  # 사용자 이름을 받아옴
    new_post.sex = request.POST['sex']
    new_post.body = request.POST['body']
    new_post.pub_date = timezone.now()
    new_post.image = request.FILES.get('image')

    # 사용자 이름으로 해당 사용자를 가져옴
    writer = User.objects.get(username=writer_username)
    new_post.writer = writer  # 사용자 인스턴스를 할당

    new_post.save()

    return redirect('main:detail', id=new_post.id)  # id 매개변수 추가

def update(request, id):
    update_post = Post.objects.get(pk=id)

    update_post.title = request.POST['title']
    writer_username = request.POST['writer']  # 사용자 이름을 받아옴
    update_post.sex = request.POST['sex']
    update_post.body = request.POST['body']
    update_post.pub_date = timezone.now()

    # 사용자 이름으로 해당 사용자를 가져옴
    writer = User.objects.get(username=writer_username)
    update_post.writer = writer  # 사용자 인스턴스를 할당

    if request.FILES.get('image'):
        update_post.image = request.FILES['image']

    update_post.save()

    return redirect('main:detail', id=update_post.id)  # id 매개변수 추가

def delete(request, id):
    delete_post = Post.objects.get(pk=id)
    delete_post.delete()
    return redirect('main:secondpage')
