from django.urls import path

from posts import views

app_name = 'posts'

urlpatterns = [
    path('',views.post_list_api_view, name='post-list'), 
    path('<int:post_id>/',views.post_retrieve_api_view, name='post-retrieve'), 
    path('likes/<int:post_id>/',views.likes_api_view, name='likes_api_view'), 
    path('users_post/',views.users_post_api_view, name='users_post_api_view'),    
]