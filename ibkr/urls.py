from django.urls import path

from ibkr.views import (
    GroupDetailView,
    GroupListView,
    GroupsCreateView,
    TradeDetailView,
    TradeListView,
)

app_name = "ibkr"

urlpatterns = [
    path("groups/", GroupListView.as_view(), name="group-list"),
    path("groups/create", GroupsCreateView.as_view(), name="group-create"),
    path("groups/<int:pk>", GroupDetailView.as_view(), name="group-detail"),
    path("trades/", TradeListView.as_view(), name="trade-list"),
    path("trades/<int:pk>", TradeDetailView.as_view(), name="trade-detail"),
]
