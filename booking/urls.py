from django.conf.urls import url
from .views import (
    booker_view,
    program_view,
    booking_view,
    technician_view,
    artist_manager_view
)


urlpatterns = [
    url(r'^booking/$', booking_view, name='booking'),
    url(r'^program/$', program_view, name='program'),
    url(r'^technician/$', technician_view, name='technician_view'),
    url(r'^booker/$', booker_view, name='booker'),
    url(r'^artist_manager/$', artist_manager_view, name='artist_manager'),
]
