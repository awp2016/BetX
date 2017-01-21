from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^pronosticuri/$', views.pronosticuri, name='pronosticuri'),
    url(r'^(?P<pronostic_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<pronostic_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<pronostic_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^signup', views.signup, name="signup"),
    url(r'^home', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^user_profile/(?P<pk>\d+)/$', views.UserProfileView.as_view(),
        name="user_profile"),
    url(r'^user-profile/(?P<pk>\d+)/edit/$', views.UserProfileUpdate.as_view(),
        name="edit_profile")
]
