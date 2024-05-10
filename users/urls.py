from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('',views.user_list_api_view, name='user-list'), 
    path('<int:user_id>/',views.user_retrieve_api_view, name='user-retrieve'), 
    path('login/',views.login_api_view, name='login_api_view'), 
       
]