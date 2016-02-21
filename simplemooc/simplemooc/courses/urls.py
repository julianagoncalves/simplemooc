from django.conf.urls import url


urlpatterns = [
    url(r'^$', 'simplemooc.courses.views.index', name="index"),
]
