from django.urls import path

from .views import AuthedUserView

urlpatterns = [
    path('authed/', AuthedUserView.as_view(), name='get_authed_user'),
]
