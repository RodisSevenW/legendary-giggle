from django.urls import path,re_path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('jsj/', views.jsj_views, name='jsj'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.logout_view, name='logout'),
    path('sc/secondary_page/', views.user_list, name='secondary_page'),
    path('sc/guessnumber/', views.Guess_the_numbers, name='guessnumber'),
    re_path(r'^.*$', views.home_view),  # 通配符URL，将未匹配的URL重定向到主页
]


