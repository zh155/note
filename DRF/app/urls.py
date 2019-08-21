from django.conf.urls import url, include
from rest_framework import routers

from app import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'group', views.GroupViewSet)
router.register(r'books', views.BookViewSet)
urlpatterns = [
    url(r'index/', views.index),
    url(r'hello/', views.Hello.as_view(msg='zhangsan')),
    url(r'', include(router.urls)),
]
