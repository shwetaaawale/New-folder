from django.urls import path
from .views import RegisterView, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
 path('signup/', RegisterView.as_view(), name='signup'),
 path('login/', TokenObtainPairView.as_view(), name='login'),
 path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
 path('logout/', LogoutView.as_view(), name='logout'),
]
