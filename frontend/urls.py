from django.conf.urls import url
from django.shortcuts import redirect

from . import views


urlpatterns = [
    url(r'^images/(.*)$', views.redirect_images_to_media, name=''),
    url(r'^i18n.json$', lambda request: redirect("/static/i18n.json"), name=''),
    url(r'^config.json$', lambda request: redirect("/static/config.json"), name=''),
    url(r'^_pages/(.*)$', views.get_raw_markdown, name=''),
    url(r'^submit_page_change$', views.submit_page_change, name=''),
    url(r'^(.*)$', views.get_page, name=''),
]
