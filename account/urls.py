from django.urls import path
from .views import UsersInfo,UpdateUserInfo

urlpatterns = [

    path('all-users/', UsersInfo.as_view()),
    path('update-user/<int:pk>', UpdateUserInfo.as_view()),

]   
