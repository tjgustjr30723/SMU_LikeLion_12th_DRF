from django.urls import path
from .views import ProfileAPIView
from users import views

app_name = 'users'

urlpatterns = [
    path('',views.UserListCreateAPIView.as_view(), name='user-list'), 
    path('profile/', ProfileAPIView.as_view(), name='profile'),
    path('login/',views.LoginAPIView.as_view(), name='login_api_view'), 
    path('change_password/',views.ChangePasswordAPIView.as_view(), name='change_password_api_view_api_view'), 
    path('reset_password/',views.ResetPasswordAPIView.as_view(), name='reset_password_api_view'),
]