
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User  # 추가된 import

from .models import Post, Comment, Tag

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
    if request.method == 'GET':
        comments = Comment.objects.filter(post=post)
        return render(request, 'main/detail.html', {'post': post, 'comments': comments})
    elif request.method == 'POST':
        new_comment = Comment()
        new_comment.post = post
        new_comment.writer=request.user
        new_comment.content=request.POST['content']
        new_comment.pub_date=timezone.now()

        new_comment.save()

        return redirect('main:detail', id)
    
def delete_comment(request, id):
    comment = get_object_or_404(Comment, pk=id)
    post_id = comment.post.id
    if request.user.is_authenticated and request.user == comment.writer:
        comment.delete()
    return redirect('main:detail', id=post_id)

def edit(request, id):
    edit_post = Post.objects.get(pk=id)
    return render(request, 'main/edit.html', {'post': edit_post})

def create(request):
    if request.user.is_authenticated:
        new_post=Post()

        new_post.title = request.POST['title']
        new_post.writer = request.user # 사용자 이름을 받아옴
        new_post.sex = request.POST['sex']
        new_post.body = request.POST['body']
        new_post.pub_date = timezone.now()
        new_post.image = request.FILES.get('image')

        new_post.save()

        words=new_post.body.split(' ')
        tag_list = []

        for w in words:
            if len(w)>0:
                if w[0] == '#':
                    tag_list.append(w[1:])

        for t in tag_list:
            tag, boolean = Tag.objects.get_or_create(name=t)
            new_post.tags.add(tag.id)

        return redirect('main:detail', id=new_post.id)  # id 매개변수 추가
    else:
        return redirect('accounts:login')


def update(request, id):
    update_post = Post.objects.get(pk=id)
    if request.user.is_authenticated and request.user == update_post.writer:
        update_post.title = request.POST['title']
        update_post.sex = request.POST['sex']
        update_post.body = request.POST['body']
        update_post.pub_date = timezone.now()


        if request.FILES.get('image'):
            update_post.image = request.FILES['image']

        update_post.save()
        return redirect('main:detail', id=update_post.id)  # id 매개변수 추가
    return redirect('accounts:login', id=update_post.id)

def delete(request, id):
    delete_post = Post.objects.get(pk=id)

    tags=delete_post.tags.all()
    for tag in tags:
        if tag.posts.count()==1:
            tag.delete()
    delete_post.delete()
    return redirect('main:secondpage')

def tag_list(request):
    tags=Tag.objects.all()
    return render(request, 'main/tag-list.html', { 'tags' : tags})

def tag_posts(request, tag_id):
    tag=get_object_or_404(Tag, id=tag_id)
    posts=tag.posts.all()
    return render(request, 'main/tag-post.html', {
        'tag' : tag,
        'posts' : posts,
    })
