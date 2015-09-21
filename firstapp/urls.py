from django.conf.url import url
from . import views

urlpatterns = [

  url(r'^$', views.post_list, name='home-template'),

]