from django.urls import path
from .views import HomePage, DetailsPage, CreatePostPage, DeletePostPage, UpdatePostPage, CategoryView

urlpatterns = [
    path('', HomePage.as_view(), name='home-page'),
    path('/detail/<int:pk>', DetailsPage.as_view(), name='detail-page'),
    path('/create_post', CreatePostPage.as_view(), name='create-post-page'),
    path('/detail/<int:pk>/delete', DeletePostPage.as_view(), name='delete-post-page'),
    path('/detail/<int:pk>/edit', UpdatePostPage.as_view(), name='update-post-page'),
    path('category/<str:cat>/', CategoryView, name='category')
]
