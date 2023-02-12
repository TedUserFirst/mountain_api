from django.urls import path, include, re_path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'peaks', views.PeakViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path('peaks/bounding_box/(?P<min_latitude>[\d.]+)/(?P<min_longitude>[\d.]+)/(?P<max_latitude>[\d.]+)/(?P<max_longitude>[\d.]+)/', views.PeakListInBoundingBox.as_view(), name='peak-list-in-bounding-box'),

]

