from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Result


class Result_Create(CreateView):
    model = Result
    fields = "__all__"
    success_url = reverse_lazy("list_url")


class Result_List(ListView):
    model = Result


class Result_Detail(DetailView):
    model = Result


class Result_Update(UpdateView):
    model = Result
    fields = "__all__"
    success_url = reverse_lazy("list_url")



class Result_Delete(DeleteView):
    model = Result
    success_url = reverse_lazy("list_url")

