from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login_page, name='login_page'),
    url(r'^$', views.form_list, name='form_list'),
    # url(r'^$', views.blank, name='blank'),
    url(r'^', views.form, name='form'),
    url(r'^form_validation/', views.form_validation, name='form_validation$'),
]
