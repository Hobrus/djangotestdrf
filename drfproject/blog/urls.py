from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import PostsViewSet\
    ,CSRFTokenView

router = DefaultRouter()
router.register('posts', PostsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('api/token/', obtain_auth_token, name='obtain-token')
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('csrf/', CSRFTokenView.as_view(), name='csrf_token'),
]
