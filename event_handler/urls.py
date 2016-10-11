from django.conf.urls import url

from views import CreateEventView


urlpatterns = [
    url(r'^update$', CreateEventView),
]
