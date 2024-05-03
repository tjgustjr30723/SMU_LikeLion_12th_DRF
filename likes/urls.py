from django.urls import path

from likes import views

urlpatterns = [
    path('',views.like_list_api_view, name='like-list'), 
    path('<int:pk>',views.like_retrieve_api_view, name='like-retrieve'), 
    
       
]