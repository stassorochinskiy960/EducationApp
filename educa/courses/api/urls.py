from django.urls import re_path, include
from rest_framework import routers
from . import views

app_name = 'api'

router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet)

urlpatterns = [
    re_path(r'^subjects/$', views.SubjectListView.as_view(), name='subject_list'),
    re_path(r'^subjects/(?P<pk>\d+)/$', views.SubjectDetailView.as_view(), name='subject_detail'),
    re_path(r'^', include(router.urls)),
]
