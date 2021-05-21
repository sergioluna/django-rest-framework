from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register views with it
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

