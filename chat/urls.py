from django.urls import path
from .views import signup_func, signin_func, listview_func

urlpatterns = [
    path('signup/', signup_func, name='signup'),
    path('signin/', signin_func, name='signin'),
    path('list/', listview_func, name='list'),
]
