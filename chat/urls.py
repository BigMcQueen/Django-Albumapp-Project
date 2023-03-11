from django.urls import path
from .views import signup, signin

urlpatterns = [
    path('signup/', signup),
    path('signin/', signin),
]
