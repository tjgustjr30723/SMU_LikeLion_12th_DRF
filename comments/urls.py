from django.urls import path

from comments import views

app_name = 'comments'

urlpatterns = [
    path('',views.comment_list_api_view, name='comment-list'), 
    path('<int:comment_id>/',views.comment_retrieve_api_view, name='comment-retrieve'), 
    
       
]