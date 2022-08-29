from django.urls import path
# from . import views
from .views import HomeView, ArticleDetailView

urlpatterns = [
    # path('', views.Home,name="Home"),
    path('', HomeView.as_view(), name='Home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
]
