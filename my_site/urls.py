
from django.contrib import admin
from django.urls import path, include
from p_library.views import AuthorEdit, AuthorList, author_create_many, books_authors_create_many
from p_library import views

app_name = 'p_library'
urlpatterns = [
        
        path('admin/', admin.site.urls),
        
        path('', views.FriendList),
        path('author/', AuthorList.as_view(), name='author_list'),
        
        
        path('friend/', views.FriendList),
]