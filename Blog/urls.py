from django.urls import path
# from . import views
from .views import HomeView, ArticleDetailView, AddPostView

urlpatterns = [
    # path('', views.Home,name="Home"),
    path('', HomeView.as_view(), name='Home'),
    path('Article/<int:pk>', ArticleDetailView.as_view(), name='Article_Detail'),
    path('Add_Blog/', AddPostView.as_view(), name='Add_Blog')
]
