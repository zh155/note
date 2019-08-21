from django.conf.urls import url

from study_serializers import views

urlpatterns = [
    url(r'person/', views.PersonView.as_view()),
    url(r'personmodel/', views.PersonModel.as_view()),
]
