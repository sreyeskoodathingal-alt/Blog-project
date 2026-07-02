from django.urls import path
from . import views

urlpatterns = [
    path('greetings/',views.greetings),
    path('basic/',views.basic),
    path('home/',views.home,name='home'),
    path('create_blog/',views.create_blog,name='create_blog'),
    path('update_blog/<int:blog_id>/',views.update_blog,name='update_blog'),
    path('delete_blog/<int:blog_id>/', views.delete_blog,name='delete_blog'),
    path('detail_blog/<int:blog_id>/', views.detail_blog,name='detail_blog'),
    path("register/", views.register_view, name="register_view"),
    path("", views.login_view, name="login"),
    path('logout', views.logout_view,name="logout"),
    
]
