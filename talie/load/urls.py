from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.load, name="chargement"),
    url(r'^loadHTML$', views.loadHTML, name="chargement_HTML"),
    url(r'^associations$', views.associations, name="entites associees"),
]
