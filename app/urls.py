from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('update/<str:ip>', Update.as_view(), name='update'),
]