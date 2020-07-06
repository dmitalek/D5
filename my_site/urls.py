from django.contrib import admin
from django.urls import path
from p_library.views import  AuthorEdit, AuthorList, BookEdit, FriendList, FriendUpdate, FriendEdit, Publisher
from p_library import views

app_name = 'p_library'
urlpatterns = [
        path('admin/', admin.site.urls),
        path('', views.books_list),
        path('index/', views.index),
        path('author/create', AuthorEdit.as_view(), name='author_create'),
        path('author/', AuthorList.as_view(), name='author_list'),
        path('book/create', BookEdit.as_view(), name='book_create'),
        path('friends', FriendList.as_view(), name='friend_list'),
        path('<pk>/friend_update', FriendUpdate.as_view(), name='friend_update'),
        path('friend/create', FriendEdit.as_view(), name='friend_create'),
        path('maker', Publisher.as_view(), name='publish'),
]