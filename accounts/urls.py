from django.urls import path
from . import views
from .views import dashboard_view

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
