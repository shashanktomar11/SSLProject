from django.urls import path
from .views import SignUpView

from django.contrib.auth import views

from .views import CreatePostView # new

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('post/', CreatePostView.as_view(), name='add_post')
]
