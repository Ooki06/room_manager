from django.conf.urls import url

from . import views

app_name = 'room_manager'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^yoyaku/$', views.YoyakuView.as_view(), name='yoyaku'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^table/$', views.TableView.as_view(), name='table'),
    url(r'^yoyakudel/$', views.YoyakudelView.as_view(), name='yoyakudel'),
    url(r'^zikanwari/$', views.ZikanwariView.as_view(), name='zikanwari'),
]
