from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index, name='index'),
    path('login/',auth_views.login,{'template_name':'arki/login.html'}, name='login'),
    path('logout/',auth_views.logout,{'next_page': '/arki'}, name='logout'),
]