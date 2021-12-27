from django.urls import path, include

from . import views

# from django.urls import path, include

urlpatterns = [
    path('login_user/', views.login_user,name='login_user')

]
