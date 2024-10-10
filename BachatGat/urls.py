from django.urls import *
from rest_framework.routers import DefaultRouter
from .views import *
from .serializers import *

router = DefaultRouter()
router.register("bachatgat", BachatGatRegistrationViewSet),
router.register("member_registration",MemberRegistrationViewSet),

urlpatterns = [
    *router.urls,
    path('',include(router.urls)),

]