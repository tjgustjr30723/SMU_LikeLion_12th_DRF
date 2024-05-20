from django.urls import path

from posts import views

app_name = 'posts'

urlpatterns = [
    path('',views.PostListCreateAPIView.as_view(), name='post-list'), 
    path('<int:post_id>/',views.PostRetrieveAPIView.as_view(), name='post-retrieve'), 
    path('likes/<int:post_id>/',views.LikesAPIView.as_view(), name='likes_api_view'), 
    path('users_post/',views.UserPostsAPIView.as_view(),name='users_post_api_view'),    
]