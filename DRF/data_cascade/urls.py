from django.conf.urls import url

from data_cascade import views

urlpatterns = [
    url(r'users/$', view=views.UserAPIView.as_view()),

    # url(r'books/$', view=views.BookAPIView.as_view()),
    # url(r'books/(?P<pk>\d+)/$', view=views.BookAPIView.as_view()),

    url(r'books/$', view=views.BookViewSet.as_view(
        actions={'post': 'do_post', 'get': 'list'}
    )),
    url(r'books/(?P<pk>\d+)/$', view=views.BookViewSet.as_view(
        actions={'get': 'do_retrieve', 'delete': 'do_destroy'}
    )),
]
