from django.conf.urls import url

from user_address import views

urlpatterns = [
    url(r'users/$', view=views.UserViewSet.as_view(
        actions={'post': 'register_login'}
    )),
    url(r'address/$', view=views.AddressViewSet.as_view(
        actions={'post': 'create_address', 'get': 'show_address'}
    )),
    url(r'address/(?P<pk>\d+)/$', view=views.AddressViewSet.as_view(
        actions={'delete': 'del_address'}
    )),
]
