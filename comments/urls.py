from django.urls import path

from comments import views

app_name = 'comments'

urlpatterns = [
    path('',views.comment_list_api_view, name='comment-list'), 
    path('<int:comment_id>/',views.comment_retrieve_api_view, name='comment-retrieve'), 
    path('likes/<int:comment_id>/',views.likes_api_view, name='likes_api_view'), 
    path('posts/<int:post_id>/',views.comment_m_api_view, name='comment_m_api_view'), 
    
]