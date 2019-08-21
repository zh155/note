from django.conf.urls import url, include
from rest_framework import routers

from register_login import views

router = routers.DefaultRouter()
router.register(r'register_login_viewset', views.RegisterLoginViewSet)

urlpatterns = [
                  url(r'register_login_apiview/', view=views.RegisterLoginAPIView.as_view()),
                  url(r'register_login_apiview/(?P<pk>\d+)', view=views.RegisterLoginAPIView.as_view()),
                  # url(r'register_login_viewset/', view=views.RegisterLoginViewSet.as_view(
                  #     actions={
                  #         'post': 'register_login'
                  #     }
                  # ))
              ] + router.urls
# urlpatterns = router.urls
