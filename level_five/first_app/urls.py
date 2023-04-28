from django.urls import path, include
from first_app import views

app_name = 'first_app'

urlpatterns = [
    path('', views.register, name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('logout/', views.user_logout, name='logout'),
]
