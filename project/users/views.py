from django.shortcuts import render
from main.models import Post

# Create your views here.
def mypage(request):
    user_posts = Post.objects.filter(writer=request.user) 
    return render(request, 'users/mypage.html', {'user_posts': user_posts})
