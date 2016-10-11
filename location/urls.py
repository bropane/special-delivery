from django.conf.urls import include, url

import views


urlpatterns = [
    url(r'^update$', views.UpdateLocationView),
]
