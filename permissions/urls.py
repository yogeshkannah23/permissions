from django.urls import path
from permissions import views

urlpatterns = [
    path('',views.PostAddList.as_view(),name='index'),  
    path('list/',views.PostList.as_view(),name='post-list')
]