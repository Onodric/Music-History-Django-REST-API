from django.conf.urls import url, include
from music_history_api.views import *
from rest_framework.routers import DefaultRouter
from django.contrib import admin

# Create a router, using DefaultRouter
# Register each ViewSet with it.
router = DefaultRouter()
router.register(r'users', user_view.UserViewSet)
router.register(r'artists', artist_view.ArtistViewSet)
router.register(r'albums', album_view.AlbumViewSet)
router.register(r'songs', song_view.SongViewSet)
router.register(r'genres', genre_view.GenreViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
