from typing import T

import django_filters
import django_filters.views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from ibkr.filter_sets import TradeListFilterSet
from ibkr.forms import GroupForm, TradeForm
from ibkr.models import Group, Trade


class GroupListView(LoginRequiredMixin, ListView):
    model = Group
    paginate_by = 100
    template_name = "groups/list.html"
    ordering = ["-active", "name"]

    def get_queryset(self) -> QuerySet[T]:
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs


class GroupsCreateView(LoginRequiredMixin, CreateView):
    model = Group
    fields = ["name"]
    template_name = "groups/create.html"
    success_url = "/ibkr/groups"


class GroupDetailView(LoginRequiredMixin, DetailView, UpdateView):
    model = Group
    template_name = "groups/detail.html"
    form_class = GroupForm
    success_url = "/ibkr/groups/"


class TradeListView(LoginRequiredMixin, django_filters.views.FilterView):
    model = Trade
    template_name = "trades/list.html"
    paginate_by = 100
    filterset_class = TradeListFilterSet
    ordering = ["-executed_at"]

    def get_queryset(self) -> QuerySet[T]:
        qs = super().get_queryset()  # to work with django-filters
        qs = qs.filter(user=self.request.user)
        qs = qs.prefetch_related("groups")
        return qs


class TradeDetailView(LoginRequiredMixin, DetailView, UpdateView):
    model = Trade
    template_name = "trades/detail.html"
    success_url = "/ibkr/trades/"
    form_class = TradeForm
