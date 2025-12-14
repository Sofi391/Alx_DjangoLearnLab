from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet,FeedView,LikeView,UnLikeView

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='feed'),
    path('like/<int:pk>', LikeView.as_view(), name='like'),
    path('unlike/<int:pk>', UnLikeView.as_view(), name='unlike'),
]
