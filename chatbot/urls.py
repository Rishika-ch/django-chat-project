from django.contrib import admin
from django.urls import path
from chatbot import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('chatbot/', views.chatbot_response, name='chatbot'),
]
