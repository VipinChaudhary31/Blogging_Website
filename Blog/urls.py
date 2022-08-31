from django.urls import path
# from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView,CategoryListView

urlpatterns = [
    # path('', views.Home,name="Home"),
    path('', HomeView.as_view(), name='Home'),
    path('Article/<int:pk>', ArticleDetailView.as_view(), name='Article_Detail'),
    path('Add_Blog/', AddPostView.as_view(), name='Add_Blog'),
    path('Add_category/', AddCategoryView.as_view(), name='Add_category'),
    path('Article/Edit/<int:pk>', UpdatePostView.as_view(), name='Update_Post'),
    path('Article/<int:pk>/remove', DeletePostView.as_view(), name='Delete_Post'),
    path('category/<str:cats>', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),

]
