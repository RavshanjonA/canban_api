from django.urls import path

from apps.users.api_endpoints.User.User_Destroy.views import UserDestroyAPIView
from apps.users.api_endpoints.User.User_List.views import UserListAPIView
from apps.users.api_endpoints.User.User_Login_Logout.views import LoginAPIView, LogoutAPIView
from apps.users.api_endpoints.User.User_Register.views import UserRegisterAPIView
from apps.users.api_endpoints.User.User_Retrieve.views import UserRetrieveAPIView
from apps.users.api_endpoints.User.User_Update.views import UserUpdateAPIView

app_name = 'users'

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='user_register'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('login/', LoginAPIView.as_view(), name='user_login'),
    path('logout/', LogoutAPIView.as_view(), name='user_logout'),
    path('all-users/', UserListAPIView.as_view(), name='user_list'),
    path('all-users/<int:pk>/', UserRetrieveAPIView.as_view(), name='user_detail'),
    path('delete-user/<int:pk>/', UserDestroyAPIView.as_view(), name='user_delete'),
]
