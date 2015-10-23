from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    # urls for loging in users
    url(r'^login', views.login_view, name='login'),
    url(r'^logout', views.logout_view, name='logout'),
    url(r'^authenticate$', views.authenticate_view, name='authenticate'),

    # look at pressings/records in the database
    url(r'^records/view\+all/?', views.all_records, name='all_records'),
    url(r'^records/view/(?P<pk>[0-9]+)/?', views.AlbumDetailView.as_view(), name='album_detail'),
    url(r'^records/view/pressing/(?P<pk>[0-9]+)/?', views.PressingDetailView.as_view(), name='pressing_detail'),
    url(r'^albums/create/?', views.create_album, name='create_album'),
    url(r'^albums/process/?', views.process_album, name='process_album'),

    # look at information about artists
    url(r'^artists/view\+all/?', views.ArtistListView.as_view(), name='all_artists'),
    url(r'^artists/view/(?P<pk>[0-9]+)/?', views.ArtistDetailView.as_view(), name='artist_detail'),
    url(r'^artists/create/?', views.create_artist, name='create_artist'),
    url(r'^artists/process/?', views.process_artist, name='process_artist'),

    # modify/view personal user information
]
