from django.urls import path
from django.conf.urls import include, url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    url(r'api/v1/foods/', view=views.FoodViewSet.as_view({'get': 'food'}), name='food')
]