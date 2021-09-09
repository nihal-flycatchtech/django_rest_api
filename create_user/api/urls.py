from django.urls import path
from create_user.api.views import Registration_view,HelloView

app_name='create_user'

urlpatterns=[
    path('register',Registration_view.as_view(),name="register"),
    path('view',HelloView.as_view(),name="view")
]