from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .serializers import PostSerializer, PostListSerializer
from rest_framework import permissions
from ..models import Post


class PostListViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = Post.objects.select_related('category', 'author').filter(status='published').order_by('-created')
    serializer_class = PostSerializer

    """
        "List view"
        self.basename from urls.py  router.register("news", PostListViewSet, basename="news")
    """
    def list(self, request, *args, **kwargs):
        if self.basename == 'all':
            queryset = self.queryset
        else:
            queryset = Post.objects.select_related('category', 'author').filter(category__slug=self.basename,
                                                                            status='published').order_by('-created')
        serializer = PostListSerializer(queryset, many=True)
        return Response(serializer.data)

# TODO разобраться
    @action(detail=True, methods=['get', 'post'])
    def my_custom_action(self, request, pk=None):
        instance = self.get_object()
        # do something with the instance
        return Response({'detail': 'Custom action completed'})

