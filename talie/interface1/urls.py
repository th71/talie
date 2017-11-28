from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^load$', views.load, name="chargement"),
    url(r'^virgilius$', views.virgilius, name='virgilus'),
    url(r'^virgilius/([0-9]+)/$', views.virgiliusL, name='virgilus'),
    url(r'^virgilius/([0-9]+)/([0-9]+)$', views.virgiliusC, name='virgilus'),
]
