from django.urls import path
from .views import signup_func, signin_func, listview_func, signout_func

urlpatterns = [
    path('signup/', signup_func, name='signup'),
    path('signin/', signin_func, name='signin'),
    path('list/', listview_func, name='list'),
    path('signout/', signout_func, name='signout'),
]
