from django.urls import path, include
from rest_framework import routers
from .views import AuthorModelView, CategoryModelView, BookModelView

router = routers.DefaultRouter()
router.register(r'authors', AuthorModelView)
router.register(r'authors', CategoryModelView)
router.register(r'authors', BookModelView)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls)),
    path('', include(router.urls))
]
