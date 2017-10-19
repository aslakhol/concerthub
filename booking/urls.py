from django.conf.urls import url
from .views import (
    booker_view,
    program_view,
    booking_manager_view,
    technician_view,
    artist_manager_view,
    organizer_view,
    BookingUpdate,
)


urlpatterns = [
    url(r'^program/$', program_view, name='program'),

    url(r'^organizer_overview/$', organizer_view, name='organizer_view'),
    url(r'^booking_overview/$', booking_manager_view, name='booking_manager_view'),
    url(r'^booking/$', booker_view, name='booker_view'),
    url(r'^work_hours/$', technician_view, name='technician_view'),
    url(r'^offers_concerts/$', artist_manager_view, name='artist_manager_view'),

    url(r'^offers_concerts/(?P<pk>\w+)/update/$', BookingUpdate.as_view()),

    # url(r'^timeslot/(?P<pk>w+)/create/$', TimeSlotCreate)
]
