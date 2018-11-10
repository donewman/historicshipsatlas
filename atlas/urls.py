from django.urls import path
from atlas import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ship/<int:pk>", views.ShipDetailView.as_view(), name="ship_detail"),
    path("ships/", views.ShipListView.as_view(), name="ships",)
]
