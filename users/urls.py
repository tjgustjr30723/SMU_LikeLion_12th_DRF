from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('',views.user_list_api_view, name='user-list'), 
    path('profile/',views.profile_api_view, name='profile_api_view'), 
    path('login/',views.login_api_view, name='login_api_view'), 
    path('change_password/',views.change_password_api_view, name='change_password_api_view_api_view'), 
    path('reset_password/',views.reset_password_api_view, name='reset_password_api_view'),
]