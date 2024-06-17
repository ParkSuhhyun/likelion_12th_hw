from django.urls import path
from .views import *

<<<<<<< HEAD:accounts/urls.py

app_name = "accounts"
urlpatterns = [
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('signup/', signup, name="signup"),

=======
app_name="main"
urlpatterns=[
    path('', mainpage, name="mainpage"),
    path('second', secondpage, name="secondpage"),
    path('new-post', new_post, name="new-post"),
    path('create', create, name="create"),
    path('<int:id>', detail, name="detail"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
    path('tag-list', tag_list, name="tag-list"),
    path('tag-posts/<int:tag_id>', tag_posts, name="tag-posts"),
    path('comment/delete/<int:id>/', delete_comment, name='delete-comment'),
    path('likes/<int:post_id>', likes, name="likes"),
>>>>>>> 3f86284a02f54f474f6cae9e9dcb2c5d12b065e9:project/main/urls.py
]