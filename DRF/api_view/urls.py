from django.conf.urls import url, include
from rest_framework import routers

from api_view import views

router = routers.DefaultRouter()
router.register(r'students', views.StudentModelViewSet)

urlpatterns = [
    url(r'index/', view=views.Index),
    url(r'api/', view=views.Api),
    url(r'apiview/', views.ApiView.as_view()),
    url(r'viewsets/', include(router.urls)),
    url(r'students/create/', views.StudentCreateAPIView.as_view()),
    url(r'students/list/', views.StudentListAPIView.as_view()),
    url(r'students/listcreate/', views.StudentListCreateAPIView.as_view()),
    url(r'students/retrieve/(?P<pk>\d+)', views.StudentRetrieveAPIView.as_view()),

    url(r'', include(router.urls)),
    # url(r'students/$', views.StudentModelViewSet.as_view(
    #     actions={
    #         'get': 'list',
    #         'post': 'create',
    #     }
    # )),
    # url(r'students/(?P<pk>\d+)', views.StudentModelViewSet.as_view(
    #     actions={
    #         'get': 'retrieve',
    #
    #     }
    # )),
]
