from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('editprofile/', views.EditProfile.as_view(), name='editprofile'),
    #path('editprofile/', views.edit_profile_view, name = 'editprofile'), 
    path('success/', views.success, name = 'success'), 
]
