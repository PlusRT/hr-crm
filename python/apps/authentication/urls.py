from django.urls import path

from apps.authentication.views import AndroidAuthenticationView, ConvertRoleTokenView

urlpatterns = [
    path('auth/android', AndroidAuthenticationView.as_view()),
    path('auth/convert-role-token', ConvertRoleTokenView.as_view(), )
]
