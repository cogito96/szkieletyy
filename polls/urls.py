from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^home/', views.home_view, name='home'),
    url(r'^base/', views.base_view, name='base'),
    url(r'^$',views.home_view),
    url(r'^players/',views.show_player, name='show_player'),
    url(r'^teams/',views.show_teams, name='show_teams'),
    url(r'^match/',views.show_match, name='show_match'),
    url(r'^action/',views.show_action, name='show_action'),
    url(r'^table/',views.show_table, name='show_table'),
    url(r'^statistic/',views.show_statistic, name='show_statistic'),
    url(r'^results/',views.show_all_statistic, name='show_all_statistic'),
]
