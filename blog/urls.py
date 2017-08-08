
from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^faq/$', views.FaqView.as_view(), name='faq'),
    url(r'^terms/$', views.TermsView.as_view(), name='terms'),
    url(r'^privacy/$', views.PrivacyView.as_view(), name='privacy'),
]