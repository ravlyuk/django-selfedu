from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from women.views import *

# router = routers.DefaultRouter()
# router.register(r'women', WomenViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/', include(router.urls)),

    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/women/', WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>', WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>', WomenAPIDestroy.as_view()),

    # djoser
    path('api/v1/auth/', include('djoser.urls')),
    # http://127.0.0.1:8000/auth/token/login/ {"username": "vivex","password": "vivexpass1"}
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    # jwt
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
