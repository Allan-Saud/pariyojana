from django.urls import path
from .views import CustomTokenObtainPairView, ForgotPasswordView, ResetPasswordView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset_password'),
    path('reset-password/<int:user_id>/', ResetPasswordView.as_view(), name='admin_reset_password'),

]
