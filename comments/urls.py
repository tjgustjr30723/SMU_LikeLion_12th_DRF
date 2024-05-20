from comments import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet
# app_name = 'comments'

router = DefaultRouter()
router.register(r'', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('<int:post_id>/create/', CommentViewSet.as_view({'post': 'create_comment'}), name='create-comment')
]
# urlpatterns = [
#     path('',views.comment_list_api_view, name='comment-list'), 
#     path('<int:comment_id>/',views.comment_retrieve_api_view, name='comment-retrieve'), 
#     path('likes/<int:comment_id>/',views.likes_api_view, name='likes_api_view'), 
#     path('posts/<int:post_id>/',views.comment_m_api_view, name='comment_m_api_view'), 
    
# ]