from django.urls import path

from users import views

urlpatterns = [
    path('',views.user_list_api_view, name='user-list'), 
    path('<int:pk>',views.user_retrieve_api_view, name='user-retrieve'), 
    
       
]