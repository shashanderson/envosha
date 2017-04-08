from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.form_list, name='form_list'),
]