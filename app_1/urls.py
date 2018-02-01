from django.conf.urls import url

from .views import ErrorView


urlpatterns = [
    url(r'^$', ErrorView.as_view(), name='error'),
]
