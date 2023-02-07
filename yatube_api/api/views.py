from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions

from posts.models import Post, Group

from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters
from .permission import IsAuthorOrReadOnlyPermission
from .serializers import (
    PostSerializer, GroupSerializer, CommentSerializer, FollowSerializer)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnlyPermission)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnlyPermission)

    def get_post(self):
        post = get_object_or_404(Post, id=self.kwargs.get('id'))
        return post

    def get_queryset(self):
        post = self.get_post()
        return post.comments.all()

    def perform_create(self, serializer):
        serializer.save(
            post=self.get_post(), author=self.request.user)


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = FollowSerializer
    http_method_names = ['get', 'post']
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'following__username')

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
