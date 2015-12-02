from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),

    # urls for loging in users
    url(r'^login', views.login_view, name='login'),
    url(r'^logout', views.logout_view, name='logout'),
    url(r'^authenticate', views.authenticate_view, name='authenticate'),

    # urls creating users
    url(r'^join', views.join_user, name='join_user'),
    url(r'^create', views.create_user, name='create_user'),
    url(r'^edit', views.edit_user, name='edit_user'),
    url(r'^update', views.update_user, name='update_user'),

    # look at/modify albums in the database
    url(r'^records/view\+all', views.all_records, name='all_records'),
    url(r'^records/view/(?P<pk>[0-9]+)', views.AlbumDetailView.as_view(), name='album_detail'),
    url(r'^albums/create', views.create_album, name='create_album'),
    url(r'^albums/update/(?P<pk>[0-9]+)', views.update_album, name='update_album'),
    url(r'^albums/process', views.process_album, name='process_album'),

    # look at/modify pressings in the database
    url(r'^records/view/pressing/(?P<pk>[0-9]+)', views.PressingDetailView.as_view(), name='pressing_detail'),
    url(r'^pressings/create/(?P<album_id>[0-9]+)', views.create_pressing, name='create_pressing'),
    url(r'^pressings/process', views.process_pressing, name='process_pressing'),

    # look at information about artists
    url(r'^artists/view\+all', views.ArtistListView.as_view(), name='all_artists'),
    url(r'^artists/view/(?P<pk>[0-9]+)', views.ArtistDetailView.as_view(), name='artist_detail'),
    url(r'^artists/create', views.create_artist, name='create_artist'),
    url(r'^artists/update/(?P<pk>[0-9]+)', views.update_artist, name='update_artist'),
    url(r'^artists/process', views.process_artist, name='process_artist'),

    # modify/view personal user information
    url(r'^collection/view', views.view_collection, name='view_collection'),
    url(r'^collection/add', views.add_to_collection, name='add_to_collection'),
    url(r'^collection/delete', views.delete_collection, name='delete_collection'),
    url(r'^profile/view', views.view_profile, name='view_profile'),

    # create and process new record labels
    url(r'^record\+label/create', views.create_record_label, name='create_record_label'),
    url(r'^record\+label/process', views.process_record_label, name='process_record_label'),

    # view users
    url(r'^users/view', views.UserListView.as_view(), name='all_users'),
    url(r'^users/(?P<pk>.*)', views.UserDetailView.as_view(), name='user_detail'),
]
