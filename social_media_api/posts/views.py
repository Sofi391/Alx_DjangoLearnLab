from rest_framework import viewsets
from rest_framework.generics import UpdateAPIView, ListAPIView
from .models import Post,Comment
from .serializers import PostSerializer, CommentSerializer,FollowSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth import get_user_model
from rest_framework.response import Response


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'
    pagination_class = PageNumberPagination
    # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['title','content']
    ordering_fields = ['created_at','updated_at']
    ordering_field = '-created_at'

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.query_params.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset

    def get_permissions(self):
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
        return [permissions() for permissions in permission_classes]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'comment_id'
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['content']
    ordering_fields = ['created_at','updated_at']
    ordering_field = '-created_at'

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

User = get_user_model()

class FollowView(UpdateAPIView):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # The object being updated is always the current user
        return self.request.user

    def perform_update(self, serializer):
        current_user = self.request.user
        target_user_id = serializer.validated_data['target_user_id']
        target_user = User.objects.get(id=target_user_id)

        if target_user in current_user.following.all():
            current_user.following.remove(target_user)
            action = 'unfollowed'
        else:
            current_user.following.add(target_user)
            action = 'followed'

        current_user.save()
        serializer.instance = current_user  # update the instance reference
        return action

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        action = self.perform_update(serializer)
        return Response({'status': action})


class FeedView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        following_users = self.request.user.following.all()
        queryset = Post.objects.filter(author__in=following_users).order_by('-created_at')
        return queryset

