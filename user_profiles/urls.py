from django.conf.urls import url
import views

urlpatterns = [

    url(r'^profile$', views.profile, name='Generic Profile'),
    url(r'^update$', views.update_profile, name='Update Profile')
]
#    url(r'^myprofile$', views.myprofile, name='Logged In User Profile')
#]