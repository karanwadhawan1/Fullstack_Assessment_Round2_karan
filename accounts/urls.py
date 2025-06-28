from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('ajax-login/', views.ajax_login, name='ajax_login'),
]
