from rest_framework.routers import DefaultRouter
from .apiviews import *
from django.urls import path , re_path
from . import views
router = DefaultRouter()
router.register('user',ProfileViewSet,)

urlpatterns = [
        path("login", views.login, name="login"),
]


urlpatterns += router.urls