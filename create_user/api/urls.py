from django.urls import path
from create_user.api.views import RegistrationView, HelloView

app_name = 'create_user'

urlpatterns = [
    path('register', RegistrationView.as_view(), name="register"),
    path('view', HelloView.as_view(), name="view")
]
