from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^Home/$', views.MatchListView.as_view(), name='Home'),
    url(r'^Match/(?P<pk>[0-9]+)/$', views.PronosticuriListView.as_view(), name='pronosticuri'),
    url(r'^Match/Details/(?P<pk>[0-9]+)/$', views.PronosticDetailView.as_view(), name='details'),
    url(r'^signup', views.signup, name="signup"),
    url(r'^Login', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^user_profile/(?P<pk>\d+)/$', views.UserProfileView.as_view(),
        name="user_profile"),
    url(r'^user-profile/(?P<pk>\d+)/edit/$', views.UserProfileUpdate.as_view(),
        name="edit_profile"),
     url(r'^Match/Details/(?P<pk>[0-9]+)/comment/add/$', views.AddComment.as_view(), name='addcomment'),
]
