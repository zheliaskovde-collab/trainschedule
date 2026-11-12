from django.contrib import admin
from django.urls import path
from core import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls), #панель адмініістратора, інетрфейс від django
    path('', views.home_view, name='home'),#домашня сторінка
    path('register/', views.register_view, name='register'), #вікно реєстрації
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'), #вікно входу
    path('logout/', LogoutView.as_view(), name='logout'), #
    path('schedule/', views.schedule_list_view, name='schedule_list'), #

]
