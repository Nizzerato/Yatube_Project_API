from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CommentViewSet, FollowViewSet,
                    GroupViewSet, PostViewSet)

router1 = DefaultRouter()
router1.register(r'posts', PostViewSet, basename='posts')
router1.register(r'groups', GroupViewSet, basename='groups')
router1.register(r'groups/(?P<group_id>\d+)',
                 GroupViewSet, basename='group')
router1.register(r'posts/(?P<post_id>\d+)/comments',
                 CommentViewSet, basename='comments')
router1.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
