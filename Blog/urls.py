from django.urls import path
# from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    # path('', views.Home,name="Home"),
    path('', HomeView.as_view(), name='Home'),
    path('Article/<int:pk>', ArticleDetailView.as_view(), name='Article_Detail'),
    path('Add_Blog/', AddPostView.as_view(), name='Add_Blog'),
    path('Article/Edit/<int:pk>', UpdatePostView.as_view(), name='Update_Post'),
    path('Article/<int:pk>/remove', DeletePostView.as_view(), name='Delete_Post')

]
