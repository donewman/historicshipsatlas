from django.conf.urls import url
from atlas import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ship/(?P<slug>[\w-]+)/$', views.ShipDetailView.as_view(), name='ship_detail'),
    url(r'^ships/$', views.ShipListView.as_view(), name='ships'),
    url(r'^type/(?P<slug>[\w-]+)/$', views.TypeDetailView.as_view(), name='type_detail'),
    url(r'^city/(?P<slug>[\w-]+)/$', views.CityDetailView.as_view(), name='city_detail'),
    url(r'^country/(?P<slug>[\w-]+)/$', views.CountryDetailView.as_view(), name='country_detail'),
    url(r'^status/(?P<slug>[\w-]+)/$', views.StatusDetailView.as_view(), name='status_detail'),
    url(r'^use/(?P<slug>[\w-]+)/$', views.UseDetailView.as_view(), name='use_detail'),
    url(r'^owner/(?P<slug>[\w-]+)/$', views.OwnerDetailView.as_view(), name='owner_detail'),
]
