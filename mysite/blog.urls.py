from django.conf.urls import url
from . import views
#import mysite

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]